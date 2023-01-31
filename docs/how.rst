How It Works
************

.. toctree::
   :maxdepth: 2

.. figure:: _static/PriVox_PVX.png
   :class: with-border

   PriVox Voice Exchange System Overview


========
Overview
========

Central to the Privox voice exchange is the notion of a producer farm. A producer farm 
is a publicly available endpoint which socket consumers and producers can connect to. 
It acts as an anonymous directory connecting producers with consumers in a pseudo random manner.

The API servers will take an inbound request and select a producer farm to deliver the 
request to. The producer farm will decide which producer node to forward the request to. Neither
endpoint knows anything about the other. 

Privox maintains a set of Privox controlled producer farms and associated static producer 
nodes, but most producer farms are user contributed as are most producer nodes.

When a request is received by an API server (api.privox.io/stt for example), it selects a user
powered producer farm and sends it the request. If that fails it will try a second and if that
fails, it will fallback to an organizational producer farm.

Currently the producer farm work distribution strategy is simply to spin thru the list of 
available producer nodes in an array which is organized by time connected and forward the 
request to the first idle connection found. Obviously this can be improved upon in the future
as may the API server farm selection strategy.


======
Detail
======
Currently, all producer nodes are pull producer nodes. This means they connect to a producer
farm and wait for requests. Pull producer nodes adhere to the Privox pull node protocol which
is a very simple fixed length header followed by a more specific command. See the `repository`_
under the 'farm/' directory for the code that pushes the requests and see the 'producer/'
directory for the code that services those requests.


.. _repository: https://github.com/PrivoxAnon1/privox


------------
API CGI Code
------------

The API CGI code may be found under the 'api/cgi/' directory. This code selects the producer 
farm and handles associated retry logic. The APIs are standard python CGI scripts which are
designed to be run by an Apache or nginx webserver, though they are easily adaptable to other
servers like flask or lighthttpd. 

The main stt.py (tts.py is very similar) code looks like this ...


**Python**

.. code-block:: python
   :linenos:

   while retry_ctr > 0 and result != '':
       stt_cgi.transcriber.farm = get_producer_farm()
       stt_cgi.transcribe()
       result = stt_cgi.transcriber.err_msg
       bark("stt retrys left = %s, result = %s" % (retry_ctr, result))
       retry_ctr -= 1


The get_producer_farm() method tries to select a random farm from the current directory of
farms. 



**Python**

.. code-block:: python
   :linenos:

   PRODUCER_FARMS = ['pfalpha', 'pfbeta']

   def get_producer_farm():
       max_val = len(PRODUCER_FARMS)
       rnd_val = int( random.random() * 100 ) % max_val
       return PRODUCER_FARMS[rnd_val] + ".privox.io"


The following files may be found under the 'api/cgi/' directory of the repository.

* cgi_config.py - configuration values
* cgi_util.py - utility functions
* stt.py - main http entry point, selects producer farm
* stt_cgi.py - cgi form validator
* stt_remote_transcriber.py - sends request to producer farm
* tts.py - main http entry point, selects producer farm
* tts_cgi.py - cgi form validator
* tts_remote_transcriber.py - sends request to producer farm


------------------
Producer Farm Code
------------------

The producer farm code may be found under the 'farm/' directory. The producer farm
is a simple socket server. It takes either 'tts' or 'stt' on the command line which
means the same server base code is used for both. The server launches a consumer 
socket or producer socket based on the response to the 'who' field in the initial
socket bring up sequence.

* privox_config.py - configuration values
* privox_utils.py - utility functions
* privox_socket_server.py - pass 'tts' or 'stt' on command line
* stt_socket_consumer.py - socket handler for stt consumers
* stt_socket_producer.py - socket handler for stt producers
* tts_socket_consumer.py - socket handler for tts consumers
* tts_socket_producer.py - socket handler for tts producers



------------------
Producer Node Code
------------------

The producer node code is the code which runs on a contributor's machine. It may be 
found in the 'producer/' directory of the repository.

* install.sh - install script installs both tts and stt on your machine
* prime.sh - loads all models for tts and stt
* start.sh - runs a tts and stt node
* stt_producer_socket.py - stt producer node
* tts_producer_socket.py - tts producer node


