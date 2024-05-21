import cv2

img = cv2.imread("img/farol.jpg")
imgCinza = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
print(imgCinza)

cv2.imshow("Imagem", imgCinza)
cv2.waitKey(0)