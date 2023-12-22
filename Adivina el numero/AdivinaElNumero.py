import tkinter as tk
from tkinter import ttk
from random import randint

def crar_numero():
    numeroONo = randint(1, 101)
    return numeroONo

def reinicio():
    global conteo
    numeroONo = randint(1, 101)
    reset = "Adivina el número entre 1 y 100"
    textwin.set(reset)
    conteo = 10
    cotadorVar.set(f"Intento número {conteo}")
    return numeroONo, conteo

numero = crar_numero()
conteo = 10
def intento(x):
    global conteo
    respuesta = None
    try:
        x = int(x)
    except TypeError: # Si ocurre un error de tipo
        respuesta = "¡¡ERROR!! \nDebes ingresar un número"
    if 1 < conteo <= 10:

        if isinstance(x, int):
            if x == numero:
                respuesta = f"Felicidades acertaste\nEs el numero {x}\nPreciona el boton de reinicio"
                resultado.config(style= "win.TLabel")
                entrynun.set(0)
            elif x > numero:
                respuesta = f"¡¡ERROR!! \nEl numero {x} es mayor"
            elif x < numero:
                respuesta = f"¡¡ERROR!! \nEl numero {x} es menor"
            textwin.set(respuesta)
    else:
        respuesta = "¡¡Perdiste!! \nAlcansaste el número maximo de intentos"
        resultado.config(style= "lose.TLabel")
        entrynun.set(0)
        textwin.set(respuesta)
        

    conteo -= 1
    cotadorVar.set(f"Intento número {conteo}")
    return conteo


wiyn = tk.Tk()
wiyn.config(bg= "black")
wiyn.geometry("320x240")
wiyn.config(padx= 10, pady= 10)

textwin = tk.StringVar()
textwin.set("Ingresa un nuemro del 1 al 100")
entrynun = tk.IntVar()
entrynun.set(0)
cotadorVar = tk.StringVar()
cotadorVar.set(f"Número de intestos restantes {conteo}")


myStyle = ttk.Style()
myStyle.configure("black.TFrame", background = "black")
myStyle.configure("black.TLabel", background = "black", foreground = "white")
myStyle.configure("win.TLabel", background = "black", foreground = "green")
myStyle.configure("lose.TLabel", background = "black", foreground = "red")
myStyle.configure("black.TButton", background = "black")

principal = ttk.Frame(wiyn, style = "black.TFrame")
principal.pack()

titulo = ttk.Label(principal, text= "Adivina el número entre 1 y 100", style= "black.TLabel")
titulo.grid(column= 0, row= 0, columnspan= 2)

numero1 = ttk.Entry(principal, textvariable = entrynun)
numero1.grid(column= 0, row= 1, columnspan= 2, padx= 5, pady= 5)

resultado = ttk.Label(principal, style= "black.TLabel", textvariable = textwin, justify = "center")
resultado.grid(column=0, row= 4, columnspan= 2, padx= 5, pady= 5)

adivina = ttk.Button(principal, text = "intentar", style= "black.TButton", command=lambda:intento(numero1.get()))
adivina.grid(column= 0, row= 3)
reinicio = ttk.Button(principal, text = "reiniciar", style= "black.TButton", command= reinicio)
reinicio.grid(column= 1, row= 3)

contador = ttk.Label(principal, style= "black.TLabel", textvariable = cotadorVar, justify = "center")
contador.grid(column=0, row= 5, columnspan= 2, padx= 5, pady= 5)


wiyn.mainloop()