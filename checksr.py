import os
import wave

def get_sampling_rate(audio_file):
    try:
        with wave.open(audio_file, 'rb') as audio:
            return audio.getframerate()
    except wave.Error:
        return None

def main(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.wav'):  # Assuming all audio files are in WAV format
            file_path = os.path.join(folder_path, file_name)
            sampling_rate = get_sampling_rate(file_path)
            if sampling_rate!=16000:
                print(f"{file_name}: {sampling_rate} Hz")
            #else:
            #    print(f"Failed to read {file_name}")

if __name__ == "__main__":
    folder_path = 'audio/speaker14'
    main(folder_path)
