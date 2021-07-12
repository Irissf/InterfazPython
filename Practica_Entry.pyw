from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200,height=600)
miFrame.config(bg="#CEE5D0")
miFrame.pack()

#miniformulario ejemplo, usaremos grid en vez de pack() o place()
#la propiedad sticky nos permite mover la alineación, n,s,w,e de los puntos cardinales
#podemos añadir, padding(pady, padx..), margin etc
nombreLabel = Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="w",padx=10,pady=3)#los parámetros son row(fila) y column
cuadroTexto = Entry(miFrame)
cuadroTexto.grid(row=0, column=1,padx=10,pady=3)
cuadroTexto.config(fg="#5E454B")

apellidoLabel = Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1,column=0, sticky="w",padx=10,pady=3)#los parámetros son row(fila) y column
cuadroTextoApellido = Entry(miFrame)
cuadroTextoApellido.grid(row=1, column=1,padx=10,pady=3)
cuadroTextoApellido.config(fg="#5E454B")

direLabel = Label(miFrame, text="Dirección:")
direLabel.grid(row=2,column=0, sticky="w",padx=10,pady=3)#los parámetros son row(fila) y column
cuadroTextoDire = Entry(miFrame)
cuadroTextoDire.grid(row=2, column=1,padx=10,pady=3)
cuadroTextoDire.config(fg="#5E454B")

contraseña = Label(miFrame, text="Contraseña:")
contraseña.grid(row=3,column=0, sticky="w",padx=10,pady=3)#los parámetros son row(fila) y column
cuadroTextoPass = Entry(miFrame)
cuadroTextoPass.grid(row=3, column=1,padx=10,pady=3)
#show, para que salga el caracter que especificamos, muy util en contraseñas
cuadroTextoPass.config(fg="#5E454B",show="•")

raiz.mainloop()