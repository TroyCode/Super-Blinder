import pafy

video_id = "3B_1itqCKHo"
video = pafy.new(video_id)

print video.title

audiostreams = video.audiostreams

for a in audiostreams:
  print(a.bitrate, a.extension, a.get_filesize())

a_len = len(audiostreams)
print a_len

prepare = audiostreams[a_len-1]

prepare.download(filepath="3B_1itqCKHo." + prepare.extension)