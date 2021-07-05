from PIL import Image
#img  = Image.open(path)     
# On successful execution of this statement,
# an object of Image type is returned and stored in img variable)
   
try: 
    img  = Image.open("/mnt/c/Users/EVELIZGR/OneDrive/Nego/api/factura-autonomo.jpg")
except IOError:
    pass
img.save("/mnt/c/Users/EVELIZGR/OneDrive/Nego/api/out/factura-autonomo01.jpg")
# Use the above statement within try block, as it can 
# raise an IOError if file cannot be found, 
# or image cannot be opened.