The Repository
**************

.. toctree::
   :maxdepth: 2

The repository contains all the code necessary to deploy the public voice exchange as
well as all the code necessary to run a local copy on a single machine. It is the code
the public voice exchange is currently running, though the cloud based voice network is
composed of several servers.

The repository is broken up into general areas of responsibility as follows.

===
API
===

Code in the api/ directory handles the public facing API calls. These are simple Python
CGI scripts which accept and validate the input and then in most cases the data is relayed
on to a producer farm.

The only time this is not the case is when the API CGI code is configured to produce immediately,
in which case the transcription is produced by the CGI script itself. 


==============
Producer Farms
==============

A producer farm is a publically accessible endpoint which can accept incoming socket requests
on a well known URI and port. The code in this directory provides the socket relay function by
dispatching two distinct types of sockets; consumers and producers.


==============
Producer Nodes
==============

Producer nodes are technically any endpoint that can transcribe, either STT or TTS. The code
in this directory is the code the pull producer nodes run. It connects to a producer farm at
a well know location and port and waits for requests to be pushed to it using a standard socket.

=================
Javascript Access
=================

The code under the web/ subdirectory contains the HTML, CGI and Javascript necessary to 
reproduce the functionality achieved by the website on its HTML test page. This code 
demonstrates the use of the 'xlate' flag which is necessary to convert from the ogg format
javascript sends to the wav format Privox requires. Note if you use this (basically the 
'xlate' flag) your api code will need to have 'ffmpeg' installed. See the api code for
more information.
