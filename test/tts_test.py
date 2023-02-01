import logging, asyncio, aiohttp, os

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s %(thread)s %(funcName)s %(message)s")

async def tts(sentence):
    response = {}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    post_data = {
        'text': sentence,
        'key': '7E779A1361C138D4',
        'voice': 'voice2'
    }
    async with aiohttp.ClientSession() as session:
        async with session.post("http://api.privox.io/tts", headers=headers, data=post_data) as resp:
            try:
                response = await resp.read()
            except:
                #print("Warning! exception in write transaction. this usually means an error from the cgi-bin endpoint")
                pass

            return response
    return response

async def main(sentence):
    loop = asyncio.get_running_loop()
    logging.info("Transcribing the following sentence ---> %s" % (sentence,))
    wav_data = await tts(sentence)
    logging.info( "Received %s bytes" % (len(wav_data),) )

    # save file for aplay
    fh = open("junk.wav", "wb")
    fh.write(wav_data)
    fh.close()

    logging.info("produced %s seconds of audio" % (len(wav_data) / (22050 * 2)),)

    os.system("date;aplay junk.wav;date")

def speak(text):
    asyncio.run(main(text))

if __name__ == "__main__":
    speak("Testing one two three.")

