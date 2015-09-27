from pydub import AudioSegment
from pydub.silence import split_on_silence

sound = AudioSegment.from_wav("test.wav")

chunks = split_on_silence(sound, 
    # must be silent for at least half a second
    min_silence_len = 500,

    # consider it silent if quieter than -16 dBFS
    silence_thresh = -30
)

i = 0
for i, chunk in enumerate(chunks):
    chunk.export("chunk{0}.wav".format(i), format = "wav")

print 'There are splited into {number} files'.format(number = i + 1)