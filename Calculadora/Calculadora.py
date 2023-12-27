import tkinter as tk
from tkinter import ttk
from math import sqrt

def calculo(operacion):
    try:
        resultado = str(format(eval(operacion),".2f"))
    except:
        resultado = "ERROR"
    pantalla.delete(0, tk.END)
    pantalla.insert(tk.END, resultado)

def rais(rais):
    b = format(sqrt(int(pantalla.get())),".5f") 
    pantalla.delete(0, tk.END)
    pantalla.insert(0, b)

def back_space():
    b = pantalla.get()
    pantalla.delete(0, tk.END)
    pantalla.insert(0, b[:-1])

calculadora = tk.Tk()
calculadora.title("Calculadora")
calculadora.config(padx= 10, pady= 10)

style = ttk.Style()
style.theme_use("clam")
style.configure('pantalla.TEntry', bg='#000000', anchor = "E")
style.configure("BotonesNumeros.TButton", font = "arial 22", relief = "flat", background = "#ffffff")
style.configure("OtrosBotones.TButton", font = "arial 22", relief = "flat", background = "#CDCDCD")
style.configure("mainFrame.TFrame", background= "#DBDBDB")


mainframe = ttk.Frame(calculadora,style= "mainFrame.TFrame")
mainframe.grid(column= 0, row= 0)
#--------------------------------- Pantalla ---------------------------

pantalla = ttk.Entry(mainframe, width = 14, style= 'pantalla.TEntry', justify= "right", font = ('Arial', 20))
pantalla.grid(column = 1, row = 0, columnspan= 4, padx= 5, pady= 5, sticky= 'we')

#--------------------------------- Teclas ---------------------------
#--------------------------------- Fila 1 ---------------------------
button7 = ttk.Button(mainframe, text= "7", width= 3, command=lambda:pantalla.insert(tk.END, "7"), style = "BotonesNumeros.TButton")
button8 = ttk.Button(mainframe, text= "8", width= 3, command=lambda:pantalla.insert(tk.END, "8"), style = "BotonesNumeros.TButton")
button9 = ttk.Button(mainframe, text= "9", width= 3, command=lambda:pantalla.insert(tk.END, "9"), style = "BotonesNumeros.TButton")
buttonDiv = ttk.Button(mainframe, text= u"\u00F7", width= 3, command=lambda:pantalla.insert(tk.END, "/"), style = "OtrosBotones.TButton")

button7.grid(column = 1, row= 2)
button8.grid(column = 2, row= 2)
button9.grid(column = 3, row= 2)
buttonDiv.grid(column = 4, row= 2)

#--------------------------------- Fila 2 ---------------------------
button4 = ttk.Button(mainframe, text= "4", width= 3, command=lambda:pantalla.insert(tk.END, "4"), style = "BotonesNumeros.TButton")
button5 = ttk.Button(mainframe, text= "5", width= 3, command=lambda:pantalla.insert(tk.END, "5"), style = "BotonesNumeros.TButton")
button6 = ttk.Button(mainframe, text= "6", width= 3, command=lambda:pantalla.insert(tk.END, "6"), style = "BotonesNumeros.TButton")
buttonMul = ttk.Button(mainframe, text= "*", width= 3, command=lambda:pantalla.insert(tk.END, "*"), style = "OtrosBotones.TButton")

button4.grid(column = 1, row= 3)
button5.grid(column = 2, row= 3)
button6.grid(column = 3, row= 3)
buttonMul.grid(column = 4, row= 3)

#--------------------------------- Fila 3 ---------------------------
button1 = ttk.Button(mainframe, text= "1", width= 3, command=lambda:pantalla.insert(tk.END, "1"), style = "BotonesNumeros.TButton")
button2 = ttk.Button(mainframe, text= "2", width= 3, command=lambda:pantalla.insert(tk.END, "2"), style = "BotonesNumeros.TButton")
button3 = ttk.Button(mainframe, text= "3", width= 3, command=lambda:pantalla.insert(tk.END, "3"), style = "BotonesNumeros.TButton")
buttonRes = ttk.Button(mainframe, text= "-", width= 3, command=lambda:pantalla.insert(tk.END, "-"), style = "OtrosBotones.TButton")

button1.grid(column = 1, row= 4)
button2.grid(column = 2, row= 4)
button3.grid(column = 3, row= 4)
buttonRes.grid(column = 4, row= 4)

#--------------------------------- Fila 4 ---------------------------
button0 = ttk.Button(mainframe, text= "0", width= 3, command=lambda:pantalla.insert(tk.END, "0"), style = "BotonesNumeros.TButton")
buttonComa = ttk.Button(mainframe, text= ",", width= 3, command=lambda:pantalla.insert(tk.END, "."), style = "OtrosBotones.TButton")
buttonIgual = ttk.Button(mainframe, text= "=", width= 3, command=lambda:calculo(pantalla.get()), style = "OtrosBotones.TButton")
buttonSum = ttk.Button(mainframe, text= "+", width= 3, command=lambda:pantalla.insert(tk.END, "+"), style = "OtrosBotones.TButton")

button0.grid(column = 1, row= 5)
buttonComa.grid(column = 2, row= 5)
buttonIgual.grid(column = 3, row= 5)
buttonSum.grid(column = 4, row= 5)

#--------------------------------- Fila 5 ---------------------------
buttonC = ttk.Button(mainframe, text= "DEL", width= 3, command= back_space, style = "OtrosBotones.TButton")
buttonDel = ttk.Button(mainframe, text= "C", width= 3, command=lambda:pantalla.delete(0, tk.END), style = "OtrosBotones.TButton")
buttonRais = ttk.Button(mainframe, text= "√", width= 3, command=lambda:rais(pantalla.get()), style = "OtrosBotones.TButton")
buttonEx = ttk.Button(mainframe, text= "^", width= 3, command=lambda:pantalla.insert(tk.END, "**"), style = "OtrosBotones.TButton")

buttonC.grid(column = 1, row= 1)
buttonDel.grid(column = 2, row= 1)
buttonRais.grid(column = 3, row= 1)
buttonEx.grid(column = 4, row= 1)

for child in mainframe.winfo_children():
    child.grid_configure(ipady = 10, padx = 1, pady = 1)

calculadora.mainloop()