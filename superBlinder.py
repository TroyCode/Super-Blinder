import os
import argparse
from app import youtubePafy

parser = argparse.ArgumentParser(description='')
parser.add_argument('--videoId', help='youtube video ID')
args = parser.parse_args()

vid = args.videoId
v = youtubePafy.Video(vid)
print v.video.title
# v.min_audio_download()
# command = ""
# os.system("ffmpeg -i 111.mp3 -acodec pcm_s16le -ac 1 -ar 16000 out.wav")