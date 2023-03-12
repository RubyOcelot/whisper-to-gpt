import sys
from pydub import AudioSegment

def devide_audio(audio_file, start_time, end_time, output_file):
    audio = AudioSegment.from_file(audio_file)
    audio = audio[start_time:end_time]
    audio.export(output_file, format="mp3")

def split_audio(audio_file_name, duration, num):
    audio = AudioSegment.from_file(audio_file_name)
    duration_ms = duration * 1000
    output_file_base_name = "tmp/"+audio_file_name.split(".")[0]
    for i in range(0, num):
        devide_audio(audio_file_name, i*duration_ms, (i+1)*duration_ms, output_file_base_name+"-"+str(i)+".mp3")

if __name__ == "__main__":
    audio_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    ten_seconds = 10 * 1000
    split_audio(audio_file_name, 10, 10)
