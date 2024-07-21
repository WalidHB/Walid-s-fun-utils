import cv2
import pytesseract


image = ''

img = cv2.imread(image)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Adding custom options
custom_config = r'--oem 3 --psm 6'
print(pytesseract.image_to_string(img, config=custom_config, lang='eng'))
