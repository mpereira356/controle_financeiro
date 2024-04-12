from tkinter import *
from tkinter import Tk, ttk
import os
print("Current working directory:", os.getcwd())

#importanto Pillow
from PIL import Image, ImageTk

# importando barra de progresso
from tkinter.ttk import Progressbar

# importando Matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

################# cores ###############
co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']



#criando janela

janela = Tk()
janela.title()
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style=ttk.Style(janela)
style.theme_use("clam")

# criando frames para divisao da tela
frameCima = Frame(janela, width=1043, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=361, bg=co1,pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1,padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=1,padx=10, sticky=NSEW)

#Trabalhando no frame Cima

#acessando a imagem
app_img = Image.open('logo.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Controle Financeiro", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4,)
app_logo.place(x=0, y=0)


# percentagem --------------------

def percentagem():
    l_nome = Label(frameMeio, text="Porcentagem da Receita gasta", height=1, anchor=NW, font=('Verdana 12' ), bg=co1, fg=co4)
    l_nome.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness=25)

    bar = Progressbar(frameMeio, length=180, style='black.Horizontal.TProgressbar')
    bar.place(x=10, y=35)
    bar['value'] = 50

    valor = 50

    l_percentagem = Label(frameMeio, text="{:,.2f}%".format(valor), height=1, anchor=NW, font=('Verdana 12' ), bg=co1, fg=co4)
    l_percentagem.place(x=200, y=35)


# funcao para grafico barra ---------------------

def grafico_bar():
    lista_categorias = ['Renda','Despesas', 'Saldo']
    lista_valores = [3000, 2000, 6236]

    # faça figura e atribua objetos de eixo
    
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    #ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)
    
    #create a list to collect the plt.patches data

    c = 0
    # set individual bar lables using above list
    
    for i in ax.patches:
        
        #get_x pulls left or right; get_height pushes up or down
        
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_categorias,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)


# funcao de resumo total
def resumo():
    valor = [500, 600, 420]

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    l_linha.place(x=309, y=52)
    l_sumario = Label(frameMeio, text="Total Renda Mensal      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg="#83a9e6")
    l_sumario.place(x=309, y=35)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[0]), anchor=NW, font=('Arial 17'), bg=co1, fg="#545454")
    l_sumario.place(x=309, y=70)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    l_linha.place(x=309, y=132)
    l_sumario = Label(frameMeio, text="Total Despesas Mensais      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg="#83a9e6")
    l_sumario.place(x=309, y=115)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[1]), anchor=NW, font=('Arial 17'), bg=co1, fg="#545454")
    l_sumario.place(x=309, y=150)
    
    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    l_linha.place(x=309, y=207)
    l_sumario = Label(frameMeio, text="Total Saldo da Caixa      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg="#83a9e6")
    l_sumario.place(x=309, y=190)
    l_sumario = Label(frameMeio, text="R$ {:,.2f}".format(valor[2]), anchor=NW, font=('Arial 17'), bg=co1, fg="#545454")
    l_sumario.place(x=309, y=220)


frame_gra_pie = Frame(frameMeio, width=580, height=250, bg=co2)
frame_gra_pie.place(x=440, y=5)

#funcao grafico pie
def grafico_pie():
    
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_gra_pie)
    canva_categoria.get_tk_widget().grid(row=0, column=0)


grafico_pie()
percentagem()
grafico_bar()
resumo()

janela.mainloop()
