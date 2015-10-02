#!/usr/bin/env python3

import speech_recognition as sr

# obtain path to "test.wav" in the same folder as this script
from os import path

file = open("newfile.txt", "w")

for x in range(0, 64):
  filename = "chunk{0}.wav".format(x)
  WAV_FILE = path.join(path.dirname(path.realpath(__file__)), filename)

  # use "test.wav" as the audio source
  r = sr.Recognizer()
  with sr.WavFile(WAV_FILE) as source:
      audio = r.record(source) # read the entire WAV file

  # recognize speech using Google Speech Recognition
  try:
      # for testing purposes, we're just using the default API key
      # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
      # instead of `r.recognize_google(audio)`
      file.write(filename + ": " + r.recognize_google(audio) + "\n")
  except sr.UnknownValueError:
      file.write(filename + ": " + "Google Speech Recognition could not understand audio" + "\n")
  except sr.RequestError:
      file.write(filename + ": " + "Could not request results from Google Speech Recognition service" + "\n")

