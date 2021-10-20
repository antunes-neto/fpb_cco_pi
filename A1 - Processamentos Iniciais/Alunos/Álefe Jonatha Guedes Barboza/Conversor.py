#Álefe Jonatha Guedes Barboza - CCO P8 - Manhã
#
#********Guia para Executar************
#
# (Opção 1) Abrir o arquivo: conversor.exe (Para NÃO instalar os modulos e executar o programa, mas o windows defender não vai reconhecer);
# (Opção 2) Abrir o link https://replit.com/@AlefeGuedes/DrabBusyCell#main.py	
# (Opção 3) Instalar os modulos e rodar o código no VSCode;
# 	    pip install pillow
#           pip install opencv-python


from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showerror, showinfo
from PIL import Image, ImageChops
import cv2
import numpy as np
import os.path

# Criação Tela principal
menu_inicial = Tk()
menu_inicial.title("Conversor")
# Dimensões
menu_inicial.geometry('370x310+450+150')
menu_inicial.minsize(370, 310)
menu_inicial.maxsize(370, 310)

# variaveis
endereco_imagem = StringVar()
endereco_destino = StringVar()
valor_vermelho = IntVar()
valor_verde = IntVar()
valor_azul = IntVar()
valor_cinza = IntVar()
valor_negativo = IntVar()


# Funções
def load_file():
    fname = askopenfilename(filetypes=(("All files", ("*.jpg", "*.jpeg", "*.png")), ("JPG files", "*.jpg"), ("JPEG files", "*.jpeg"), ("PNG files", "*.png")))
    if fname:
        try:
            endereco_imagem.set(fname)
        except:  # enviar mensagem
            showerror("Erro", "Arquivo inválido" % fname)


def save_file():
    fname = askdirectory()
    if fname:
        try:
            endereco_destino.set(fname)
        except:  # enviar mensagem de erro
            showerror("Erro", "Diretório inválido")


def novo_nome(destino, imagem, texto):
    endereco_split = os.path.split(imagem)
    nome_arquivo = os.path.splitext(endereco_split[1])
    novo_nome_arquivo = nome_arquivo[0] + texto + nome_arquivo[1]
    return os.path.join(destino, novo_nome_arquivo)


def cmd_converter(imagem, destino):
    if imagem == "" or destino == "":
        showerror("Falha ao converter", "Selecione os campos corretamente")

    elif (valor_azul.get() != 1 and valor_verde.get() != 1 and valor_vermelho.get()
          != 1 and valor_cinza.get() != 1 and valor_negativo.get() != 1):
        showerror("Erro", "Nenhum valor foi selecionado")

    else:
        img_original = Image.open(imagem)
        img_originalRGB = cv2.imread(imagem)

        azul, verde, vermelho = cv2.split(img_originalRGB)
        zeros = np.zeros(azul.shape, np.uint8)

        if valor_vermelho.get() == 1:
            vermelhoBGR = cv2.merge((zeros, zeros, vermelho))
            cv2.imwrite(novo_nome(destino, imagem, 'EscRed'), vermelhoBGR)
        if valor_verde.get() == 1:
            verdeBGR = cv2.merge((zeros, verde, zeros))
            cv2.imwrite(novo_nome(destino, imagem, 'EscGreen'), verdeBGR)
        if valor_azul.get() == 1:
            azulBGR = cv2.merge((azul, zeros, zeros))
            cv2.imwrite(novo_nome(destino, imagem, 'EscBlue'), azulBGR)
        if valor_cinza.get() == 1:
            img_escala_de_cinza = img_original.convert('L')
            img_escala_de_cinza.save(novo_nome(destino, imagem, 'EscGray'))
        if valor_negativo.get() == 1:
            img_scala_negativa = ImageChops.invert(img_original)
            img_scala_negativa.save(novo_nome(destino, imagem, 'EscNegative'))

        showinfo("Sucesso", "A imagem foi convertida com sucesso")


# widgets
label_imagem_endereco = Label(menu_inicial,
                              text='Selecione a imagem',
                              pady=15,
                              textvariable=endereco_imagem
                              ).grid(columnspan=2, sticky='we')

label_imagem = Label(menu_inicial,
                     text='Procurar imagem',
                     pady=15,
                     width=20,
                     ).grid(row=1, column=0)

btn_imagem = Button(menu_inicial,
                    text="Procurar",
                    width=20,
                    command=load_file).grid(row=1, column=1)

label_destino_endereco = Label(menu_inicial,
                               text='Selecione a imagem',
                               pady=15,
                               textvariable=endereco_destino
                               ).grid(columnspan=2, sticky='we')

label_destino = Label(menu_inicial,
                      text='Selecionar destino',
                      pady=15,
                      width=20,
                      ).grid(row=3, column=0)

btn_destino = Button(menu_inicial,
                     text="Selecionar",
                     width=20,
                     command=save_file).grid(row=3, column=1)

check_vermeho = Checkbutton(menu_inicial,
                            text="Filtro vermelho.",
                            variable=valor_vermelho,
                            ).grid(row=4, column=0, sticky='w')

check_verde = Checkbutton(menu_inicial,
                          text="Filtro verde.",
                          variable=valor_verde,
                          ).grid(row=5, column=0, sticky='w')

check_azul = Checkbutton(menu_inicial,
                         text="Filtro azul.",
                         variable=valor_azul,
                         ).grid(row=6, column=0, sticky='w')

check_cinza = Checkbutton(menu_inicial,
                          text="Escala Cinza.",
                          variable=valor_cinza,
                          ).grid(row=4, column=1, sticky='w')

check_negativo = Checkbutton(menu_inicial,
                             text="Escala negativa.",
                             variable=valor_negativo,
                             ).grid(row=5, column=1, sticky='w')

btn_converter = Button(menu_inicial,
                       text="Converter",
                       width=10,
                       pady=5,
                       bg="green",
                       fg="white",
                       command=lambda: cmd_converter(endereco_imagem.get(), endereco_destino.get())).grid(columnspan=2)

# Iniciar menu_inicial
menu_inicial.mainloop()
