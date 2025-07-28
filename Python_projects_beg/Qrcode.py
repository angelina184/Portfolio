import qrcode
from qrcode.constants import ERROR_CORRECT_H

user_answer = input("Enter URL/text:").strip()
file_name = input("Enter the name of the file (filename.jpg):").strip()
qr = qrcode.QRCode(version=1, box_size = 10, border = 5)
qr.add_data(user_answer)
qr.make(fit = True)
image = qr.make_image(fill_color = 'white',back_color = 'black')
image.save(file_name)
print(f"QR saved as {file_name}")