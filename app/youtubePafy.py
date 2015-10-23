import pafy
import argparse

class Video:
  video_id = ""
  video = pafy.new("9bZkp7q19f0")

  def __init__(self, videoId):
    self.video_id = videoId

  def audio_list(self):
    audiostreams = self.video.audiostreams
    for s in audiostreams:
      print s

  def min_audio_download(self, directory=None):
    audiostreams = self.video.audiostreams
    a_len = len(audiostreams)

    # select the most light weight file to download
    prepare = audiostreams[a_len-1]
    filename = self.video_id + '.' + prepare.extension
    path = directory + '/' + filename
    prepare.download(filepath=path)