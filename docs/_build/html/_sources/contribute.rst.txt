Contributing
************

.. toctree::
   :maxdepth: 2


============
Installation
============

----------
Clone Repo
----------

.. code-block:: bash

   git clone https://github.com/PrivoxAnon1/privox.git


------------------
Run install script
------------------

.. code-block:: bash

   cd Privox
   ./producer/install.sh

This will install the TTS and STT packages and create the necessary directory structure.

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


