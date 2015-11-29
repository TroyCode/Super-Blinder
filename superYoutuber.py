import os
import argparse
import json
from app import audio
from app import youtube
from app import stastics


BASE_DIR = "/home/troy/project/SuperBlinder/"
APP_DIR = BASE_DIR + "app/"
JSON_PATH = BASE_DIR + "tmp/json/"
MEDIA_DIR = BASE_DIR + "tmp/media/"
SEGMENT_DIR = BASE_DIR + "tmp/segment/"


def stopword_filter(sentence):
  stopword_path = APP_DIR + "stopword.txt"
  f = open(stopword_path, 'r')
  stopwords = []
  for line in f:
    word_list = line.split()
    for word in word_list:
      stopwords.append(word.lower())

  words = sentence.split()
  key_list = []
  for key in words:
    key = key.lower()
    if key not in stopwords:
      key_list.append(key)

  return key_list

def convert_mono(input_path, output_path):
  command = 'ffmpeg -i {input} -acodec pcm_s16le -ac 1 -ar 16000 {output}'.format(
    input=input_path, 
    output=output_path
    )
  os.system(command)

parser = argparse.ArgumentParser(description='')
parser.add_argument('--videoId', help='youtube video ID')
args = parser.parse_args()

# time and word stastics instance
stic_t = stastics.Times()
stic_w = stastics.Words()

# create new video instance
# select the minimum audio to download
vid = args.videoId
v = youtube.Video(vid)
v.audio_download_min(MEDIA_DIR)
stic_t.add_stamp("download")

# path varible
input_path = MEDIA_DIR + v.id + "." + v.audio_extension
converted_path = MEDIA_DIR + v.id + ".wav"

# convert
convert_mono(input_path, converted_path)
stic_t.add_stamp("convert")

# split
output_dir = SEGMENT_DIR
split_count = audio.split(converted_path, output_dir)
stic_t.add_stamp("split")

# transcript
timeline = 0.0
datalist = []
for i in range(0, split_count-1):
  filepath = SEGMENT_DIR + v.id + "_{}".format(i) + ".wav"
  dur = audio.wav_duration(filepath)
  print "processing({}/{}):  length:{}  accmulation:{}".format(
    i+1, split_count, round(dur, 1), round(timeline, 1))
  if dur == 0:
    print "\t# skip (0 sec)"
  elif dur < 30:
    sentence = audio.transcript(filepath)
    keys = stopword_filter(sentence)    
    stic_w.add_list(keys, timeline)
    data = {"time": round(timeline, 1), "sentence":sentence, "keywords":keys}
    datalist.append(data)
    timeline = timeline + dur
  else:
    timeline = timeline + dur
    print "\t# skip (over 30 secs)"
stic_w.dic_sort()

# json output
f = open(JSON_PATH+v.id+".json", 'w')
f.write(json.dumps(datalist))
f = open(JSON_PATH+v.id+"_stic.json", 'w')
f.write(json.dumps(stic_w.count_list))
stic_t.add_stamp("transcript")

# delete all temprory file
os.system("rm {path}".format(path=input_path))
print "original file has been deleted."
os.system("rm {path}".format(path=converted_path))
print "converted file has been deleted."
os.system("rm {path}".format(path=SEGMENT_DIR+v.id+"*"))
print "splited file has been deleted."

stic_t.print_result()