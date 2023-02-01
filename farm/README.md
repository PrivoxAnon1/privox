# Privox Producer Farm

## Overview

A producer farm is a python asyncio socket server which understands two types of connections; a producer socket and a consumer socket. These are represented by the files xxx_socket_producer.py and xxx_socket_consumer.py where 'xxx' is either 'stt' or 'tts'. When an endpoint connects to the producer farm it will be asked to identify itself as either a producer ('c') or consumer ('s') in the 'who' exchange during the identity establishment phase.

Consumer sockets look for an available producer socket and request production.

Producer sockets wait for consumer requests, push the request down to the producer node, wait for the result and then update the consumer.

The producer farm understands these two basic types of sockets. The file privox_socket_server.py takes one parameter, a service type. This can be either 'stt' or 'tts'. The command ...

  python privox_socket_server.py stt

Will start a STT producer farm which by default listens for connections on port 1776. The command ...

  python privox_socket_server.py tts

Will start a TTS producer farm which by default listens for connections on port 1777. 

In both cases, an optional second parameter may be added to override the default ports of 1776 and 1777.

Typically the API CGI scripts which run on a different machine will validate the posted parameters and if valid, forward the request on to a producer farm. This is a consumer socket and the producer farm will start a consumer socket which as described above, will look for an available producer socket and request production.

## Current Farms

Currently three producer farms exist. 

pfalpha.privox.io
pfbeta.privox.io
pfinternal.privox.io

pfinternal is not publically available, however, the alpha and beta farms are available for public use and will be favored 
over internal resources when transcribing requests. 

## Create producer farm

mkdir logs

python3 -m venv venv_farm
source venv_farm/bin/activate

pip install aiohttp

nohup python -u privox_socket_server.py tts > logs/tts.out 2>&1 &
nohup python -u privox_socket_server.py stt > logs/stt.out 2>&1 &

To send your farm requests see the api/ directory. To connect to your farm and produce see the producer/ directory.


