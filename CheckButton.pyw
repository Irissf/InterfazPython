import tkinter


from tkinter import *

root = Tk()
root.title("Ejemplo")

#Para evaluar los check
playa=IntVar()
montanha=IntVar()
ciudad=IntVar()

def opcionesViaje():
    opcionEscogida = ""
    if (playa.get() == 1):
        opcionEscogida += "Playa"
        
    if (montanha.get() == 1):
        opcionEscogida += "Montaña"
        
    if (ciudad.get() == 1):
        opcionEscogida += "Ciudad"
    #Accedemos al label donde pondremos el resultado de lo seleccionado   
    textoFinal.config(text=opcionEscogida)

#--------------Parte gráfica---------------------------------

foto = PhotoImage(file="recursos\prueba.png")
Label(root,image=foto).pack()

frame = Frame(root)
frame.pack()

Label(frame, text="Selecciona un destino", width=50).pack()

#checkbutton para varios seleccionados 
Checkbutton(frame, text="playa", variable=playa, onvalue=1, offvalue=0,command=opcionesViaje).pack()
Checkbutton(frame, text="montaña", variable=montanha, onvalue= 1, offvalue=0,command=opcionesViaje).pack()
#variable->donde mete el valor, onvalue-> valor activado
#offvalue->valor desactivado, command->función a la que llama
Checkbutton(frame, text="ciudad", variable=ciudad, onvalue = 1, offvalue=0, command=opcionesViaje).pack()

#para que muestre las opciones escogidas
textoFinal = Label(frame)
textoFinal.pack()

root.mainloop()
#------------------------------------------------------------

