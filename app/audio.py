import wave
import contextlib
from pydub import AudioSegment
from pydub.silence import split_on_silence
import speech_recognition as sr

# using pydub
def split(input_path, output_directory=None):
  print "Start cutting"
  sound = AudioSegment.from_wav(input_path)

  chunks = split_on_silence(sound, 
    # must be silent for at least half a second
    min_silence_len = 500,
    # consider it silent if quieter than -50 dBFS
    silence_thresh = -33
  )

  # export the chunk
  # i for the output file count
  i = 0
  slash_index = input_path.rfind("/") + 1
  filename = input_path[slash_index: -4]
  for i, chunk in enumerate(chunks):
    chunk.export("{dir}{name}_{count}.wav".format(
      dir=output_directory, 
      name=filename, 
      count=i), format="wav")

  print 'There are splited into {number} files'.format(number=i + 1)
  return i + 1

# using wave and contextlib
def wav_duration(input_path):
  with contextlib.closing(wave.open(input_path, 'r')) as f:
    frames = f.getnframes()
    rate = f.getframerate()
    duration = frames / float(rate)
    return duration

def transcript(input_path):
  r = sr.Recognizer()
  with sr.WavFile(input_path) as source:
      audio = r.record(source) 

  # recognize speech using Google Speech Recognition
  try:
      # for testing purposes, we're just using the default API key
      # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
      # instead of `r.recognize_google(audio)`
      return r.recognize_google(audio)
  except sr.UnknownValueError:
      # print "Google Speech Recognition could not understand audio"
      return ""
  except sr.RequestError:
      print "Could not request results from Google Speech Recognition service"
      return ""
