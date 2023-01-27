import requests, time, sys
# python3 post_api.py API_KEY

if len(sys.argv) < 2:
    print("Missing API Key!")
    quit()

key = sys.argv[1]
filename = "wav_files/sample.wav"

fh = open(filename, "rb")
data = fh.read()
fh.close()

multipart_form_data = {
    'file': data,
    'key': key,
    'model': 'fast'
}

print("Sending wav file %s" % (filename,))
start = time.time()

response = requests.post('http://api.privox.io/cgi-bin/stt.py', files=multipart_form_data)

took = int(time.time() - start)

print("Took %s seconds" % (took,))
print(response.content.decode('utf-8').strip())
