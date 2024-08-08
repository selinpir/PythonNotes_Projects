
"""
qr kod oluşturma:

    python -m
    + pip install qrcode
    + pip install image

"""

import qrcode
import image
qr=qrcode.QRCode(version=7,
                 box_size=12,
                 border=5)
data="https://www.youtube.com/watch?v=j56ujw-PLYQ"

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="red",back_color="black")
img.save("qr.png")
