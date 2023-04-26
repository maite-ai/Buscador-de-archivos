import os

dashed_line = "\n---------------------------------"

# Muestra los archivos existentes en la carpeta raíz
print("* Contenido actual de la carpeta *")
content_root_folder = os.listdir('Carpeta-ejercicio')
for folder in content_root_folder:
	print(folder)
print()

try: 
	# El usuario escribe el nombre
	user_select = input("Escribe el nombre de la carpeta o archivo\n (Debes respetar mayúsculas y minúsculas) \n")
	# Si es un archivo, lo abre y lo lee
	if os.path.isfile('Carpeta-ejercicio/'+user_select):
		try: 
			print(dashed_line)
			open('Carpeta-ejercicio/'+user_select)
			
		except FileNotFoundError:
			print("\t¡ALTO! \nLa carpeta NO EXISTE, o el nombre que ingresaste es INCORRECTO")
		else:
			print(f"--> LEYENDO {user_select}")
			print(dashed_line, "\n")
			open_file = open('Carpeta-ejercicio/'+user_select)
			for line in open_file:
				print(line)
	# Pero si es una carpeta, muestra lo que ésta contiene
	elif os.path.isdir('Carpeta-ejercicio/'+user_select):
		try:
			os.listdir('Carpeta-ejercicio/'+user_select)
			print(dashed_line)
			print("Contenido de la carpeta", user_select)
			files_in_folder = os.listdir('Carpeta-ejercicio/'+user_select)
		except FileNotFoundError:
			print("\t¡ALTO! \nEl archivo NO EXISTE, o el nombre que ingresaste es INCORRECTO")
		else:
			# Muestra el contenido del directorio
			for file in files_in_folder:
				print(file)
			print()
			# Se le pide al usuario que ingrese el nombre del archivo
			try:
				user_select_file = input("Escribe el nombre del archivo\n (¡no te olvides de la extensión!) \n")
				print(dashed_line)
				open('Carpeta-ejercicio/'+user_select+'/'+user_select_file)
			# Si no existe o el nombre fue incorrectamente escrito, captura el error.
			except FileNotFoundError:
				print("\t¡ALTO! \nLa carpeta NO EXISTE, o el nombre que ingresaste es INCORRECTO")
			# Si todo es correcto, lee el archivo
			else:
				print(f"--> LEYENDO {user_select_file}")
				print(dashed_line, "\n")
				open_file = open('Carpeta-ejercicio/'+user_select+'/'+user_select_file)
				for line in open_file:
					print(line)
	# Si no existe o el nombre fue incorrectamente escrito, captura el error.	
except FileNotFoundError:
	print("\t¡ALTO! \nEl archivo NO EXISTE, o el nombre que ingresaste es INCORRECTO")
finally: 
	print("\n-- Fin del programa --")