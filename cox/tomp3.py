import os
from pydub import AudioSegment

def convert_wav_to_mp3(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".wav"):
            wav_path = os.path.join(folder_path, filename)
            
            print("123",wav_path)
            mp3_path = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.mp3")
            AudioSegment.from_wav(wav_path).export(mp3_path, format="mp3")
            print(f"Converted {wav_path} to {mp3_path}")

folder_path = r"C:\Users\james\Desktop\DECO3500\cox"
convert_wav_to_mp3(folder_path)
