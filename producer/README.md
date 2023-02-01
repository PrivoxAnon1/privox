# Privox Producer Nodes

Simple python socket scripts which adhere to the Privox pull node protocol. 


## Problem

I'd like to contribute but I don't have a publically accessible URI and/or I only want to contribute on a temporary basis. 


## Solution

The producer node is designed to solve these issues. A producer node is a simple python script which opens a socket connection to a producer farm and waits for commands. 

It will be sent two commands. Either a ping command in which case it will send back the string 'pong', or a transcribe command in which case it will perform the transcription and send back the result. 

Producer nodes come in two flavors; stt or tts. 


## STT Producer

The STT producer is a python script which provides speech to text transcription using the Whisper speech to text models. 


## TTS Producer

The TTS Producer is a python script which provides text to speech transcription using the Coqui text to speech models. 


