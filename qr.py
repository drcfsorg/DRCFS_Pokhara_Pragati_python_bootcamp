
# Importing library
import qrcode
 
# Data to be encoded
data = 'https://forms.office.com/r/0m5e09HJ34'
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('MyQRCode1.png')