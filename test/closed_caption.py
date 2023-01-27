import webrtcvad, whisper, signal, numpy, queue, time, sys
from io import BytesIO
from threading import Thread
"""
run like this ...

  arecord -f s16_le -c 1 -r 16000 | python closed_caption.py
  OR
  for Mac using sox
  rec -r 16000 -c 1 -b 16 -t wav - | python closed_caption.py
"""
def signal_handler(sig, frame):
    sys.stdout.buffer.flush()
    sys.exit(0)


def read_stdin_stream(handler, chunk_size=320):
    with sys.stdin as f:
        while True:
            buffer = f.buffer.read(chunk_size)
            if buffer == b'':
                break
            handler(buffer)


class SilenceDetector:
    def __init__(self):
        self.vad = webrtcvad.Vad()
        self.vad.set_mode(2)
        self.sample_rate = 16000
        self.state = 'idle'
        self.speech_buff = b''
        self.model_name = "tiny.en"
        self.model = whisper.load_model(self.model_name)
        self.queue = queue.Queue()
        self.consumer = Thread(target=self.convert_stt)
        self.consumer.start()


    def convert_stt(self):
        print('STT Transcriber: Running')
        while True:
            wav_data = self.queue.get()
            # check for stop
            if wav_data is None:
                break

            text = ""
            # Convert buffer to float32 using NumPy                                                                                 
            audio_as_np_int16 = numpy.frombuffer(wav_data, dtype=numpy.int16)
            audio_as_np_float32 = audio_as_np_int16.astype(numpy.float32)

            # Normalize float32 array so that values are between -1.0 and +1.0                                                      
            max_int16 = 2**15
            audio_normalised = audio_as_np_float32 / max_int16

            lang = 'English'
            start_time = time.time()
            text = self.model.transcribe(audio_normalised, fp16=False, language=lang)["text"].strip()
            elapsed = time.time() - start_time
            #print("%s [Took %s to transcribe %s bytes]" % (text, elapsed, len(wav_data)))
            print(text)

        print('STT Transcriber: Done')


    def process_data(self, buffer):
        if self.state == 'idle':
            if self.vad.is_speech(buffer, self.sample_rate):
                self.state = 'collecting'
                self.speech_buff = buffer
        else:
            if not self.vad.is_speech(buffer, self.sample_rate):
                if len(self.speech_buff) > 3000:
                    b1 = self.speech_buff[ : ]
                    self.queue.put(b1)
                    self.state = 'idle'
            else:
                self.speech_buff += buffer


def main():
    signal.signal(signal.SIGINT, signal_handler)

    sd = SilenceDetector()
    read_stdin_stream(sd.process_data)


if __name__ == "__main__":
    main()

