from tkinter import *
from typing import Sized

#EJEMPLO NO COMPLETO PARA EXPLICAR ALGUNOS TËRMINOS
#lo que se quiere hacer a mayores, ya se puede hacer facilmente

raiz = Tk()

ancho = 4
alto = 2

miFrame = Frame()
miFrame.config(padx=10,pady=10)
miFrame.pack()

operacion = ""
resultado = 0

#--------------pantalla-------------------------------------------------

numeroPantalla = StringVar()

#la pantalla donde se ve la operación, con colspan(columnspan)
#decimos que: ocupe 4 columnas en vez de 1
pantalla = Entry(miFrame , textvariable = numeroPantalla)
pantalla.grid(row=1,column=1,columnspan=4,pady=10)
pantalla.config(bg="black",fg="green",justify="right",font=20)

#--------------pulsaciones teclado--------------------------------------

def numeroPulsado(num):
    global operacion
    global resultado

    if (operacion!=""):
        #si es diferente de cadena vacia sabemos que pulsó un comando de opeación
        numeroPantalla.set(num)
        operacion = ""
    else:   
        numeroPantalla.set(numeroPantalla.get() + num)

#----------------------Operaciones--------------------------------------
def suma(num):
    #trabajamos con la variable global operacion
    global operacion
    global resultado

    resultado += int(num)
    operacion = "suma"
    numeroPantalla.set(resultado)

def elResultado():
    global resultado

    numeroPantalla.set(resultado+int(numeroPantalla.get()))


#--------------botones fila 1-------------------------------------------
button7 = Button(miFrame,text="7",width=ancho,height=alto, command=lambda:numeroPulsado("7"))
button7.grid(row=2,column=1)
button8 = Button(miFrame,text="8",width=ancho,height=alto, command=lambda:numeroPulsado("8")) 
button8.grid(row=2,column=2)
button9 = Button(miFrame,text="9",width=ancho,height=alto, command=lambda:numeroPulsado("9")) 
button9.grid(row=2,column=3)
buttonDiv = Button(miFrame,text="/",width=ancho,height=alto) 
buttonDiv.grid(row=2,column=4)

#---------------botones fila 2-------------------------------------------
button4 = Button(miFrame,text="4",width=ancho,height=alto, command=lambda:numeroPulsado("4"))
button4.grid(row=3,column=1)
button5 = Button(miFrame,text="5",width=ancho,height=alto, command=lambda:numeroPulsado("5")) 
button5.grid(row=3,column=2)
button6 = Button(miFrame,text="6",width=ancho,height=alto, command=lambda:numeroPulsado("6")) 
button6.grid(row=3,column=3)
buttonMul = Button(miFrame,text="X",width=ancho,height=alto) 
buttonMul.grid(row=3,column=4)

#----------------botones fila 3------------------------------------------
button1 = Button(miFrame,text="1",width=ancho,height=alto, command=lambda:numeroPulsado("1"))
button1.grid(row=4,column=1)
button2 = Button(miFrame,text="2",width=ancho,height=alto, command=lambda:numeroPulsado("2")) 
button2.grid(row=4,column=2)
button3 = Button(miFrame,text="3",width=ancho,height=alto, command=lambda:numeroPulsado("3")) 
button3.grid(row=4,column=3)
buttonRes = Button(miFrame,text="-",width=ancho,height=alto) 
buttonRes.grid(row=4,column=4)

#-----------------botones fila 4----------------------------------------
buttonComa = Button(miFrame,text=",",width=ancho,height=alto, command=lambda:numeroPulsado("."))
buttonComa.grid(row=5,column=1)
button0 = Button(miFrame,text="0",width=ancho,height=alto, command=lambda:numeroPulsado("0")) 
button0.grid(row=5,column=2)
buttonIgual = Button(miFrame,text="=",width=ancho,height=alto, command= lambda:elResultado()) 
buttonIgual.grid(row=5,column=3)
buttonSum = Button(miFrame,text="+",width=ancho,height=alto, command=lambda:suma(numeroPantalla.get())) 
buttonSum.grid(row=5,column=4)


raiz.mainloop()
