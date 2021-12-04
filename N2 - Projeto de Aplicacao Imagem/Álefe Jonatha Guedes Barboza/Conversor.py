from tkinter import *
from tkinter.filedialog import askopenfilename, askdirectory
from tkinter.messagebox import showerror, showinfo
import numpy
from PIL import Image, ImageChops, ImageTk, ImageEnhance
import cv2
import os.path

root = Tk()
root.title('Conversor')
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))



class ScaleValue:
    def __init__(self):
        self.value0 = 0
        self.value1 = 0
        self.value2 = 0
        self.valuecontraste = 0
        self.valuebrilho = 0
        self.valuenitidez = 0
        self.imagem_original = 0
        self.imagem_salvar = 0
        self.imagem_alterada = 0
        self.imagem_alteradaB = 0


# VARIÁVEIS
endereco_imagem = StringVar()
endereco_destino = StringVar()
valor_cinza = IntVar()
valor_negativo = IntVar()

global scale
scale = ScaleValue()


def sair():
    root.destroy()


def abrir_imagem():
    fname = askopenfilename(filetypes=(
        ("All files", ("*.jpg", "*.jpeg", "*.png")), ("JPG files", "*.jpg"), ("JPEG files", "*.jpeg"),
        ("PNG files", "*.png")))
    if fname:
        try:
            endereco_imagem.set(fname)
            img = Image.open(endereco_imagem.get())
            new_image = numpy.array(img)

            scale.imagem_original = Image.fromarray(new_image)
            scale.imagem_alterada = escalonamento(scale.imagem_original)
            scale.imagem_alteradaB = scale.imagem_alterada


            # newFrame(image_alterada)
            newFrame(scale.imagem_alterada)
        except:
            showerror("Erro", "Arquivo inválido" % fname)


def novo_nome(destino, imagem, texto):
    endereco_split = os.path.split(imagem)
    nome_arquivo = os.path.splitext(endereco_split[1])
    novo_nome_arquivo = nome_arquivo[0] + texto + nome_arquivo[1]
    return os.path.join(destino, novo_nome_arquivo)


def salvar():
    if endereco_imagem.get() != "":
        fname = askdirectory()
        if fname != '':
            # img = Image.open(endereco_imagem.get())
            try:
                endereco_destino.set(fname)
                if valor_negativo.get() == 1:
                    name = 'negativa'
                    scale.imagem_salvar = ImageChops.invert(scale.imagem_original)
                elif valor_cinza.get() == 1:
                    name = 'cinza'
                    scale.imagem_salvar = scale.imagem_original.convert('L')
                else:
                    name = 'rgb'
                    scale.imagem_salvar = calc_rgb(scale.imagem_original, scale.value0, scale.value1, scale.value2)
                    scale.imagem_salvar = contrast(scale.imagem_salvar)
                    scale.imagem_salvar = brilho(scale.imagem_salvar)
                    scale.imagem_salvar = nitidez(scale.imagem_salvar)

                scale.imagem_salvar.save(novo_nome(endereco_destino.get(), endereco_imagem.get(), name))
                showinfo("Sucesso", "A imagem foi convertida com sucesso")
            except:
                showerror("Conversor", "Erro ao salvar", )
    else:
        showerror("Conversor", "Erro", )


