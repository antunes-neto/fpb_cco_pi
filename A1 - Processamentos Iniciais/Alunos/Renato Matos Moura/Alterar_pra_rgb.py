import numpy as np
import cv2
import matplotlib.pyplot as plt 
from PIL import Image

img = cv2.imread('imagem.jpg')

(canalAzul, canalVerde, canalVermelho) = cv2.split(img)

zeros = np.zeros(img.shape[:2], dtype = "uint8")

cv2.imshow("Vermelho", cv2.merge([zeros, zeros,canalVermelho]))

cv2.imshow("Verde", cv2.merge([zeros, canalVerde, zeros]))

cv2.imshow("Azul", cv2.merge([canalAzul, zeros, zeros]))

cv2.waitKey(0)
