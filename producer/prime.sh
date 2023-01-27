###################
# load tts models #
###################
date
tts --text "Prime it!" --model_name tts_models/en/vctk/vits --speaker_idx p236 --out_path out.wav;aplay out.wav
date

date
tts --text "Prime it!" --model_name tts_models/en/vctk/vits --speaker_idx p270 --out_path out.wav;aplay out.wav
date

###################
# load stt models #
###################
echo ' '
echo '** MODEL: tiny.en **'
echo ' '
date
whisper --language English wav_files/three_seconds.wav --model tiny.en --fp16 False
date

echo ' '
echo '** MODEL: tiny **'
echo ' '
date
whisper --language French wav_files/parlez_vous.wav --model tiny --fp16 False
date

echo ' '
echo '** MODEL: base.en **'
echo ' '
date
whisper --language English wav_files/three_seconds.wav --model base.en --fp16 False
date

echo ' '
echo '** MODEL: base **'
echo ' '
date
whisper --language French wav_files/parlez_vous.wav --model base --fp16 False
date

echo ' '
echo '** MODEL: small.en **'
echo ' '
date
whisper --language English wav_files/three_seconds.wav --model small.en --fp16 False
date

echo ' '
echo '** MODEL: small **'
echo ' '
date
whisper --language French wav_files/parlez_vous.wav --model small --fp16 False
date

echo ' '
echo '** MODEL: medium.en **'
echo ' '
date
whisper --language English wav_files/three_seconds.wav --model medium.en --fp16 False
date

echo ' '
echo '** MODEL: medium **'
echo ' '
date
whisper --language French wav_files/parlez_vous.wav --model medium --fp16 False
date

echo ' '
echo '** MODEL: large **'
echo ' '
date
whisper --language English wav_files/three_seconds.wav --model large --fp16 False
date

echo ' '
echo '** MODEL: large-v2 **'
echo ' '
date
whisper --language French wav_files/parlez_vous.wav --model large-v2 --fp16 False
date

