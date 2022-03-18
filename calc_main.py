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
janela.geometry('270x292')
janela.config(bg=cor1)

# criando frames
frame_tela = Frame(janela, width=290, height=56, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_cientifica = Frame(janela, width=290, height=86)
frame_cientifica.grid(row=1, column=0)

frame_corpo = Frame(janela, width=290, height=340)
frame_corpo.grid(row=2, column=0)

# Funções
global todos_valores

todos_valores = ''
texto = StringVar()


# entrada de valores na tela
def inserir_valor(evento):
    global todos_valores

    todos_valores += str(evento)
    texto.set(todos_valores)


# calculo dos operadores
def calcular_valor():
    global todos_valores

    modulos = ['math.tan', 'math.sin', 'math.cos', 'math.sqrt', 'math.log',
               'math.log10', 'math.e', 'math.pow', 'math.pi']

    for i in modulos:
        if i == 'math.tan':
            todos_valores = todos_valores.replace('tan', i)

        if i == 'math.sin':
            todos_valores = todos_valores.replace('sin', i)

        if i == 'math.cos':
            todos_valores = todos_valores.replace('cos', i)

        if i == 'math.sqrt':
            todos_valores = todos_valores.replace('sqrt', i)

        if i == 'math.log':
            todos_valores = todos_valores.replace('log', i)

        if i == 'math.log10':
            todos_valores = todos_valores.replace('log10', i)

        if i == 'math.e':
            todos_valores = todos_valores.replace('e', i)

        if i == 'math.pow':
            todos_valores = todos_valores.replace('pow', i)

        if i == 'math.pi':
            todos_valores = todos_valores.replace('pi', i)

    resultado = str(eval(todos_valores))
    texto.set(resultado)

    todos_valores = ''


# limpando a tela
def limpar_tela():
    global todos_valores

    todos_valores = ''
    texto.set("")


# configurando o frame tela
label_tela = Label(frame_tela, textvariable=texto, width=17, height=2, padx=10, anchor='e', bd=0, justify=RIGHT,
                   font='Ivy 18', bg=cor3, fg=cor2)
label_tela.place(x=0, y=0)

# cofingurando o frame cientifica
# parte 1
b_tan = Button(frame_cientifica, command=lambda: inserir_valor('tan'), text='tan', width=6, height=1, relief=RAISED,
               overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_tan.place(x=0, y=0)

b_sin = Button(frame_cientifica, command=lambda: inserir_valor('sin'), text='sin', width=6, height=1, relief=RAISED,
               overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_sin.place(x=59, y=0)

b_cos = Button(frame_cientifica, command=lambda: inserir_valor('cos'), text='cos', width=6, height=1, relief=RAISED,
               overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_cos.place(x=118, y=0)

b_srqt = Button(frame_cientifica, command=lambda: inserir_valor('sqrt'), text='sqrt', width=6, height=1, relief=RAISED,
                overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_srqt.place(x=177, y=0)

# parte 2
b_log = Button(frame_cientifica, command=lambda: inserir_valor('log'), text='log', width=6, height=1, relief=RAISED,
               overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_log.place(x=0, y=29)

b_log10 = Button(frame_cientifica, command=lambda: inserir_valor('log10'), text='log10', width=4, height=1, relief=RAISED,
                 overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_log10.place(x=59, y=29)

b_e = Button(frame_cientifica, command=lambda: inserir_valor('e'), text='e', width=6, height=1, relief=RAISED,
             overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_e.place(x=118, y=29)

b_pow = Button(frame_cientifica, command=lambda: inserir_valor('pow'), text='pow', width=6, height=1, relief=RAISED,
               overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_pow.place(x=177, y=29)

# parte 3
b_pi = Button(frame_cientifica, command=lambda: inserir_valor('pi'), text='pi', width=6, height=1, relief=RAISED,
              overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_pi.place(x=0, y=58)

b_virgula = Button(frame_cientifica, command=lambda: inserir_valor(','), text=',', width=6, height=1, relief=RAISED,
                   overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_virgula.place(x=59, y=58)

b_pare = Button(frame_cientifica, command=lambda: inserir_valor('('), text='(', width=6, height=1, relief=RAISED,
                overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_pare.place(x=118, y=58)

b_pare2 = Button(frame_cientifica, command=lambda: inserir_valor(')'), text=')', width=6, height=1, relief=RAISED,
                 overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_pare2.place(x=177, y=58)

# frame corpo
# parte 1
b_resu = Button(frame_corpo, command=limpar_tela, text='C', width=11, height=1, relief=RAISED,
                overrelief=RIDGE, font='Ivy 10 bold', bg=cor4, fg=cor2)
b_resu.place(x=0, y=0)

b_porce = Button(frame_corpo, command=lambda: inserir_valor('%'), text='%', width=6, height=1, relief=RAISED,
                 overrelief=RIDGE, font='Ivy 10 bold', bg=cor4, fg=cor2)
b_porce.place(x=118, y=0)

b_barra = Button(frame_corpo, command=lambda: inserir_valor('/'), text='/', width=6, height=1, relief=RAISED,
                 overrelief=RIDGE, font='Ivy 10 bold', bg=cor4, fg=cor2)
b_barra.place(x=177, y=0)

# parte 2
b_sete = Button(frame_corpo, command=lambda: inserir_valor('7'), text='7', width=6, height=1, relief=RAISED,
                overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_sete.place(x=0, y=29)

b_oito = Button(frame_corpo, command=lambda: inserir_valor('8'), text='8', width=6, height=1, relief=RAISED,
                overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_oito.place(x=59, y=29)

b_nove = Button(frame_corpo, command=lambda: inserir_valor('9'), text='9', width=6, height=1, relief=RAISED,
                overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_nove.place(x=118, y=29)

b_mult = Button(frame_corpo, command=lambda: inserir_valor('*'), text='*', width=6, height=1, relief=RAISED,
                overrelief=RIDGE, font='Ivy 10 bold', bg=cor4, fg=cor2)
b_mult.place(x=177, y=29)

# parte 3
b_quatro = Button(frame_corpo, command=lambda: inserir_valor('4'), text='4', width=6, height=1, relief=RAISED,
                  overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_quatro.place(x=0, y=59)

b_cinco = Button(frame_corpo, command=lambda: inserir_valor('5'), text='5', width=6, height=1, relief=RAISED,
                 overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_cinco.place(x=59, y=59)

b_seis = Button(frame_corpo, command=lambda: inserir_valor('6'), text='6', width=6, height=1, relief=RAISED,
                overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_seis.place(x=118, y=59)

b_menos = Button(frame_corpo, command=lambda: inserir_valor('-'), text='-', width=6, height=1, relief=RAISED,
                 overrelief=RIDGE, font='Ivy 10 bold', bg=cor4, fg=cor2)
b_menos.place(x=177, y=59)

# parte 4
b_um = Button(frame_corpo, command=lambda: inserir_valor('1'), text='1', width=6, height=1, relief=RAISED,
              overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_um.place(x=0, y=89)

b_dois = Button(frame_corpo, command=lambda: inserir_valor('2'), text='2', width=6, height=1, relief=RAISED,
                overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_dois.place(x=59, y=89)

b_tres = Button(frame_corpo, command=lambda: inserir_valor('3'), text='3', width=6, height=1, relief=RAISED,
                overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_tres.place(x=118, y=89)

b_mais = Button(frame_corpo, command=lambda: inserir_valor('+'), text='+', width=6, height=1, relief=RAISED,
                overrelief=RIDGE, font='Ivy 10 bold', bg=cor4, fg=cor2)
b_mais.place(x=177, y=89)

# parte 8
b_zero = Button(frame_corpo, command=lambda: inserir_valor('0'), text='0', width=11, height=1, relief=RAISED,
                overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_zero.place(x=0, y=119)

b_ponto = Button(frame_corpo, command=lambda: inserir_valor('.'), text='.', width=6, height=1, relief=RAISED,
                 overrelief=RIDGE, font='Ivy 10 bold', bg=cor1, fg=cor2)
b_ponto.place(x=118, y=119)

b_igual = Button(frame_corpo, command=calcular_valor, text='=', width=6, height=1, relief=RAISED,
                 overrelief=RIDGE, font='Ivy 10 bold', bg=cor4, fg=cor2)
b_igual.place(x=177, y=119)

janela.mainloop()
