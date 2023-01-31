Contributing
************

.. toctree::
   :maxdepth: 2


============
Installation
============

--------------
Clone the repo
--------------

.. code-block:: bash

   git clone https://github.com/PrivoxAnon1/privox.git


----------------------
Run the install script
----------------------

.. code-block:: bash

   cd Privox
   ./producer/install.sh

This will install the TTS and STT packages and create the necessary directory structure
which is basically a subdirectory named 'logs' to stick the log file output in. It will
also test each STT model and TTS voice. This is to preload the models so they are already
loaded once you begin producing.

You will only do this once. Depending on your system it could take close to 15 minutes 
to complete.


.. _my-section:

=========
Producing
=========

----------
Foreground
----------

Running a temporary producer node in the foreground is a great way to contribute immediately. 


.. code-block:: bash

   source venv_producer/bin/activate
   python stt_producer_socket.py MY_API_KEY

Congratulations! you are now contributing valuable resource to the voice exchange network. To
verify this you can look at the `about page`_ on the website and you should see the number of
available STT nodes increase by one. Your fellow consumers appreciate it.

Press Ctl+C at any time to stop the program.

.. _about page: https://privox.io/about


You can also specify the producer farm you want to connect to on the command line. By deault
pfAlpha is the first farm tried but you can override this behavior.


.. code-block:: bash

   python stt_producer_socket.py MY_API_KEY pfbeta


Or you can specify your own producer farm.


.. code-block:: bash

   python stt_producer_socket.py MY_API_KEY MY_PRODUCER_FARM_URI




----------
Background
----------

If you have an old desktop or laptop laying around doing nothing you can always run a couple of
producer nodes in the background. They consume very little in network badwidth and are a great
way to help the backend infrastructure distribute the traffic.


.. code-block:: bash

   #!/bin/bash
   # Usage
   #  ./start.sh API_KEY
   source venv_producer/bin/activate
   nohup python -u stt_producer_socket.py $1 pfalpha > logs/stt.out 2>&1 &
   nohup python -u stt_producer_socket.py $1 pfbeta > logs/stt.out 2>&1 &

   nohup python -u tts_producer_socket.py $1 pfalpha > logs/tts.out 2>&1 &
   nohup python -u tts_producer_socket.py $1 pfbeta > logs/tts.out 2>&1 &


------
Laptop
------

Laptops tend to shutdown when you close the lid, even if you leave them plugged in. To overcome this should you want to leave your laptop producing while you are away simply disable your laptop suspend behavior as described in the following articles ...

`Ask Ubuntu, Laptop Lid <https://askubuntu.com/questions/141866/keep-ubuntu-server-running-on-a-laptop-with-the-lid-closed>`_



