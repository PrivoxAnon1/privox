#!/bin/bash
python3 -m venv venv_producer
source venv_producer/bin/activate
pip install webrtcvad
pip install git+https://github.com/openai/whisper.git
pip install -U TTS
mkdir logs
bash prime.sh
