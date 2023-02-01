import whisper, time

audioPath = "five_seconds.wav"

model_names = [
        'tiny',
        'tiny.en',
        'base',
        'base.en',
        'small',
        'small.en',
        'medium',
        'medium.en',
        'large',
        'large-v1',
        'large-v2'
        ]

for model_name in model_names:
    model = whisper.load_model(model_name)
    start = time.time()
    res = model.transcribe(audioPath, fp16=False, language='English')['text'].strip()
    took = time.time() - start
    print(model_name, took)
    start = time.time()
    res = model.transcribe(audioPath, fp16=False, language='English')['text'].strip()
    took = time.time() - start
    print(model_name, took)
    print("============================")

