import pytesseract
import re
import cv2
import sys

# loading pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def img_processing(f1, template_number):
    # print(sys.argv[0])
    img = cv2.imread(f1)
    greyscale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gaussian_blur = cv2.GaussianBlur(greyscale_img, (7, 7), 2)
    sharpened2 = cv2.addWeighted(greyscale_img, 3.5, gaussian_blur, -2.5, 0)
    bil_out2 = cv2.bilateralFilter(sharpened2, 5, 6, 6)
    # cv2.imshow('original', img)
    # cv2.imshow('processed image', bil_out2)
    # cv2.waitKey(0)
    return recognition_distributor(bil_out2, template_number)


def recognition_distributor(bil_out2, template_number):
    if template_number == "1":
        ocr_recognition_template1(bil_out2)
    elif template_number == "2":
        ocr_recognition_template2(bil_out2)
    elif template_number == "3":
        ocr_recognition_template3(bil_out2)


def ocr_recognition_template1(f1):
    # recognizing text from image using ocr
    text1 = pytesseract.image_to_string(f1)
    # print(text1)

    # regex to find the sentence
    m = re.findall(r'“.*.”', text1)
    if len(m) != 0:
        x = m[0].find('“')
        y = m[0].find('”')
        # print(x, y)
        print(m[0][x + 1:y])
    # print(m[0])


def ocr_recognition_template2(f1):
    # recognizing text from image using ocr
    print("Entering 2nd template logic")
    text2 = pytesseract.image_to_string(f1)
    result = re.sub(" ", "", text2)
    print(result)


def ocr_recognition_template3(f1):
    print("Entering template 3")
    # recognizing text from image using ocr
    text3 = pytesseract.image_to_string(f1)

    # regex to find the sentence
    m = re.findall(r'Type.*.', text3)
    if len(m) != 0:
        x = m[0].find(': ')
        y = m[0].find('. ')

        if x != -1:
            captcha_string = m[0][x + 2:]
            print(captcha_string)
            result = re.sub(" ", "", captcha_string)
            print(result)
        if y != -1:
            captcha_string = m[0][y + 2:]
            print(captcha_string)
            result = re.sub(" ", "", captcha_string)
            print(result)
    # print(m[0])


img_processing(sys.argv[1], sys.argv[2])
