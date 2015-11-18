import os
import argparse
import time
import json
from app import youtube
from app import audio

BASE_DIR = "/home/troy/project/SuperBlinder/"
APP_DIR = BASE_DIR + "app/"
JSON_PATH = BASE_DIR + "tmp/json/"
MEDIA_DIR = BASE_DIR + "tmp/media/"
SEGMENT_DIR = BASE_DIR + "tmp/segment/"
START_TIME = time.time()


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



parser = argparse.ArgumentParser(description='')
parser.add_argument('--videoId', help='youtube video ID')
args = parser.parse_args()

# create new video instance
# select the minimum audio to download
vid = args.videoId
v = youtube.Video(vid)
v.audio_download_min(MEDIA_DIR)
st_download = time.time()

# convert to wav mono
input_path = MEDIA_DIR + v.id + "." + v.audio_extension
converted_path = MEDIA_DIR + v.id + ".wav"
command = 'ffmpeg -i {input} -acodec pcm_s16le -ac 1 -ar 16000 {output}'.format(
  input=input_path, 
  output=converted_path
  )
os.system(command)

st_convert = time.time()

# split
output_dir = SEGMENT_DIR
split_count = audio.split(converted_path, output_dir)

st_split = time.time()

# transcript
timeline = 0
datalist = []
for i in range(0, split_count-1):
  filepath = SEGMENT_DIR + v.id + "_{}".format(i) + ".wav"
  sentence = audio.transcript(filepath)
  keys = stopword_filter(sentence)
  data = {"time": round(timeline, 0), "sentence":sentence, "keywords":keys}
  datalist.append(data)
  timeline = timeline + audio.wav_duration(filepath)


f = open(JSON_PATH+v.id+".json", 'w')
f.write(json.dumps(datalist))

st_tnf = time.time()



# delete all temprory file
os.system("rm {path}".format(path=input_path))
print "original file has been deleted."
os.system("rm {path}".format(path=converted_path))
print "converted file has been deleted."

st_done = time.time()

# calculate per processing time
t_download = st_download - START_TIME
t_convert = st_convert - st_download
t_split = st_split - st_convert
t_tns = st_tnf - st_split
t_total = st_tnf - START_TIME
print "Time: download   {}secs".format(round(t_download, 1))
print "      convert    {}secs".format(round(t_convert, 1))
print "      split      {}secs".format(round(t_split, 1))
print "      transcript {}secs".format(round(t_tns, 1))
print "      total      {}secs".format(round(t_total, 1))