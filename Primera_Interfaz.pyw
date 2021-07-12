from tkinter import *

#raiz -> es la ventana
raiz = Tk()
                
#========================= VENTANA =========================
#modificar características de la ventana
raiz.title("Mi interfaz")
#el tamaño de la venta, pero es mejor darle el tamaño al frame
#raiz.geometry("600x600")
#no se puede redimensionar en ninguna dirección, 0 o False, 1 o True
#raiz.resizable(1,1)
#cambiar icono
raiz.iconbitmap("recursos/icono.ico")
#cambiar color de fondo
raiz.config(bg="#C3B4A5")

#======================= FRAME ================================
miFrame = Frame()
miFrame.config(bg = "#9C8D7F")
#tamaño del frame
miFrame.config(width="500",height="500")

#lo metemos en raiz, el side, es para donde se ancla, arriba, abajos,
#igual que los puntos cardinales, norte sur...
#fill-> sería para expander el frame al crecer la ventana
miFrame.pack(side="left",anchor="n")
#un borde para el frame
miFrame.config(relief="groove", bd=3)
#cambiar cursor
miFrame.config(cursor="hand2")


#Siempre al final
raiz.mainloop() #mainloop es como un bucle infinito, ya que la 
#ventana debe estar a la escucha de eventos