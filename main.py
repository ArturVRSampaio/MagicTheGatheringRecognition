import cv2
import pytesseract
import re

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

    #remove strange simbols from the reading
    img = cv2.rectangle(img, (625, 350), (750, 400), (0,0,0), -1)
    img = cv2.rectangle(img, (650, 400), (670, 450), (0,0,0), -1)
    img = cv2.rectangle(img, (760, 400), (830, 450), (0,0,0), -1)

    # collumn / ROW
    img = img[350:450, 530:830]

    #blur + b&w image + invert
    img = cv2.blur(img, [2, 2], 0)
    img = cv2.threshold(img, 16, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=1)

    if cv2.waitKey(1) & 0xFF == ord('f'):
        rawText = pytesseract.image_to_string(img, config='--psm 6')

        items = re.findall(r'\b\w+\b', rawText)


        print(rawText)
        print(items)
        print("*******")

    cv2.imshow("video", img)
