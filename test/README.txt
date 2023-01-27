Simple tests and relatd files


To run basic tests, run 

  ./basic_tests.sh MYKEY

This will run a few STT and TTS examples through the cloud APIs.


To run the closed_caption example, make sure to source your
virtual environment where you pipped Whisper before you run this

  arecord -f s16_le -c 1 -r 16000 | python closed_caption.py

Note this runs locally and does not use the cloud. If you are 
on a Mac or system without arecord/aplay you can try sox ...

  rec -r 16000 -c 1 -b 16 -t wav - | python closed_caption.py


This is a short python http post request example which uses 
the cloud API.

  python3 post_api.py API_KEY

will post a wav file to the stt endpoint and print the resultant text.

Due to the silly, non-json cgi interface employed by the APIs
there is no easy way to determine a TTS request failed. This code
shows one way which is to use the size of the response. An alternative
approach could simply try to decode the wav data and catch the exception.


