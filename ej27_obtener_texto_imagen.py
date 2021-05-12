#Obtener texto de una imagen

import cv2
import pytesseract

# Este ejercicio muestra como usar la libreria pytesseract para leer de una imagen png el texto q tiene

imagen = cv2.imread("open   .png")

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"
text = pytesseract.image_to_string(imagen)
print(text)
