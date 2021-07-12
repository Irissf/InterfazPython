from tkinter import *

root=Tk()
miFrame = Frame(root, width=500, height=400)
miFrame.pack()

#======================= LABEL ====================================
#creamos una label
miLabel = Label(miFrame, text="Cosas de la vida", fg="red",font=("Comic Sans MS",18))
#en vez de pack, usamos place, nos permite unas coordenadas
miLabel.place(x=100, y=100)
#si no vamos a tocar la label podemos atajar
# Label(miFrame, text="Cosas de la vida").place(x=100, y=100)

#======================= LABEL CON IMAGENES==========================
#permite gif y png, de querer otro habrá que bajar otras librerias
miImagen = PhotoImage(file = "recursos/imagen.gif", width= 200, height=100)

miLabelImagen = Label(miFrame, image=miImagen)
miLabelImagen.place(x=200, y=200)

root.mainloop()