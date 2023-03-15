import cv2
import pytesseract

framewidth = 1920
frameheight = 1080

cap = cv2.VideoCapture(0)

cap.set(3, framewidth)
cap.set(4, frameheight)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    success, img = cap.read()

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
    img=blackAndWhiteImage
    # img = cv2.bitwise_not(img)

    # row / collumn
    img = img[830:925, 300:800]

    if cv2.waitKey(1) & 0xFF == ord('f'):
        text = pytesseract.image_to_string(img)
        print(text)

    cv2.imshow("video", img)
