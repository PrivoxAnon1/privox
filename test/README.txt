Simple tests and relatd files


To run basic tests, run 

  ./basic_tests.sh MYKEY


To run the closed_caption example, make sure to source your
virtual environment where you pipped Whisper before you run this

  arecord -f s16_le -c 1 -r 16000 | python closed_caption.py

Note this runs locally and does not use the cloud


python3 post_api.py API_KEY

will post a wav file to the stt endpoint and print the resultant text.
