import os
import subprocess
from adx2wav import adx2wav

input_directory = "./bgm"  # Cambia esto por la ruta al directorio con archivos .ADX
output_directory = "./output"  # Cambia esto por la ruta al directorio donde guardar los archivos .WAV

# Lista todos los archivos en el directorio de entrada
files = os.listdir(input_directory)

# Filtra los archivos .ADX
adx_files = [file for file in files if file.lower().endswith(".adx")]

# Convierte cada archivo .ADX a .WAV
for adx_file in adx_files:#for one by one in adx_files
    input_file = os.path.join(input_directory, adx_file)#added directory and file to wav converted
    with open(input_file , "rb") as f:#read this file
        data = f.read()#this is save in data
    wav = adx2wav(data)#after converted to wav
    output_file = os.path.join(output_directory, adx_file[:-4] + ".wav")
    with open(output_file , "wb") as f:#write this, but overwrite this
        f.write(wav)#overwrite