# -------------------------------------------------
# -- practical => image manipulation with pillow --
# -------------------------------------------------

from PIL import Image

# open the image
myimage = Image.open("D:\python\img1.jpg")


# show the image

myimage.show()

# my cropped image

mybox = (300, 300, 800, 800)
mynewimage = myimage.crop(mybox)

# show the new image

mynewimage.show()

# my converted mode image
myconverted = myimage.convert("L")
myconverted.show()