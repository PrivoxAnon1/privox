#!/bin/bash
# STT
echo 'Sending this wav file'
aplay wav_files/sample.wav
date;curl -X POST -F "file=@wav_files/sample.wav" -F "quality=fast" -F "language=English" -F "key=$1" api.privox.io/stt;date
echo ' '

echo 'Sending a three second wav file'
aplay wav_files/three_seconds.wav;date;curl -X POST -F "file=@wav_files/three_seconds.wav" -F "quality=fast" -F "language=English" -F "key=3C338479FCA6AF07" api.privox.io/stt;date
echo ' '

# TTS
echo 'speak(Who killed Abraham Lincoln and why.)'
date;curl -X POST http://api.privox.io/tts -H "Content-Type: application/x-www-form-urlencoded" -d "key=$1&language=en&voice=voice2&text=Who killed Abraham Lincoln and why." > junk.wav;date;aplay junk.wav
echo ' '

echo 'speak(It is seventy five degrees and sunny out.)'
date;curl -X POST http://api.privox.io/tts -H "Content-Type: application/x-www-form-urlencoded" -d "key=$1&language=en&voice=voice1&text=It is seventy five degrees and sunny out." > junk.wav;date;aplay junk.wav
echo ' '


# Intl. STT
echo 'sending a french wav file. This will take longer (like 40 seconds) ...'
aplay wav_files/parlez_vous.wav
#date;curl -X POST -F "file=@wav_files/parlez_vous.wav" -F "quality=best" -F "language=French" -F "key=$1" api.privox.io/stt;date

rm junk.wav
