
import os
import requests

class FileDownloader:
    def __init__(self, directorio_destino):
        self.directorio = directorio_destino

    def crear_directorio(self):
        if not os.path.exists(self.directorio):
            os.makedirs(self.directorio)
            print(f"Directorio {self.directorio} creado correctamente")
        else:
            print(f"Directorio {self.directorio} ya existe")

    def descargar_archivo(self, url):

        nombre_archivo = url.split("/")[-1]
        path = os.path.join(self.directorio, nombre_archivo)

        try:
            if not os.path.exists(path):
                response = requests.get(url)

                if response.status_code == 200:
                    with open(path, 'wb') as file:
                        file.write(response.content)
                    print(f"Archivo {nombre_archivo} descargado correctamente")
                else:
                    print(f"Error: {response.status_code}")
            else:
                print(f"El archivo {nombre_archivo} ya existe")
        except Exception as e:
            print(f"Error: {e}")
        
    def filtrar_descargar_archivos(self, urls, tipos_archivo=["all"]):
        if tipos_archivo == ["all"]:
            for url in urls:
                self.descargar_archivo(url)
        else:
            for url in urls:
                if (url.endswith(f".{tipo}") for tipo in tipos_archivo):
                    self.descargar_archivo(url)