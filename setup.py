import os

command = 'sudo pip install --upgrade {package}'.format(
  package="MySQL-python \
           google-api-python-client \
           pafy \
           pydub \
           SpeechRecognition" 
  )
os.system(command)