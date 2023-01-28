.. Privox documentation master file, created by
   sphinx-quickstart on Fri Jan 27 13:32:28 2023.

PriVox.io Documentation 
=======================

Privox is a free, privacy respecting, anonymous, open source, user powered, distributed voice exchange.
You access it through the speech to text (STT) and text to speech (TTS) APIs ...


**Curl**

.. code-block:: bash

   # TTS
   curl -X POST http://api.privox.io/tts -H "Content-Type: application/x-www-form-urlencoded" -d "key=X&voice=voice2&text=Hello World." > tts_out.wav

   # STT
   curl -X POST http://api.privox.io/stt -F "file=@wav_files/parlez_vous.wav" -F "quality=best" -F "language=French" -F "key=X" > stt_out.txt


Index
=====

.. toctree::
   :maxdepth: 2

   intro
   audience
   overview
   use
   website
   repo
   contribute
   how
   ack

