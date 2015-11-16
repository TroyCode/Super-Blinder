import os
import argparse
import time
from app import youtube
from app import audio

BASE_DIR = "/home/troy/project/SuperBlinder/"
MEDIA_DIR = BASE_DIR + "tmp/media/"
SEGMENT_DIR = BASE_DIR + "tmp/segment/"
MESSAGE_COUNT = 0
START_TIME = time.time()

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
audio.split(converted_path, output_dir)

st_split = time.time()

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
t_total = st_split - START_TIME
print "Time: download {}secs".format(round(t_download, 1))
print "      convert  {}secs".format(round(t_convert, 1))
print "      split    {}secs".format(round(t_split, 1))
print "      total    {}secs".format(round(t_total, 1))