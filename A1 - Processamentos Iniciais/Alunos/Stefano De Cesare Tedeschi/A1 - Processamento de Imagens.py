'''
===================================================================================================================

Tutorial de execução para o codigo abaixo

1º passo - Baixe e instale o Python no computador[url para download direto: https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe]
(não precisa de nenhuma configuração especial só pressione proximo)
2º passo - Aperte "Ctrl + Shift + X" e busque pela extensão oficial da Microsoft pro Python e a instale
(pesquisar por Python)
3º passo - Instale tambem a extensão com o nome de "Code Runner" feita por Jun Han
(essa extensão pode executar varias linguagens sem a necessidade de compilar o algoritmo num programa toda vez)
4º passo - Abra o CMD["Win + R" e escreva "cmd"] e digite o seguinte
    + python -m tkinter (Se abrir uma janela significa que a instalação do python deu certo, é só fecha-la)
    + python -m pip install pillow
5º passo - Voltar para este codigo e apertar "Ctrl + Alt + N" ou clicar no botão de play no canto superior direito 
da tela do codigo

===================================================================================================================
Espero que o tutorial tenha sido facil e que não tenha dado nenhum problema, testei em 2 pcs e foi de boa.
É a 1ª vez q mexo com python então já aviso aqui que o programa é lento, mas acho que deve ser pelo programa 
passar por todos os pixels da imagem

PS: alterar as cores remove o efeito de greyscale e/ou negativo, então use primeiro os sliders de cores e depois
aplique o efeito de imagem
Feito por Stefano De Cesare Tedeschi
'''
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

def enableControle():
    botao_greyscale.config(state = 'active')
    botao_negativo.config(state = 'active')
    barra_cor_vermelha.config(state = 'active')
    barra_cor_verde.config(state = 'active')
    barra_cor_azul.config(state = 'active')
    barra_alpha.config(state = 'active')
    botao_resetar.config(state = 'active')
    botao_salvar.config(state = 'active')

    texto_cor_vermelha.config(state = 'active')
    texto_cor_verde.config(state = 'active')
    texto_cor_azul.config(state = 'active')
    texto_alpha.config(state = 'active')
    resetImg()

imagemEmCache = None
imagemOriginal = None
caminhoArquivo = None
def browseFiles():
    global caminhoArquivo
    caminhoArquivo = filedialog.askopenfilename(
        initialdir = "/",
        title = "Selecione uma Imagem",
        filetypes = [("Arquivos de Imagem",".png .jpg .jpeg .gif .tiff")]
    )
    global imagemEmCache
    global imagemOriginal
    imagemEmCache = Image.open(caminhoArquivo)
    imagemEmCache.thumbnail((512,512),Image.ANTIALIAS)
    imagemOriginal = imagemEmCache
    enableControle()

def greyscale():
    global imagemEmCache
    greyscaleImage = imagemEmCache.convert("RGBA")
    for y in range(greyscaleImage.height):
        for x in range(greyscaleImage.width):
            pixelRGB = greyscaleImage.getpixel((x,y))
            media = int((pixelRGB[0] + pixelRGB[1] + pixelRGB[2])/3)
            greyscaleImage.putpixel((x,y),(media,media,media,pixelRGB[3]))
    imagemEmCache = greyscaleImage
    atualizaPrevia(imagemEmCache)

def negative():
    global imagemEmCache
    negativeImage = imagemEmCache.convert("RGBA")
    for y in range(negativeImage.height):
        for x in range(negativeImage.width):
            pixelRGB = negativeImage.getpixel((x,y))
            negativeImage.putpixel((x,y),(255-pixelRGB[0],255-pixelRGB[1],255-pixelRGB[2],pixelRGB[3]))
    imagemEmCache = negativeImage
    atualizaPrevia(imagemEmCache)

incrementoPixel = [0,0,0,0]
def atualizarVermelho(value):
    global incrementoPixel
    incrementoPixel[0]=int(value)
    alterarCor()
def atualizarVerde(value):
    global incrementoPixel
    incrementoPixel[1]=int(value)
    alterarCor()
def atualizarAzul(value):
    global incrementoPixel
    incrementoPixel[2]=int(value)
    alterarCor()
def atualizarAlpha(value):
    global incrementoPixel
    incrementoPixel[3]=int(value)
    alterarCor()
def alterarCor():
    global imagemEmCache, imagemOriginal, incrementoPixel
    imagemAlterada = imagemOriginal.convert("RGBA")
    for y in range(imagemAlterada.height):
        for x in range(imagemAlterada.width):
            pixelRGB = imagemAlterada.getpixel((x,y))
            alpha = 0
            if pixelRGB[3] > 0:
                alpha = incrementoPixel[3]
            imagemAlterada.putpixel((x,y),(pixelRGB[0]+incrementoPixel[0],pixelRGB[1]+incrementoPixel[1],pixelRGB[2]+incrementoPixel[2],alpha))
    imagemEmCache = imagemAlterada
    atualizaPrevia(imagemEmCache)
    
def atualizaPrevia(img):
    img = img.convert("RGBA")
    tkimage = ImageTk.PhotoImage(img)
    previaImagem.config(corpo,
        image = tkimage,
        width = "382px",height = "382px",
        background = "#fff"
    )    
    previaImagem.image = tkimage
    previaImagem.update()
    labelImagem.update()

def resetImg():
    global imagemEmCache
    global imagemOriginal
    imagemEmCache = imagemOriginal
    atualizaPrevia(imagemOriginal)
    barra_cor_vermelha.set(0)
    barra_cor_verde.set(0)
    barra_cor_azul.set(0)
    barra_alpha.set(255)

