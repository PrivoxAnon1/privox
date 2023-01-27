import requests, time, sys, os
# python3 post_tts.py API_KEY

if len(sys.argv) < 2:
    print("Missing API Key!")
    quit()

key = sys.argv[1]

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

form_data = {
    'voice': 'voice2',
    'key': key,
    'text': 'Your test seems to be working.'
}

print("Sending request %s" % (form_data,))
start = time.time()

response = requests.post('http://api.privox.io/cgi-bin/tts.py', headers=headers, data=form_data)

took = int(time.time() - start)

print("Took %s seconds" % (took,))

if len(response.content) < 500:
    print("Error %s" % (response.content,))
else:
    fh = open("tts.wav", "wb")
    fh.write(response.content)
    fh.close()
    os.system("aplay tts.wav")

