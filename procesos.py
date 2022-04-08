from cryptography import fernet
from pathlib import Path
import os

def leerArchivo(archivo):
    #Chequeamos si en la carpeta esta creado el archivo y de no estarlo se crea un archivo vacio para evitar error
    archivo = r'texto.txt'
    objetoArchivo = Path(archivo)
    if not objetoArchivo.is_file():
        #abrimos el archivo en linea de append (agregar)
         with open(archivo, 'a') as file:
          file.write("")

    stream = open(archivo, "rt", encoding="utf-8")
    print(stream.read())

def escribirArchivo(linea, archivo):
    #abrimos el archivo en linea de append (agregar)
    with open(archivo, 'a') as file:
         file.write("\n"+linea)
    
def generar_clave():
    #generamos la llave unica que tambien utilizara para desencriptar
    archivo = r'key.key'
    objetoArchivo = Path(archivo)
    if not objetoArchivo.is_file():
        clave = fernet.Fernet.generate_key()
        
        with open("key.key", "wb") as key_file:
            key_file.write(clave)
        
def cargar_clave():
    return open("key.key", "rb").read()

def encriptar(archivo, clave):
    f = fernet.Fernet(clave)
    with open(archivo, "rb") as file:
        file_data = file.read()
    
    #Encriptamos los datos del archivo
    datos_encriptados = f.encrypt(file_data)
    
    with open(archivo, "wb") as file:
        file.write(datos_encriptados)

def desencriptar(archivo, clave):
 try:
    f = fernet.Fernet(clave)
    with open(archivo, "rb") as file:
        datos_encriptados = file.read()
  
    datos = f.decrypt(datos_encriptados)
    
    with open(archivo, "wb") as file:
        file.write(datos)        
        
    print("Se desencripto el archivo correctamente")
    #Si intentamos desencriptar un archivo que no existe nos va a arrojar el error - FileNotFoundError
    #Y si intentamos desencritar un archivo que no esta encriptado nos da un error no registrado - InvalidToken
    #Si se borra la key y se intenta desencriptar un archivo encriptado con otra key arroja error - InvalidToken
    #Por ese motivo capturo de esta forma todos estos errores
 except Exception:
        print("No se encuentra el archivo, El archivo no esta cifrado o La llave de cifrado fue cambiada")

        
def borrarArchivo(archivo):
 try:
     os.remove(archivo)
     print("Se borro el archivo correctamente")
 except OSError as e:
     print(f"Error:{ e.strerror}")
