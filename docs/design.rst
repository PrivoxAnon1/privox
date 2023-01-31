Design Guide
************

.. toctree::
   :maxdepth: 2


========
Overview
========

The Privox private voice exchange provides users with a free, privacy respecting, anonymous, user
powered voice network, however, it has its limitations. These arise from the small size of the 
network initially and as the network grows these limitations will disappear, however, they exist
today and so to effectively use the exchange you will need to be aware of its current limitations.

===========
Public APIs
===========

------------------
Speech Recognition
------------------

The Privox voice network is a bit different than your average big name provider. For one, the speech
recognition issues associated with computing power are something you would not normally have to
concern yourself with. The whole concept of a quality speech second does not exist when you hit the
API of a properly funded provider. 

So to effectively use the Privox voice exchange you will need to be somewhat aware of its limitations.
The computing power of the private voice exchange (PVX) is provided by users. Most users do not have
machines capable of handling the larger models. As a result, you should only specify a model that
starts with the letter 'x' (xcribe and xcribe2) when you require the best accuracy possible. This is
what we call 'transcription' quality. In the future there will be specific producer farms dedicated
to this type of traffic, but for the initial releases this is not the case so if you use one of the 
transcribe models it will take about ten times as long as your input file length in seconds to turn
around the response. This would be less than ideal for most applications other than transcription.

Voice assistants and other real-time applications should specify the 'tiny' or 'base' models and if
possible, specify the 'English' language as these smaller models have 'English' only versions which
may provide improved performance. 

Here are a few data structures from the `repository`_ which should demonstrate a few basic issues 
voice developers should be aware of.



**Python**

.. code-block:: python
   :linenos:

   quality_to_model = {
            'fast':'tiny',
            'normal':'base',
            'better':'small',
            'best':'medium',
            'xcribe':'large',
            'xcribe2':'large-v2'
        }

   quality_to_multiplier = {
            'fast': 1,
            'normal': 2,
            'better': 4,
            'best': 8,
            'xcribe': 16,
            'xcribe2': 32
        }

Users of the Whisper STT models will recognize the entries as they abstact out the Whisper recognition models.


The transcription time for a five second audio input can range from a half a second (using the 'tiny.en' model)
to over seventeen seconds (using the 'xcribe2' model). 


* Tiny - 0.5
* Base - 1.0
* Small - 3.0
* Medium - 9.0
* Large - 17.5
* LargeX2 - 17.5


Which is why real-time applications should stick with the smaller models. 


----------------
Voice Generation
----------------

Voice (TTS) is currently provided by the Coqui TTS engine, though this will expand in the near future as 
other engines are added (note this will also be the case for STT as new recognizer engines are added).

The interface is abstract and extremely limited. Currently only two voices are supported, a high pitched and low
pitched voice. No other voice parameters are currently supported. Note it is on the roadmap to expand on this
soon and python contributors are encouraged to address this issue as it can improve the user experience significantly.


===============
Running Locally
===============

Running a local or edge device is a great alternative if your needs are more than the public APIs can provide. Privox
encourages open source development and is simply a wrapper around a couple of other key open source technologies which 
you already have loaded if you contributed to the PVX (and if not, shame on you), so using Whisper (STT) and/or Coqui
(TTS) locally is a relatively trivial issue as shown below ...


.. code-block:: bash


   $ arecord -f s16_le -c 1 -r 16000 | python closed_caption.py

   Recording WAVE 'stdin' : Signed 16 bit Little Endian, Rate 16000 Hz, Mono
   STT Transcriber: Running

   Testing, one, two, three. [Took 3.95 to transcribe 42240 bytes]
   What time is it? [Took 3.80 to transcribe 23040 bytes]
   What is? [Took 3.71 to transcribe 10560 bytes]
   today's date. [Took 3.55 to transcribe 24000 bytes]
   What is today's? [Took 3.79 to transcribe 29760 bytes]
   date. [Took 3.51 to transcribe 11840 bytes]
   What is today's date? [Took 3.81 to transcribe 41920 bytes]
   This was using the small model. [Took 3.88 to transcribe 57920 bytes]


Note this example code comes from the `repository`_ in the 'test/' directory. As you can see
the silence detector could use some work.


.. _repository: https://github.com/PrivoxAnon1/privox


