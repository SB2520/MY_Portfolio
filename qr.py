import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Set up QR code configuration
qr = qrcode.QRCode(
    version=1,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data("https://my-portfolio-five-alpha-58.vercel.app/")
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("portfolio.jpg")
