import pafy

class Video:
  audio_extension = None

  def __init__(self, videoId):
    self.id = videoId
    self.video = pafy.new(videoId)

  def audio_list(self):
    audiostreams = self.video.audiostreams
    i = 1
    for s in audiostreams:
      print str(i) + ". " + str(s)
      i += 1

  def audio_download_min(self, directory=None):
    # create new audiostream
    audiostreams = self.video.audiostreams
    
    # select the most light weight file to download
    a_len = len(audiostreams)
    prepare = audiostreams[a_len-1]
    self.audio_extension = prepare.extension

    # process the filepath
    if directory:
      path = directory + self.id + '.' + self.audio_extension
    else:
      path = self.id + '.' + self.audio_extension
    prepare.download(filepath=path)