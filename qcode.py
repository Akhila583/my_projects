import qrcode
import image
qr=qrcode.QRCode(version=15,box_size=10,border=5)
data="https://www.linkedin.com/in/akhila-komatiguntla-7a5166247/"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="back",back_color='white')
img.save("test2.png")
