import cv2 
import matplotlib.pyplot as plt 
 
img_bgr = cv2.imread('imagem.jpg', 1)  
img_neg = 1 - img_bgr 
  
plt.imshow(img_neg) 
plt.savefig('imagem_convertida_em_negativa.jpg')
