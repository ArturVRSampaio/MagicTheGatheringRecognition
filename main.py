import cv2
import pytesseract

framewidth = 800
frameheight = 600

cap = cv2.VideoCapture(0)

cap.set(3, framewidth)
cap.set(4, frameheight)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    success, img = cap.read()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.bitwise_not(img)
    h = 600
    w = 800

    y = 500
    x = 100
    img = img[y:y + h, x:x + w]

    if cv2.waitKey(1) & 0xFF == ord('f'):
        text = pytesseract.image_to_string(img)
        print(text)

    cv2.imshow("video", img)
