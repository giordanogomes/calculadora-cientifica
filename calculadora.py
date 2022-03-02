from tkinter import *
from tkinter import ttk
import math

# cores
cor1 = "#363434"  # preta
cor2 = "#feffff"  # branca
cor3 = "#37474F"  # cinza
cor4 = "#424345"  # laranja

# criando janela principal
janela = Tk()
janela.title('Calculadora')
janela.geometry('260x294')
janela.config(bg=cor1)

# criando frames
frame_tela = Frame(janela, width=290, height=56, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_cientifica = Frame(janela, width=290, height=86)
frame_cientifica.grid(row=1, column=0)

frame_corpo = Frame(janela, width=290, height=340)
frame_corpo.grid(row=2, column=0)


janela.mainloop()
