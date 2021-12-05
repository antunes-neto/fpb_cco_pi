'''
===================================================================================================================
IMPORTANTE eu mandei uma versão mais antiga no blackboard essa é a mais nova
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
PSS: mexer nas cores e no tamanho da tela/imagem sobescreve o filtro. É necessario utilizar um depois o outro, a ordem pode estar invertida em alguns casos.
Feito por Stefano De Cesare Tedeschi
'''
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import math

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


imagemOriginal = None
imagemEmCache = None
caminhoArquivo = None
def browseFiles():
    global caminhoArquivo
    caminhoArquivo = filedialog.askopenfilename(
        initialdir = "/",
        title = "Selecione uma Imagem",
        filetypes = [("Arquivos de Imagem",".png .jpg .jpeg .gif .tiff")]
    )
    global imagemOriginal
    imagemOriginal = Image.open(caminhoArquivo)
    enableControle()

def greyscale(image):
    print("greyscale")
    if(image == None):
        return
    greyscaleImage = image.convert("RGBA")
    for y in range(greyscaleImage.height):
        for x in range(greyscaleImage.width):
            pixelRGB = greyscaleImage.getpixel((x,y))
            media = int((pixelRGB[0] + pixelRGB[1] + pixelRGB[2])/3)
            greyscaleImage.putpixel((x,y),(media,media,media,pixelRGB[3]))
    return greyscaleImage
    

def negative(image):
    print("negativate")
    negativeImage = image.convert("RGBA")
    for y in range(negativeImage.height):
        for x in range(negativeImage.width):
            pixelRGB = negativeImage.getpixel((x,y))
            negativeImage.putpixel((x,y),(255-pixelRGB[0],255-pixelRGB[1],255-pixelRGB[2],pixelRGB[3]))
    return negativeImage

incrementoPixel = [0,0,0,0]
def atualizarVermelho(value):
    global incrementoPixel
    incrementoPixel[0]=int(value)
    atualizarImagemEmCache("filter")
def atualizarVerde(value):
    global incrementoPixel
    incrementoPixel[1]=int(value)
    atualizarImagemEmCache("filter")
def atualizarAzul(value):
    global incrementoPixel
    incrementoPixel[2]=int(value)
    atualizarImagemEmCache("filter")
def atualizarAlpha(value):
    global incrementoPixel
    incrementoPixel[3]=int(value)
    atualizarImagemEmCache("filter")
def alterarCor(image):
    print("filter")
    global incrementoPixel
    imagemAlterada = image.convert("RGBA")
    for y in range(imagemAlterada.height):
        for x in range(imagemAlterada.width):
            pixelRGB = imagemAlterada.getpixel((x,y))
            pixelAlterado = [0,0,0,0]
            for aux in range(3):
                if pixelRGB[aux] > 0:
                    pixelAlterado[aux] = pixelRGB[aux]+incrementoPixel[aux]
            if pixelRGB[3] > 0:
                pixelAlterado[3] = incrementoPixel[3]
            imagemAlterada.putpixel((x,y),(pixelAlterado[0],pixelAlterado[1],pixelAlterado[2],pixelAlterado[3]))
    return imagemAlterada
    
def atualizaTamanho(image): 
    print("resize")   
    canvas_width = tela_x.get()
    canvas_height = tela_y.get()
    #mudar tamanho canvas
    imagemRedimensionada = Image.new("RGBA", (canvas_width, canvas_height), (0, 0, 0, 255))

    #mudar tamanho imagem
    image_width = imagem_x.get()
    image_height = imagem_y.get()

    x1 = int(math.floor((canvas_width - image_width) / 2))
    y1 = int(math.floor((canvas_height - image_height) / 2))
    pasteImg = image.resize((image_width,image_height),Image.ANTIALIAS)
    imagemRedimensionada.paste(pasteImg,(x1,y1))
    return imagemRedimensionada

imagemFiltrada = None
imagemRedimensionada = None
def atualizarImagemEmCache(action):
    global imagemOriginal, imagemEmCache, imagemFiltrada, imagemRedimensionada
    #imagemEmCache = imagemOriginal
    #filtrar
    match action:
        case "greyscale":
            imagemEmCache = greyscale(imagemEmCache)
            imagemFiltrada = imagemEmCache
        case "negativate":
            imagemEmCache = negative(imagemEmCache)
            imagemFiltrada = imagemEmCache
        case "filter":
            imagemFiltrada = alterarCor(imagemEmCache)
    #redimensionar
    match action:
        case "resize":
            imagemEmCache = atualizaTamanho(imagemFiltrada)
    atualizaPrevia()

