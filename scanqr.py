# Importing library
import cv2
from pyzbar.pyzbar import decode
import requests



# Reference 
# https://www.geeksforgeeks.org/how-to-make-a-barcode-reader-in-python/

# Insert URL
url = "http://localhost/qrcode/"


# Function for read barcode
def BarcodeReader(image):

    # read the image in numpy array using cv2
    # img = cv2.imread(image)
    img = image
    # Decode the barcode image
    detectedBarcodes = decode(img)

    # If not detected then print the message
    if not detectedBarcodes:
        print("Tidak ada barcode terdeteksi")
    else:

        # Traverse through all the detected barcodes in image
        for barcode in detectedBarcodes:
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect

            # Put the rectangle in image using
            # cv2 to highlight the barcode
            cv2.rectangle(img, (x-10, y-10),
                          (x + w+10, y + h+10),
                          (255, 0, 0), 2)

            if barcode.data != "":

                # Data yang akan dikirim
                datana = {
                    'absen' : "ok",
                    'data': str(barcode.data),
                    'type': str(barcode.type),
                }

                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded'
                }

                response = requests.request("POST", url, headers=headers, data=datana)

                print(response.text)


cap = cv2.VideoCapture(0)
while True:
    check, frame = cap.read()

    BarcodeReader(frame)            
    cv2.imshow('video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
