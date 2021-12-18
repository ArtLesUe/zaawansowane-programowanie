import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'


def read_text_from_image(img: str) -> str:
    img_cv = cv2.imread(img)
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    return pytesseract.image_to_string(img_rgb)


print("IMG-1: " + read_text_from_image("img/img-1.png") + "\n===\n")
print("IMG-2: " + read_text_from_image("img/img-2.jpg") + "\n===\n")
print("IMG-3: " + read_text_from_image("img/img-3.png") + "\n===\n")
print("IMG-4: " + read_text_from_image("img/img-4.png") + "\n===\n")
print("IMG-5: " + read_text_from_image("img/img-5.jpg") + "\n===\n")