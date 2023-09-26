import os
import subprocess
from adx2wav import adx2wav

input_directory = "./bgm"  # Change this to the path to the directory with . ADX
output_directory = "./output"  # Change this to the path to the directory where to save the files. .WAV

# List all files in the input directory
files = os.listdir(input_directory)

# Filter the . ADX
adx_files = [file for file in files if file.lower().endswith(".adx")]

# Convert each .ADX to .WAV
for adx_file in adx_files: # For one by one in adx_files
    input_file = os.path.join(input_directory, adx_file) # Added directory and file to wav converted
    with open(input_file , "rb") as f: # Read this file
        data = f.read() # This is save in data
    wav = adx2wav(data) # After converted to wav
    output_file = os.path.join(output_directory, adx_file[:-4] + ".wav")
    with open(output_file , "wb") as f: # Write this, but overwrite this
        f.write(wav) # Overwrite
