import wave
import contextlib
from pydub import AudioSegment
from pydub.silence import split_on_silence

# using pydub
def split(input_path, output_directory=None, output_name='chunk'):
  print "Start cutting"
  sound = AudioSegment.from_wav(input_path)

  chunks = split_on_silence(sound, 
    # must be silent for at least half a second
    min_silence_len = 500,

    # consider it silent if quieter than -50 dBFS
    silence_thresh = -50
  )

  # i for the output file count
  i = 0
  for i, chunk in enumerate(chunks):
    chunk.export("{0}chunk{1}.wav".format(output_directory, i), format="wav")

  print 'There are splited into {number} files'.format(number=i + 1)

# using wave and contextlib
def wav_duration(input_path):
  with contextlib.closing(wave.open(input_path, 'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    return duration