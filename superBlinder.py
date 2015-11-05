import os
import argparse
from app import youtube
from app import audio

BASE_DIR = "/home/troy/project/SuperBlinder/"
MEDIA_DIR = BASE_DIR + "tmp/media/"
SEGMENT_DIR = BASE_DIR + "tmp/segment/"

parser = argparse.ArgumentParser(description='')
parser.add_argument('--videoId', help='youtube video ID')
args = parser.parse_args()

# create new video instance
# select the minimum audio to download
vid = args.videoId
v = youtube.Video(vid)
v.audio_download_min(MEDIA_DIR)

# convert to wav mono
input_path = MEDIA_DIR + v.id + "." + v.audio_extension
output_path = MEDIA_DIR + v.id + ".wav"
command = 'ffmpeg -i {input} -acodec pcm_s16le -ac 1 -ar 16000 {output}'.format(
  input=input_path, 
  output=output_path
  )
os.system(command)

# split
input_path = MEDIA_DIR + v.id + ".wav"
output_dir = SEGMENT_DIR
audioSegment.split(input_path, output_dir)