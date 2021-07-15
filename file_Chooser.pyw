from tkinter import *
from tkinter import filedialog

root = Tk()

def abreFichero():
    #importamos filedialog específicamente
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("imágenes","*.jpg"),
    ("Imagenes transparente","*.png"),("todos los archivos","*.*")))
    print(fichero)

Button (root, text="abrir fichero", command=abreFichero).pack()

root.mainloop()