import pafy
import argparse

# python arguements parser
parser = argparse.ArgumentParser()
parser.add_argument("videoId", help="the video ID that will be downloaded")
args = parser.parse_args()

# pafy module
video_id = args.videoId
video = pafy.new(video_id)
audiostreams = video.audiostreams

# a_len = len(audiostreams)

# select the most light weight file to download
# prepare = audiostreams[a_len-1]
# filename = video_id + prepare.extension
# prepare.download(filepath=filename)

class test:
  def __init__(self, args.videoId):
    print args.videoId

a = test(args)