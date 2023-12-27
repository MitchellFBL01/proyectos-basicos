import tkinter as tk
from tkinter import ttk
from random import choice, randint
from PIL import Image, ImageTk

def juego(jugador):
    global puntosJugador
    global puntosPC
    posicion = randint(-1, 2)
    pc = ["piedra", "papel", "tijera"]
    eleccion = pc[posicion]
    print(eleccion)
    if jugador == eleccion:
        conclucion = "Empatado"
        anuncio.config(style= "black.TLabel")
    elif (jugador == "piedra" and eleccion == "tijera") or (jugador == "papel" and eleccion == "piedra") or (jugador == "tijera" and eleccion == "papel"):
        conclucion = "Ganado"
        anuncio.config(style= "win.TLabel")
    else:
        conclucion = "Perdido"
        anuncio.config(style= "lose.TLabel")
    
    if conclucion == "Ganado":
        puntosJugador += 1
    elif conclucion == "Perdido":
        puntosPC += 1
    puntosJugadorVar.set(f"Veces ganadas {puntosJugador}")
    puntosPCVar.set(f"Veces perdidad {puntosPC}")
    anuncioVar.set(f"Haz {conclucion}")

    return puntosJugador, puntosPC

puntosJugador = 0
puntosPC = 0
conclucion = "Empezado"

pantalla = tk.Tk()
pantalla.config(bg= "black")
# pantalla.geometry("320x240")
pantalla.config(padx= 10, pady= 10)

puntosJugadorVar = tk.StringVar()
puntosPCVar = tk.StringVar()
anuncioVar = tk.StringVar()
puntosJugadorVar.set(f"Veces ganadas {puntosJugador}")
puntosPCVar.set(f"Veces perdidad {puntosPC}")
anuncioVar.set(f"Haz {conclucion}")

stileB = ttk.Style()
stileB.configure("win.TLabel", background = "black", foreground = "green")
stileB.configure("black.TLabel", background = "black", foreground = "white")
stileB.configure("lose.TLabel", background = "black", foreground = "red")


tijera = Image.open("Piedra papel o tijera\T.png")
piedra = Image.open("Piedra papel o tijera\PI.png")
papel  = Image.open("Piedra papel o tijera\PA.png")

tijeraTk = ImageTk.PhotoImage(tijera.resize((50, 50)))
piedraTk = ImageTk.PhotoImage(piedra.resize((50, 50)))
papelTk  = ImageTk.PhotoImage(papel.resize((50, 50)))

titulo = ttk.Label(pantalla, text= "Elije entre las opciones", justify = "center", style= "black.TLabel")

titulo.grid(column= 1, row= 1, columnspan= 3, padx= 10, pady= 10)

tijeraB = ttk.Button(pantalla, image= tijeraTk, style= "white.TButton", command=lambda:juego("tijera"))
piedraB = ttk.Button(pantalla, image= piedraTk, style= "white.TButton", command=lambda:juego("piedra"))
papelB  = ttk.Button(pantalla, image= papelTk,  style= "white.TButton", command=lambda:juego("papel"))

tijeraB.grid(column = 1, row =2)
piedraB.grid(column = 2, row =2)
papelB.grid(column = 3, row =2)

contadorJugador = ttk.Label(pantalla, textvariable = puntosJugadorVar, justify = "center", style= "black.TLabel")
contadorPC = ttk.Label(pantalla, textvariable = puntosPCVar, justify = "center", style= "black.TLabel")

contadorJugador.grid(column= 1, row= 4)
contadorPC.grid(column= 3, row= 4)

instruccionesL = ttk.Label(pantalla, text= "- Tijera le gana a Papel\n- Papel le gana a Piedra\n- Piedra le gana a Tijera", justify = "center", style= "black.TLabel")

instruccionesL.grid(column= 1, row= 5, columnspan= 3)

anuncio = ttk.Label(pantalla, textvariable = anuncioVar, justify = "center", style= "black.TLabel")
anuncio.grid(column= 1, row= 3, columnspan= 3)


pantalla.mainloop()