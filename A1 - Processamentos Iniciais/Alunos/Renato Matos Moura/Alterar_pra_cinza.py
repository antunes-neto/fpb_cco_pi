from PIL import Image

img = Image.open('imagem.jpg')
imgGray = img.convert('L')
imgGray.save('imagem_convertida_em_cinza.jpg')
