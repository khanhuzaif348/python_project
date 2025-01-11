#  Qr_code Generator 

import qrcode as qr


img = qr.make("https://github.com/khanhuzaif348/python_project/tree/main")


img.save("github.png")





#  Red color  Qr_code Generator 

import qrcode

from PIL import Image


from qrcode.console_scripts import error_correction

qr =qrcode.QRCode(version=1,
                  error_correction=qrcode.constants.ERROR_CORRECT_H,
                  box_size=10,border=4)
                  
qr.add_data("https://github.com/khanhuzaif348/python_project/tree/main")

qr.make(fit=True)

img=qr.make_image(fill_color="red",back_color="white")

img.save("github1.png")