def escalonamento(img):
    numpy_image = numpy.array(img)
    obj_img = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
    altura, largura, canais_de_cor = obj_img.shape

    if altura != largura:
        if altura > largura and altura > 300:
            x = 300
            wpercent = (x / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((x, hsize), Image.ANTIALIAS)
        elif largura > altura and largura > 700:
            x = 700
            wpercent = (x / float(img.size[0]))
            hsize = int((float(img.size[1]) * float(wpercent)))
            img = img.resize((x, hsize), Image.ANTIALIAS)
    elif altura > 300:
        x = 300
        wpercent = (x / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((x, hsize), Image.ANTIALIAS)
    return img


def newFrame(image_frame):
    try:
        photo = ImageTk.PhotoImage(image_frame)
        label_imagem.config(image=photo)
        label_imagem.image = photo
    except:
        showerror("Conversor", "ERRO")


def calc_rgb(obj_img2, azulScale, verdeScale, vermelhoScale):
    # Converter imagem para CV2 (RGB para BGR)
    numpy_image = numpy.array(obj_img2)
    obj_img = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
    altura, largura, canais_de_cor = obj_img.shape

    for y in range(0, altura):
        for x in range(0, largura):
            # BGR = canal 0 = azul // canal 1 = verde // canal 2 = vermelho
            # y altura // x largura
            # item: Pega o valor na posição selecinada // imtemset: Atribuir valor na posição selecionada
            azul = obj_img.item(y, x, 0)
            verde = obj_img.item(y, x, 1)
            vermelho = obj_img.item(y, x, 2)

            azulnew = int(azul) + int(azulScale)
            verdenew = int(verde) + int(verdeScale)
            vermelhonew = int(vermelho) + int(vermelhoScale)

            # Verificando se as entradas são maiores que 0 e menores que 255
            # AZUL
            if 0 <= azulnew <= 255:
                obj_img.itemset((y, x, 0), azulnew)
            elif azulnew >= 255:
                obj_img.itemset((y, x, 0), 255)
            elif azulnew <= 0:
                obj_img.itemset((y, x, 0), 0)
            # VERDE
            if 0 <= verdenew <= 255:
                obj_img.itemset((y, x, 1), verdenew)
            elif verdenew >= 255:
                obj_img.itemset((y, x, 1), 255)
            elif verdenew <= 0:
                obj_img.itemset((y, x, 1), 0)
            # VERMELHO
            if 0 <= vermelhonew <= 255:
                obj_img.itemset((y, x, 2), vermelhonew)
            elif vermelhonew >= 255:
                obj_img.itemset((y, x, 2), 255)
            elif vermelhonew <= 0:
                obj_img.itemset((y, x, 2), 0)

    valor_negativo.set(0)
    valor_cinza.set(0)
    # Converter imagem para Pil (BGR para RGB)
    obj_img3 = cv2.cvtColor(obj_img, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(obj_img3)
    return pil_image


def alterar_rgb():
    try:
        scale.imagem_alterada = calc_rgb(scale.imagem_alteradaB, scale.value0, scale.value1, scale.value2)
        scale.imagem_alterada = contrast(scale.imagem_alterada)
        scale.imagem_alterada = brilho(scale.imagem_alterada)
        scale.imagem_alterada = nitidez(scale.imagem_alterada)
        newFrame(scale.imagem_alterada)
    except:
        showerror("Conversor", "ERRO")


def negativo():
    try:
        resetFaders()
        scale.imagem_alterada = ImageChops.invert(scale.imagem_alteradaB)
        newFrame(scale.imagem_alterada)
        valor_negativo.set(1)  # RETIRAR
        valor_cinza.set(0)  # Retirar
    except:
        pass


def cinza():
    try:
        resetFaders()
        scale.imagem_alterada = scale.imagem_alteradaB.convert('L')
        newFrame(scale.imagem_alterada)
        valor_cinza.set(1)  # Retirar
        valor_negativo.set(0)
    except:
        pass

def contrast(imagem):
    im_contrast = ImageEnhance.Contrast(imagem)
    imagem = im_contrast.enhance(float(scale.valuecontraste))
    return imagem


def brilho(imagem):
    im_brilho = ImageEnhance.Brightness(imagem)
    imagem = im_brilho.enhance(float(scale.valuebrilho))
    return imagem

def nitidez(imagem):
    im_nitidez = ImageEnhance.Sharpness(imagem)
    imagem = im_nitidez.enhance(float(scale.valuenitidez))
    return imagem

def resetFaders():
    if scale.imagem_alterada:
        s1.set(0)
        s2.set(0)
        s3.set(0)
        s4_contraste.set(1.0)
        s5_brilho.set(1.0)
        s6_nitidez.set(1.0)
        valor_cinza.set(0)
        valor_negativo.set(0)
        scale.imagem_alterada = scale.imagem_alteradaB
        newFrame(scale.imagem_alterada)
    else:
        showerror("Conversor", "ERRO")


# MENU
barraDeMenu = Menu(root)
menuArquivo = Menu(barraDeMenu)
menuArquivo.add_command(label='Abrir', command=abrir_imagem)
menuArquivo.add_command(label='Salvar', command=salvar)
menuArquivo.add_command(label='Sair', command=sair)
barraDeMenu.add_cascade(label="Arquivo", menu=menuArquivo)

# IMAGEM
global label_imagem
label_imagem = Label(root)
label_imagem.grid(row=1, column=2, padx=10, rowspan=13, sticky='w')

label_azul = Label(root, text='azul').grid(row=2, column=0, padx=10, pady=1, sticky='NE')
label_amarelo = Label(root, text='amarelo').grid(row=2, column=0, padx=10, pady=1, sticky='NW')
label_verde = Label(root, text='verde').grid(row=4, column=0, padx=10, pady=1, sticky='NE')
label_magenta = Label(root, text='magenta').grid(row=4, column=0, padx=10, pady=1, sticky='NW')
label_verde = Label(root, text='vermelho').grid(row=6, column=0, padx=10, pady=1, sticky='NE')
label_magenta = Label(root, text='ciano').grid(row=6, column=0, padx=10, pady=1, sticky='NW')
label_contraste = Label(root, text='contraste').grid(row=9, column=0, padx=10, pady=1,sticky='N')
label_brilho = Label(root, text='brilho').grid(row=11, column=0, padx=10, pady=1,sticky='N')
label_nitidez = Label(root, text='nitidez').grid(row=13, column=0, padx=10, pady=1,sticky='N')

# WIDGETS
s1 = Scale(root, from_=-100, to=100, length=200, resolution=1, orient=HORIZONTAL,
           command=lambda v: setattr(scale, 'value0', v))
s1.set(0)
s1.grid(row=1, column=0, padx=10, pady=1)

s2 = Scale(root, from_=-100, to=100, length=200, resolution=1, orient=HORIZONTAL,
           command=lambda v: setattr(scale, 'value1', v))
s2.set(0)
s2.grid(row=3, column=0, padx=10, pady=1)

s3 = Scale(root, from_=-100, to=100, length=200, resolution=1, orient=HORIZONTAL,
           command=lambda v: setattr(scale, 'value2', v))
s3.set(0)
s3.grid(row=5, column=0, padx=10, pady=1)

s4_contraste = Scale(root, from_=0.1, to=2.0, length=200, resolution=0.1, orient=HORIZONTAL,
           command=lambda v: setattr(scale, 'valuecontraste', v))
s4_contraste.set(1.0)
s4_contraste.grid(row=8, column=0, padx=10, pady=1)

s5_brilho = Scale(root, from_=0.1, to=2.0, length=200, resolution=0.1, orient=HORIZONTAL,
           command=lambda v: setattr(scale, 'valuebrilho', v))
s5_brilho.set(1.0)
s5_brilho.grid(row=10, column=0, padx=10, pady=1)

s6_nitidez = Scale(root, from_=-5.0, to=5.0, length=200, resolution=0.1, orient=HORIZONTAL,
           command=lambda v: setattr(scale, 'valuenitidez', v))
s6_nitidez.set(1.0)
s6_nitidez.grid(row=12, column=0, padx=10, pady=1)

btn_cinza = Button(root,
                   text="Cinza",
                   width=7,
                   command=cinza
                   ).grid(row=7, column=0, padx=10, pady=10, sticky='w')

btn_negativo = Button(root,
                      text="Negativo",
                      width=7,
                      command=negativo
                      ).grid(row=7, column=0, padx=10, pady=10, sticky='e')

btn_preview = Button(root,
                     text="PREVIEW",
                     width=10,
                     bg="green",
                     fg="white",
                     command=alterar_rgb)
btn_preview.grid(row=2, column=1, padx=10, pady=10, sticky='w')

btn_reset = Button(root,
                   text="RESET",
                   width=10,
                   bg="green",
                   fg="white",
                   command=resetFaders)
btn_reset.grid(row=4, column=1, padx=10, pady=10, sticky='w')

btn_save = Button(root,
                  text="SALVAR",
                  width=10,
                  bg="green",
                  fg="white",
                  command=salvar)
btn_save.grid(row=6, column=1, padx=10, pady=10, sticky='w')

root.config(menu=barraDeMenu)
root.mainloop()
