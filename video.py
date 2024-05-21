import cv2 

video = cv2.VideoCapture("video/runners.mp4")

while True:
    check, img = video.read()
    cv2.imshow('Vídeo', img)
    cv2.waitKey(10)