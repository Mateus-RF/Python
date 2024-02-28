from tkinter import *
from tkinter import ttk



widow = Tk()
widow.title('Conversores')
widow.geometry('550x450')

aba_geral = ttk.Notebook(widow)
aba_geral.place(y=0, x=0, width=550, height=450)

aba1=Frame(aba_geral)
aba2=Frame(aba_geral)
aba3=Frame(aba_geral)


aba_geral.add(aba1,text='Graus')
def cparaf():
    f = Label(aba1, text='ºF')
    f.place(y=100, x=340)
    df = Label(aba1, text='ºC')
    df.place(y=40, x=340)
    graus =float(txt_graus.get())
    f = (graus * 9/5)+ 32
    R['text']= f
   
def cparak():
    f = Label(aba1, text='ºK')
    f.place(y=100, x=340)
    df = Label(aba1, text='ºC')
    df.place(y=40, x=340)
    graus =float(txt_graus.get())
    k = graus + 273.15
    R['text']= k

def fparak():
    f = Label(aba1, text='ºK')
    f.place(y=100, x=340)
    df = Label(aba1, text='ºF')
    df.place(y=40, x=340)
    graus =float(txt_graus.get())
    k = (graus - 32)* 5/9 + 273.15
    R['text']= k
    
def fparac():
    f = Label(aba1, text='ºC')
    f.place(y=100, x=340)
    df = Label(aba1, text='ºF')
    df.place(y=40, x=340)
    graus =float(txt_graus.get())
    c = (graus - 32)/1.8
    R['text']= c
    
def kparaf():
    f = Label(aba1, text='ºF')
    f.place(y=100, x=340)
    df = Label(aba1, text='ºK')
    df.place(y=40, x=340)
    graus =float(txt_graus.get())
    f = (graus - 273.15)* 9/5 + 32
    R['text']= f
    
def kparac():
    f = Label(aba1, text='ºC')
    f.place(y=100, x=340)
    df = Label(aba1, text='ºK')
    df.place(y=40, x=340)
    graus =float(txt_graus.get())
    c = graus - 273.15
    R['text']= c
 
   
quant_graus = Label(aba1, text='Quant. de Graus', padx=10, pady=40)
quant_graus.grid(row=1, column=0)
converted_graus = Label(aba1, text='Graus convertidos')
converted_graus.grid(row=2, column=0)

txt_graus = Entry(aba1)
txt_graus.grid(row = 1, column=1)
R = Label(aba1, text='', bg='#E0E0E0')
R.place(width=128, height=30 ,y=95, x=207)

botao0 = Button(aba1, text='ºC  ->  ºF', command=cparaf)
botao0.grid(row=3, column=0, padx=55,pady=80)
botao1 = Button(aba1, text='ºC  ->  ºK', command=cparak)
botao1.grid(row=4, column=0, padx=55, pady=0)
botao2 = Button(aba1, text='ºF  ->  ºK', command=fparak)
botao2.grid(row=3, column=1, padx=60, pady=80)
botao3 = Button(aba1, text='ºF  ->  ºC', command=fparac)
botao3.grid(row=4, column=1, padx=70, pady=0)
botao4 = Button(aba1, text='ºK  ->  ºF', command=kparaf)
botao4.grid(row=3, column=2, padx=70,pady=80)
botao5 = Button(aba1, text='ºK  ->  ºC', command=kparac)
botao5.grid(row=4, column=2, padx=70, pady=30)

aba_geral.add(aba2,text='Velocidade M.')
def vlcm():
    d = float(percusso.get())
    t = float(tempo.get())
    res['text'] = d/t
    
txt = Label(aba2, text='')
txt.grid(row=0, column=1, ipady=40)

des = Label(aba2, text='Metros')
des.grid(row=1, column=1)

traco = Label(aba2, text='___________________________________________')
traco.grid(row=2, column=0, padx=5)

tmp = Label(aba2, text='Segundos')
tmp.grid(row=3, column=1)

vlm = Button(aba2, text='Velocidade Média', command=vlcm)
vlm.place(y=95, x=345)

tempo = Entry(aba2, width=35)
tempo.grid(row=3, column=0, pady=10)

percusso = Entry(aba2, width=35)
percusso.grid(row=1, column=0, padx=10)

res = Label(aba2, text='',font=('calibri',12), bg='#E0E0E0')
res.place(width=175, height=30 ,y=125, x=345)

igual = Label(aba2, text='===', font=(15))
igual.grid(row=2, column=2)

aba_geral.add(aba3,text='E.Cinetica')
def Ec():
    k = float(K.get())
    ec = 1.5*1.38*k
    ec= str(ec)
    ec = ec+' x 10 ^-23'
    resi['text'] = ec

K = Entry(aba3, width=25)
K.grid(row=0, column=0, padx=210, pady=50)

botao = Button(aba3, width=20, text='E.C', command=Ec)
botao.grid(row=2, column=0, pady=20)

resi = Label(aba3, text='', font=('calibri',10), bg='#E0E0E0')
resi.place(width=180, height=35 ,y=100, x=195)

widow.mainloop()