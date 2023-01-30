#!/usr/bin/python3
import random, codecs, time, sys, os
from cgi_util import bark, bail
from stt_cgi import STT_CGI

PRODUCER_FARMS = ['pfalpha', 'pfbeta']

def get_producer_farm():
    max_val = len(PRODUCER_FARMS)
    rnd_val = int( random.random() * 100 ) % max_val
    return PRODUCER_FARMS[rnd_val] + ".privox.io"

writer = codecs.getwriter('utf8')(sys.stdout.buffer)
bark("*** stt.py start processing request ***")

stt_cgi = STT_CGI("remote")
if stt_cgi.error_msg != '':
    bail(stt_cgi.error_msg)

stt_cgi.process_form()
if stt_cgi.error_msg != '':
    bail(stt_cgi.error_msg)

retry_ctr = 3
result = 'err'
while retry_ctr > 0 and result != '':
    stt_cgi.transcriber.farm = get_producer_farm()
    stt_cgi.transcribe()
    result = stt_cgi.transcriber.err_msg
    bark("stt retrys left = %s, result = %s" % (retry_ctr, result))
    retry_ctr -= 1

if result != '':
    # no choice but to fallback
    bark("STT FALLBACK !!!!!!!!!!!!!")
    stt_cgi.transcriber.farm = 'pfreserved.privox.io'
    stt_cgi.transcribe()
    result = stt_cgi.transcriber.err_msg
    
text = stt_cgi.transcriber.text
bark("stt.py: result is %s, text type is %s and text is %s" % (result, type(text), text))

print('Content-Type: text/plain\r\n\r\n', end='')
sys.stdout.flush()
print(text,file=writer)
sys.stdout.flush()

