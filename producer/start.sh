#!/bin/bash
# Usage
#  ./start.sh API_KEY
source venv_producer/bin/activate
nohup python -u stt_producer_socket.py $1 pfalpha > logs/stt.out 2>&1 &
nohup python -u stt_producer_socket.py $1 pfbeta > logs/stt.out 2>&1 &

nohup python -u tts_producer_socket.py $1 pfalpha > logs/tts.out 2>&1 &
nohup python -u tts_producer_socket.py $1 pfbeta > logs/tts.out 2>&1 &

