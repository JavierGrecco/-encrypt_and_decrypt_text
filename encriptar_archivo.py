import procesos

opcion = 0

procesos.generar_clave()
clave = procesos.cargar_clave()

archivo = "texto.txt"



while opcion !=6:
 try:
    print("\nSeleciona una opción")
    print("\n1 - Leer Archivo\n2 - Agregar Texto al Archivo\n3 - Encriptar\n4 - Desencriptar\n5 - Borrar Archivo\n6 - Salir")
    opcion = int(input("\nIngresa una opción: "))
    
    if opcion == 1:
        print("El contenido del txt es: ")
        procesos.leerArchivo(archivo)
    elif opcion == 2:
      linea = input("Ingresa el texto que deseas agregar al archivo: ")
      procesos.escribirArchivo(linea, archivo)
    elif opcion == 3:
      procesos.encriptar(archivo, clave)
      print("Se encripto el archivo correctamente")
    elif opcion == 4:
      procesos.desencriptar(archivo, clave)
    elif opcion == 5:
      procesos.borrarArchivo(archivo)
    elif opcion == 6:
      print("Hasta pronto")
      print(exit())
    else:
        print("\nLa opción seleccionadda es incorrecta")
        
 except ValueError:
     print("Ingresar un numero")
