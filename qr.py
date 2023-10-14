import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data('http://mobi-bio.glitch.me')


mobi_bio = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())

mobi_bio.save("MOBI.png")