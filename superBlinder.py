import os
import argparse
from app import youtube

MEDIA_PATH = "tmp/media"

parser = argparse.ArgumentParser(description='')
parser.add_argument('--videoId', help='youtube video ID')
args = parser.parse_args()

# create new video instance
# select the minimum audio to download
vid = args.videoId
v = youtube.Video(vid)
v.audio_download_min(MEDIA_PATH)

# convert to wav mono
origin_path = MEDIA_PATH + "/" + v.audio_filename
command = 'ffmpeg -i {input} -acodec pcm_s16le -ac 1 -ar 16000 {output}'.format(
  input=MEDIA_PATH+"/"+v.audio_filename, 
  output=MEDIA_PATH
  )
os.system(command)
