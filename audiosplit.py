import wave
import numpy as np
import os

def split_wav_file(input_file, output_dir):
    # Open the WAV file
    with wave.open(input_file, 'rb') as wf:
        # Get the parameters of the input WAV file
        params = wf.getparams()
        num_channels = params.nchannels
        sample_width = params.sampwidth
        frame_rate = params.framerate
        num_frames = params.nframes

        # Calculate the number of frames in 1 second
        frames_per_second = frame_rate
        frames_per_chunk = frames_per_second

        # Read and process each 1-second chunk
        for i in range(0, num_frames, frames_per_chunk):
            wf.setpos(i)
            chunk_frames = min(frames_per_chunk, num_frames - i)
            chunk_data = wf.readframes(chunk_frames)

            # Create a new WAV file for each chunk
            output_file = os.path.join(output_dir, f"chunk_{i // frames_per_second}.wav")
            with wave.open(output_file, 'wb') as output_wf:
                output_wf.setparams(params)
                output_wf.writeframes(chunk_data)

# Example usage
input_file = "speaker12.wav"
output_dir = "speaker12_chunks"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
split_wav_file(input_file, output_dir)