def atualizaPrevia():
    global imagemEmCache
    if(imagemEmCache != None):
        _img = imagemEmCache.convert("RGBA")
        _img.thumbnail((512,512),Image.ANTIALIAS)
        tkimage = ImageTk.PhotoImage(_img)
        previaImagem.config(corpo,
            image = tkimage,
            #width = "382px",height = "382px",
            background = "#fff"
        )
        previaImagem.image = tkimage
    else:
        previaImagem.image = None
    previaImagem.update()
    labelImagem.update()

def resetImg():
    global imagemOriginal, imagemEmCache
    imagemEmCache = imagemOriginal
    atualizaPrevia()
    width, height = imagemOriginal.size
    tela_x.set(width)
    tela_y.set(height)
    imagem_x.set(width)
    imagem_y.set(height)
    barra_cor_vermelha.set(0)
    barra_cor_verde.set(0)
    barra_cor_azul.set(0)
    barra_alpha.set(255)

def salvarImg():
    global imagemEmCache
    files = [("Arquivo PNG","*.png"),("Arquivo GIF","*.gif"),("Arquivo TIFF","*.tiff")]
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
window.resizable(True,True) #comenta aqui em caso de algum problema de a imagem estar muito pequena
window.config(background = "white")

#region A1
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
    command = lambda:atualizarImagemEmCache("greyscale")
)
botao_negativo = Button(controle,
    text = "Negative",
    command = lambda:atualizarImagemEmCache("negativate")
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
#endregion

#region A2/N2
def only_numbers(char):
    return char.isdigit()
validation = controle.register(only_numbers)

texto_tamanho_tela = Label(controle,
    text="Tamanho da tela"
)
texto_campo_tamanho_tela_x = Label(controle,
    text="X:"
)
tela_x = IntVar(controle,value='0')
campo_tamanho_tela_x = Entry(controle,
    validate="key",
    validatecommand=(validation, '%S'),
    textvariable=tela_x
)
campo_tamanho_tela_x.bind('<FocusOut>',lambda x:(atualizarImagemEmCache('resize')))
texto_campo_tamanho_tela_y = Label(controle,
    text="Y:"
)
tela_y = IntVar(controle,value='0')
campo_tamanho_tela_y = Entry(controle,
    validate="key",
    validatecommand=(validation, '%S'),
    textvariable=tela_y
)
campo_tamanho_tela_y.bind('<FocusOut>',lambda x:(atualizarImagemEmCache('resize')))


texto_tamanho_imagem = Label(controle,
    text="Tamanho da Imagem"
)
texto_campo_tamanho_imagem_x = Label(controle,
    text="X:"
)
imagem_x = IntVar(controle, value=0)
campo_tamanho_imagem_x = Entry(controle,
    validate="key",
    validatecommand=(validation, '%S'),
    textvariable=imagem_x
)
campo_tamanho_imagem_x.bind('<FocusOut>', lambda x:(atualizarImagemEmCache('resize')))
texto_campo_tamanho_imagem_y = Label(controle,
    text="Y:"
)
imagem_y = IntVar(controle, value=0)
campo_tamanho_imagem_y = Entry(controle,
    validate="key",
    validatecommand=(validation, '%S'),
    textvariable=imagem_y
)
campo_tamanho_imagem_y.bind('<FocusOut>', lambda x:(atualizarImagemEmCache('resize')))
#endregion

#region posicionamento
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

texto_tamanho_tela.place(relx=0.05,rely=0.7,relwidth=.90,anchor=NW)
texto_campo_tamanho_tela_x.place(relx=0.05,rely=0.75,relwidth=.1,anchor=NW)
campo_tamanho_tela_x.place(relx=0.15,rely=0.75,relwidth=.3,anchor=NW)
texto_campo_tamanho_tela_y.place(relx=0.55,rely=0.75,relwidth=.1,anchor=NW)
campo_tamanho_tela_y.place(relx=0.65,rely=0.75,relwidth=.3,anchor=NW)

texto_tamanho_imagem.place(relx=0.05,rely=0.8,relwidth=.90,anchor=NW)
texto_campo_tamanho_imagem_x.place(relx=0.05,rely=0.85,relwidth=.1,anchor=NW)
campo_tamanho_imagem_x.place(relx=0.15,rely=0.85,relwidth=.3,anchor=NW)
texto_campo_tamanho_imagem_y.place(relx=0.55,rely=0.85,relwidth=.1,anchor=NW)
campo_tamanho_imagem_y.place(relx=0.65,rely=0.85,relwidth=.3,anchor=NW)

botao_resetar.place(relx=0.05,rely=0.925,relwidth=.40,anchor=NW)
botao_salvar.place(relx=.55,rely=0.925,relwidth=.40,anchor=NW)
#endregion

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
