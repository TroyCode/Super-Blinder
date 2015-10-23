import pafy
import argparse

class Video:
  video_id = ""

  def __init__(self, videoId):
    self.video_id = videoId

  def min_audio_download(self, directory=None):
    video = pafy.new(self.video_id)
    audiostreams = video.audiostreams
    a_len = len(audiostreams)

    # select the most light weight file to download
    prepare = audiostreams[a_len-1]
    filename = self.video_id + '.' + prepare.extension
    path = directory + '/' + filename
    prepare.download(filepath=path)