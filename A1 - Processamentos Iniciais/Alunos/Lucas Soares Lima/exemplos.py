import PIL
from PIL import Image
from matplotlib import image
from matplotlib import pyplot
from numpy import asarray

## LENDO UMA IMAGEM MAPTPLOTLIB ##
data = image.imread("image03.jpg")

## LENDO UMA IMAGEM COM PIL ##
img = Image.open('image03.jpg')

print('teste')
## PIL ##

## DADOS DA IMAGEM PIL ##
print(img.format)
print(img.size)

## DADOS DE UMA IMAGEM COMO ARRAY ##
image2 = Image.fromarray(data)
print(type(image2))

## TRASFORMANDO UM ELEMENTO IMAGEM EM ARRAY ##
data = asarray(img)
print(data)

## SALVANDO UMA IMAGEM
img.save("img/salvas/image.jpg",format="PNG")

## DEIXANDO UMA IMAGEM CINZA ##
image_cinza = img.convert(mode="L")
image_cinza.save("img/salvas/image_cinza.jpg")

## SALVANDO UMA IMAGEM MANTENDO O RADIO ##
print(img.size)
img.thumbnail((500,500))
print(img.size)
img.save("img/salvas/image_menor.jpg")

## SALVANDO UMA IMAGEM MANTENDO IGNORANDO O RADIO ##
print(img.size)
image_resize = img.resize((500,500))
print(img.size)
image_resize.save("img/salvas/image_menor_square.jpg")

## GIRANDO A IMAGEM ##

## Esquerda e direita ##
horizontal_image = img.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_image.save("img/salvas/image_esqu_dir.jpg")

## Cabeça pra baixo ##
vertical_image = img.transpose(Image.FLIP_TOP_BOTTOM)
vertical_image.save("img/salvas/image_up_down.jpg")

## 45 graus ##
image_45 = img.rotate(45)
image_45.save("img/salvas/image_45.jpg")

## CORTANDO A IMAGEM ##
image_cropped = img.crop((100,100,200,200))
image_cropped.save("img/salvas/image_crop.jpg")

## NATIVO ##

## DADOS DE UMA IMAGEM COMO ARRAY ##
print(data)
print(data.dtype)
print(data.shape)
print(data.max())
print(data.min())
print(pyplot.imshow(data))


