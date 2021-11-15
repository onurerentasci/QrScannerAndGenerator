import time
import cv2 #for the read image/camera input
from pyzbar.pyzbar import decode
import requests #for the https
from PIL import Image
from io import BytesIO

#QR2URL

def qr2url():
    img = cv2.imread('qr.png') #import the qr photo
    for a in decode(img):
        #print(decode(img))
        print(a.data.decode('utf-8'))


#CAM2URL

def cam2url():
    cap = cv2.VideoCapture(0) #use webcam for scanning
    cap.set(3,640)
    cap.set(4,480)
    usedCodes = []
    cam = True
    while cam == True:
        success, frame = cap.read()

        for a in decode(frame):
            if a.data.decode('utf-8') not in usedCodes:
                print("pass")
                print(a.data.decode('utf-8'))
                usedCodes.append(a.data.decode('utf-8'))
                time.sleep(5)
            elif a.data.decode('utf-8') in usedCodes:
                print("already used")
                time.sleep(5)
            else:
                pass

        cv2.imshow('Testing-code-scan', frame)
        cv2.waitKey(1)



# URL2QR

def url2qr():
    url = input("Geçerli URL'yi veya QR koda dönüştürmek istediğiniz metni giriniz :   ")

    endPoint = "https://api.qrserver.com/v1/create-qr-code/"

    orn = "?data={}&amp;size=500x500".format(url)
    color = "&color=B02A25" #sets the color of the generated qr code

    response = requests.get(endPoint + orn + color)
    img = Image.open(BytesIO(response.content))

    img.save("qr.png")

qr2url()
