import subprocess
import re
import os

command = "pactl list sink-inputs"
output = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True, universal_newlines=True).communicate()[0]
print(output)

# Extract the sink input ID
id_regex = r"Sink Input #(\d+)"
ids = re.findall(id_regex, output)

# Extract the application name
app_regex = r"application.name = \"(.*?)\""
apps = re.findall(app_regex, output, re.DOTALL)

# Extract the volume percentage
vol_regex = r"Volume:\s+.*?(\d+)%\s"
volumes = re.findall(vol_regex, output, re.DOTALL)

# Print the sink input ID, application name, and volume for each audio stream
for i in range(len(ids)):
    print(f"Sink Input ID: {ids[i]}, Application Name: {apps[i]}, Volume: {volumes[i]}%")

# Buscar las líneas que contienen la información de la aplicación
# app_lines = [line.strip() for line in output.splitlines() if "application.name" in line]

# # Imprimir el nombre de la aplicación para cada línea encontrada
# app_names = []
# for app_line in app_lines:
#     app_name = app_line.split("=")[1].strip()
#     print(app_name)
#     # Los nombres se encontrarán en minusculas, es mejor manejarlos así
#     app_names.append(str(app_name).lower().strip())



# # Página de la librería
# import pulsectl

# # Conectar al servidor de sonido PulseAudio
# pulse = pulsectl.Pulse('my-client-name')

# # Obtener el objeto de control de volumen para la aplicación
# sink_input_list = pulse.sink_input_list()
# for i in sink_input_list:
#     # El listado arroja los nombres usando codificacion por lo que hay que hacer un cast
#     if str(i.proplist.get('application.process.binary')) == 'firefox':
#         sink_input = pulse.sink_input_info(i.index)
#         volume = sink_input.volume
#         break
#     else:
#         print("No es lo mismo")

# # Obtener el volumen actual
# current_volume = volume.value_flat

# # Establecer el volumen al porcentaje deseado
# new_volume_val = float(1 * 1)
# new_volume = pulsectl.PulseVolumeInfo(new_volume_val, len(volume.values))
# pulse.volume_set(sink_input, new_volume)

# # SteamOS parece usar pipewire por defecto
# import pulsemixer

