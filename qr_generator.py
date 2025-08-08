import qrcode

upi_link = "upi://pay?pa=9307359558@ybl&pn=SmartRestaurant&am=0"
img = qrcode.make(upi_link)
img.save("qr_code.png")

print("✅ QR Code saved as qr_code.png")