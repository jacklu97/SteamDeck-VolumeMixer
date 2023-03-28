import subprocess
import os

# # Ejecutar el comando pactl list sink-inputs y capturar la salida
# output = subprocess.check_output(["pactl", "list", "sink-inputs"]).decode()

# # Buscar las líneas que contienen la información de la aplicación
# app_lines = [line.strip() for line in output.splitlines() if "application.name" in line]

# # Imprimir el nombre de la aplicación para cada línea encontrada
# app_names = []
# for app_line in app_lines:
#     app_name = app_line.split("=")[1].strip()
#     print(app_name)
#     # Los nombres se encontrarán en minusculas, es mejor manejarlos así
#     app_names.append(str(app_name).lower().strip())



# Prueba del comando pactl usando otro método
# output = subprocess.Popen(f"pactl list sink-inputs", stdout=subprocess.PIPE, shell=True, env=self._get_dbus_env(self), universal_newlines=True).communicate()[0])
def _get_dbus_env():
    env = os.environ.copy()
    env["DBUS_SESSION_BUS_ADDRESS"] = f'unix:path=/run/user/{os.getuid()}/bus'
    return env


output = subprocess.Popen(f"pactl list sink-inputs", stdout=subprocess.PIPE, shell=True, env=_get_dbus_env(), universal_newlines=True).communicate()[0]
print(output)
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
# import pwclient

# # Conectar con el daemon de PipeWire
# client = pwclient.Client()

# # Obtener el volumen actual de la salida predeterminada
# volume_info = client.get_volume('default')
# current_volume = volume_info.values[0]

# # Establecer un nuevo volumen
# new_volume = current_volume - 0.1  # Reducir el volumen en un 10%
# client.set_volume('default', new_volume)