from tkinter import *
from tkinter import messagebox

root = Tk()

#-----------------------Message Box------------------------------

def infoAdicional():
    #importante importar messagebox especificamente
    messagebox.showinfo("titulo","texto que queremos mostrar")
    valor = messagebox.askquestion("Salir","¿Quieres salir?")
    if valor == "yes":
        root.destroy()
        

#---------------------------------Menú---------------------------
barraMenu = Menu(root)
#le ponemos un menú a root
root.config(menu=barraMenu, width=300, height=300)

#Elementos del menú, con tearoff, quitamos esa barra que aparece cuando no hay nada
archivoMenu=Menu(barraMenu, tearoff=0)
#subelementos de archivo
archivoMenu.add_command(label="Nuevo")
archivoMenu.add_command(label="Abrir")
archivoMenu.add_command(label="Guardar")
#colocar una barra
archivoMenu.add_separator()
archivoMenu.add_command(label="Salir", command=infoAdicional)
#ventana emergente


archivoEdición=Menu(barraMenu)
archivoHerramientas=Menu(barraMenu)
archivoAyuda=Menu(barraMenu)

#El elemento archivoMenú, que aparezca con el nombre de Archivo en la barra
barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edición",menu=archivoEdición)
barraMenu.add_cascade(label="Herramientas",menu=archivoHerramientas)
barraMenu.add_cascade(label="Ayuda",menu=archivoAyuda)



root.mainloop()