import datetime
import cv2
from pyzbar.pyzbar import decode 

camera = cv2.VideoCapture(cv2.CAP_DSHOW)
scanner = cv2.QRCodeDetector()

while True:
    _, img = camera.read()
    data, one, _ = scanner.detectAndDecode(img)
    if data:
        qrcode = data
        break
    cv2.imshow('QR Code Scanner', img)
    #Press q to exit
    if cv2.waitKey(1) == ord('q'):
        break

for code in decode(img):
    data = code.data.decode('utf-8')
    now = datetime.datetime.now()
    dateNtime = now.strftime("%y-%m-%d %H:%M:%S")
    txt_file = open('QR_Code_Data.txt', 'w')
    txt_file.write(dateNtime)
    txt_file.write(data)
    txt_file.close()

camera.release()
cv2.destroyAllWindows
