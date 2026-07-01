import qrcode

link = input("Enter the link: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

filename = input("Enter file name (without .png): ")
img.save(filename + ".png")

print("QR Code generated successfully!")
