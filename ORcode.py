import qrcode

data = 'http://www.baidu.com/'
img_file = r'保存路径'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data(data)

qr.make(fit=True)

img = qr.make_image()

img.save(img_file)

img.show()