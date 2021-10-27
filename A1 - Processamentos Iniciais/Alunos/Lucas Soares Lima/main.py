import PIL
from PIL import Image
from matplotlib import image
from matplotlib import pyplot
from numpy import asarray

endereco = 'image.jpg'
nome = endereco.split('.')[0]

img = Image.open(endereco)

## Cinza
image_cinza = img.convert(mode="L")
image_cinza.save("img/data/" + nome + "-cinza.jpg")

## Girando na horizontal
horizontal_image = img.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_image.save("img/data/" + nome + "-horizontal.jpg")

## Girando na vertical ##
vertical_image = img.transpose(Image.FLIP_TOP_BOTTOM)
vertical_image.save("img/data/" + nome + "-vertical.jpg")

## 45 graus ##
image_45 = img.rotate(45)
image_45.save("img/data/" + nome + "-45.jpg")

## CORTANDO A IMAGEM ##
image_cropped = img.crop((100, 100, 200, 200))
image_cropped.save("img/data/" + nome + "-crop.jpg")

## Proporções
img.thumbnail((500, 500))
img.save("img/data/" + nome + "-menor.jpg")

## Forçando proporção
img.resize((500, 500))
img.save("img/data/" + nome + "-menor-forcada.jpg")
