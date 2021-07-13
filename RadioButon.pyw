from tkinter import Radiobutton
from tkinter import *

root = Tk()

#variable que almacenará valores int
varOpcion = IntVar()

def imprimir():
    if varOpcion.get()==1:
        etiqueta.config(text="masculino")
    else:
        etiqueta.config(text="femenino")
        

Label(root, text="Género:").pack()

#con el value pordemos rescatar el valor que fue pulsado
Radiobutton(root, text = "masculino", variable=varOpcion, value = 1, command=imprimir).pack()
Radiobutton(root, text = "femenino", variable=varOpcion, value = 2, command=imprimir).pack()

etiqueta = Label(root)
etiqueta.pack()

root.mainloop()