import ply.lex as lex
from tkinter import *
import AnalizadorLexico as AL

ventana = Tk()
ventana.title("Analizador Lexico")
ventana.geometry("700x600")
ventana.config(bg='blue')
ventana.resizable(False,False)

entrada = StringVar()

f = Frame()
f.pack()
f.config(width="680", height="580", bg='#856ff8')
f.place(x=10,y=10)

l1 = Label(f,width="20", height="1", bg='#856ff8', fg='black',font=("Times New Roman", 28),text="ANALIZADOR LEXICO")
l1.place(x=80, y=1)

l2 = Label(f,width="20", height="1",text= "Cadena(s) a analizar",font=("Times New Roman", 12),bg='#856ff8')
l2.grid(sticky="w")
l2.place(x=20, y=70)

c1 = Text(f,width="56",height="7", font=("Times New Roman", 12))
c1.place(x=20, y=100)
scrollc1 = Scrollbar(f, command=c1.yview)
scrollc1.grid(sticky="nsew")
scrollc1.place(in_=c1, relx=1, relheight=1, bordermode= "outside")
c1.config(yscrollcommand=scrollc1.set)

l3 = Label(f,width="10", height="1",text= "Resultados:",font=("Times New Roman", 12),bg='#856ff8')
l3.grid(sticky="e")
l3.place(x=20, y=270)

c2 = Text(f,width="56",height="9", font=("Times New Roman", 12))
c2.place(x=20, y=300)
scrollc2 = Scrollbar(f, command=c1.yview)
scrollc2.grid(sticky="nsew")
scrollc2.place(in_=c2, relx=1, relheight=1, bordermode= "outside")
c2.config(yscrollcommand=scrollc2.set)

def analizar():
    entrada = c1.get("1.0","end-1c")
    print(entrada)
    c2.delete("1.0","end")
    a=[]
    a=AL.analisis(entrada)
    print(a)
    for x in a:
        print(x)
        c2.insert(INSERT, x)
        c2.insert(INSERT, "\n")

bAn = Button(f,text="Analizar",font=("Times New Roman", 12),bg='blue',fg='white',command=analizar)
bAn.place(x=280, y=530, width=100, height=30)


ventana.mainloop()