def salvarImg():
    global imagemEmCache
    files = [("Arquivo JPEG","*.jpeg"),("Arquivo TIFF","*.tiff"),("Arquivo PNG","*.png"),("Arquivo GIF","*.gif")]
    file = filedialog.asksaveasfilename(defaultextension="*.*",filetypes=files)
    if file:
        imagemEmCache.save(file)

window = Tk()
window.title("Atividade Avaliativa de Processamento de Imagem.")
width = 800
height = 600
xPos = window.winfo_screenwidth()/2 - width/2
yPos = window.winfo_screenheight()/2 - height/2
windowPos = "%dx%d+%d+%d" % (width, height, xPos, yPos)
window.geometry(windowPos)
window.resizable(False,False) #comenta aqui caso de algum problema de a imagem estar muito pequena
window.config(background = "white")

cabecalho = Label(window,
    text= "Atividade Avaliativa de Processamento de Imagens\n\nFerramenta de manipulação de cores",
    background = "#f7f5dc"
)
corpo = Label(window,
    background = "#f7f5dc"
)
rodape = Label(window,
    background = "#f7f5dc"
)

controle = Label(corpo,
    background = "#fff"
)
labelImagem = Label(corpo,
    background = "#fff"
)
previaImagem = Label(labelImagem,
    image = None,
    background = "#fff"
)

botao_procurar = Button(rodape,
    text = "Procurar Imagem",
    command = browseFiles
)
botao_sair = Button(rodape,
    text = "Fechar Janela",
    command = exit
)

botao_salvar = Button(controle,
    text = "Salvar Imagem",
    command = salvarImg
)
botao_resetar = Button(controle,
    text = "Resetar Imagem",
    command = resetImg
)
botao_greyscale = Button(controle,
    text = "Greyscale",
    command = greyscale
)
botao_negativo = Button(controle,
    text = "Negative",
    command = negative
)
barra_cor_vermelha = Scale(controle,
    from_=-255,
    to=255,
    orient='horizontal',
    command=atualizarVermelho
)
texto_cor_vermelha = Label(controle,
    text="Vermelho"
)
barra_cor_verde = Scale(controle,
    from_=-255,
    to=255,
    orient='horizontal',
    command=atualizarVerde
)
texto_cor_verde = Label(controle,
    text="Verde"
)
barra_cor_azul = Scale(controle,
    from_=-255,
    to=255,
    orient='horizontal',
    command=atualizarAzul
)
texto_cor_azul = Label(controle,
    text="Azul"
)
barra_alpha = Scale(controle,
    from_=0,
    to=255,
    orient='horizontal',
    command=atualizarAlpha
)
texto_alpha = Label(controle,
    text="Alpha"
)

cabecalho.place(relx= 0.5,rely=0,relwidth=1,relheight=0.1,anchor=N)
corpo.place(relx= 0.5,rely=0.5,relwidth=1,relheight=0.8,anchor=CENTER)
rodape.place(relx= 0.5,rely=1,relwidth=1,relheight=0.1,anchor=S)

labelImagem.place(rely=0.5,relx=0.02,relwidth=0.65,relheight=0.98,anchor=W)
previaImagem.place(rely=0.5,relx=0.5,relwidth=0.98,relheight=0.98,anchor=CENTER)
controle.place(rely=0.5,relx=0.98,relwidth=0.3,relheight=0.98,anchor=E)

botao_procurar.place(relx=0.82,rely=0.5,relwidth=.125,anchor=E)
botao_sair.place(relx=0.96,rely=0.5,relwidth=.1,anchor=E)

botao_greyscale.place(relx=0.05,rely=0.05,relwidth=.40,anchor=W)
botao_negativo.place(relx=0.55,rely=0.05,relwidth=.40,anchor=W)
texto_cor_vermelha.place(relx=0.05,rely=0.10,relwidth=.90,anchor=NW)
barra_cor_vermelha.place(relx=0.05,rely=0.15,relwidth=.90,anchor=NW)
texto_cor_verde.place(relx=0.05,rely=0.25,relwidth=.90,anchor=NW)
barra_cor_verde.place(relx=0.05,rely=0.30,relwidth=.90,anchor=NW)
texto_cor_azul.place(relx=0.05,rely=0.40,relwidth=.90,anchor=NW)
barra_cor_azul.place(relx=0.05,rely=0.45,relwidth=.90,anchor=NW)
texto_alpha.place(relx=0.05,rely=0.55,relwidth=.90,anchor=NW)
barra_alpha.place(relx=0.05,rely=0.60,relwidth=.90,anchor=NW)
botao_resetar.place(relx=0.05,rely=0.95,relwidth=.40,anchor=SW)
botao_salvar.place(relx=.55,rely=0.95,relwidth=.40,anchor=SW)

botao_greyscale.config(state = 'disabled')
botao_negativo.config(state = 'disabled')
barra_cor_vermelha.config(state = 'disabled')
barra_cor_verde.config(state = 'disabled')
barra_cor_azul.config(state = 'disabled')
barra_alpha.config(state = 'disabled')
botao_resetar.config(state = 'disabled')
botao_salvar.config(state = 'disabled')

texto_cor_vermelha.config(state = 'disabled')
texto_cor_verde.config(state = 'disabled')
texto_cor_azul.config(state = 'disabled')
texto_alpha.config(state = 'disabled')

window.mainloop()
