import requests, time
# stt example

stt_uri = 'http://api.privox.io/cgi-bin/stt.py'

with open('wav_files/sample.wav', 'rb')as f: data = f.read()

form = {
  'file': data,
  'language': 'English',
  'key': 'my-api-key',
  'model': 'fast'
  }

start_time = time.time()
response = requests.post(stt_uri, files=form)
end_time = time.time()
response = response.content.decode('utf-8').strip()
print("Took %.2f seconds: %s" % ( (end_time - start_time), response) )

