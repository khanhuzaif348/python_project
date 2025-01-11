#  Qr_code Generator 

import qrcode as qr


img = qr.make("https://github.com/khanhuzaif348/python_project/tree/main")


img.save("github.png")
