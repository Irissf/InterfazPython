from tkinter import *

raiz = Tk()

miFrame = Frame(raiz, width=1200,height=600)
miFrame.config(bg="#CEE5D0",padx=20,pady=20)
miFrame.pack()

#le indicamos a la variable que va a contener caracteres
miNombre = StringVar()

nombreLabel = Label(miFrame, text="Nombre:",bg="#CEE5D0")
nombreLabel.grid(row=0,column=0,sticky="w",padx=10,pady=3)
#Este cuadro de texto estará conectado a la variable miNombre
cuadroTexto = Entry(miFrame, textvariable=miNombre)
cuadroTexto.grid(row=0, column=1,padx=10,pady=3)
cuadroTexto.config(fg="#5E454B")

apellidoLabel = Label(miFrame, text="Apellido:",bg="#CEE5D0")
apellidoLabel.grid(row=1,column=0, sticky="w",padx=10,pady=3)
cuadroTextoApellido = Entry(miFrame)
cuadroTextoApellido.grid(row=1, column=1,padx=10,pady=3)
cuadroTextoApellido.config(fg="#5E454B")

direLabel = Label(miFrame, text="Dirección:",bg="#CEE5D0")
direLabel.grid(row=2,column=0, sticky="w",padx=10,pady=3)
cuadroTextoDire = Entry(miFrame)
cuadroTextoDire.grid(row=2, column=1,padx=10,pady=3)
cuadroTextoDire.config(fg="#5E454B")

contraseña = Label(miFrame, text="Contraseña:",bg="#CEE5D0")
contraseña.grid(row=3,column=0, sticky="w",padx=10,pady=3)#los parámetros son row(fila) y column
cuadroTextoPass = Entry(miFrame)
cuadroTextoPass.grid(row=3, column=1,padx=10,pady=3)
#show, para que salga el caracter que especificamos, muy util en contraseñas
cuadroTextoPass.config(fg="#5E454B",show="•")

#=================================| TEXT |==============================
comentarios = Label(miFrame, text="Comentarios: ",bg="#CEE5D0")
comentarios.grid(row=4,column=0,padx=10,pady=3)
textoComentario = Text(miFrame, width=16,height=5)
textoComentario.grid(row=4,column=1,padx=10,pady=3)
#para el scrollbar, pertenece a texto comentario y en vista vertical
scrollVertical=Scrollbar(miFrame,command=textoComentario.yview)
#ahora lo colocamos, pero queda pequeñito, le añadimos sticky nsew(puntos cardinales)
#ya se ajusta
scrollVertical.grid(row=4,column=2,sticky="nsew")

#=================================| BUTTON |============================

def codigoBoton():
    miNombre.set("Juan")

#al pulsar el botón que llame a la funcion codigoBoton, y le asignará
# miNombre, el texto del Entry al que quedó asociada
botonEnvio = Button(miFrame,text="Enviar", command=codigoBoton)
botonEnvio.grid(row=5,column=1,padx=10,pady=3)
#al pulsar el boton que haga algo

raiz.mainloop()