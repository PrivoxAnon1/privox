Using Privox
************

.. toctree::
   :maxdepth: 2

Privox is accessed by doing an HTTP post to one of the public APIs (STT or TTS) and providing the proper input for the operation. These are summarized below.

===
STT
===

---
key
---

   The user's API key. This key may be found on your profile page.

   *default = none, this is a required parameter*

-------
quality
-------

   One of 'fast', 'normal, 'better', best', 'xcribe' or 'xcribe2' representing the quality of transcription being requested from least to most accurate.

   *default = fast*

--------
language
--------

   The language of the resultant text being requested. If you specifiy a different language than what you provided in the wav file, the system will attempt to translate. This does not work well with the smaller/faster models. Transcription will be faster for english if you specify english.

   *default = English*


-----
xlate
-----

   If this field is posted it must contain the value 'xlate'. It is used to tell the API the wav data is not in the proper format and it must be converted before being interpreted. This adversely impacts performance and should be avoided. It is typically used by Javascript.

   *default = None*

----------
*Examples*
----------

**Curl**

.. code-block:: bash

   # minimum input
   curl -X POST http://api.privox.io/stt -F "file=@wav_files/sample.wav" -F "key=X"

   # normal English usage
   curl -X POST http://api.privox.io/stt -F "file=@wav_files/sample.wav" -F "quality=fast" -F "language=English" -F "key=X" 

   # normal French usage
   curl -X POST http://api.privox.io/stt -F "file=@wav_files/parlez_vous.wav" -F "quality=best" -F "language=French" -F "key=X"

   # transcription quality
   curl -X POST http://api.privox.io/stt -F "file=@wav_files/sample.wav" -F "quality=xcribe2" -F "language=English" -F "key=X" 


**Bash**

.. code-block:: bash

   # test and time using compression
   # usage ./this_file.sh API_KEY FILENAME.WAV
   date
   cp $2 sample.wav
   zip archive.zip sample.wav
   curl -X POST -F "file=@archive.zip" -F "quality=normal" -F "language=en" -F "key=$1" api.privox.io/stt
   date


**Python**

.. code-block:: python
   :linenos:

   import requests
   # stt example

   stt_uri = 'http://api.privox.io/cgi-bin/stt.py'

   with open('mydata.wav')as f: data = f.read()

   form = {
     'file': data,
     'key': 'my-api-key',
     'model': 'fast'
     }

   response = requests.post(stt_uri, files=form)

   print(response.content.decode('utf-8').strip())



===
TTS
===

---
key
---

   The user's API key. This key may be found on your profile page.

   *default = none, this is a required parameter*


-----
voice
-----

   Either 'voice1' or 'voice2'. 

   *default = voice1*


--------
language
--------

   The language for the voice. Currently ignored.

   *default = English*


----
text
----

   The text string to convert to a wav file. 

   *default = none, this is a required parameter*


----------
*Examples*
----------


**Curl**

.. code-block:: bash

   # minimum input
   curl -X POST http://api.privox.io/tts -H "Content-Type: application/x-www-form-urlencoded" -d "key=XXX&text=Test utterance." | aplay

   # normal usage
   curl -X POST http://api.privox.io/tts -H "Content-Type: application/x-www-form-urlencoded" -d "key=XXX&language=en&voice=voice2&text=Test utterance." > junk.wav

   # time it
   date;curl -X POST http://api.privox.io/tts -H "Content-Type: application/x-www-form-urlencoded" -d "key=XXX&text=Test utterance." > tts.wav;date;aplay tts.wav


