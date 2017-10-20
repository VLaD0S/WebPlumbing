import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE' , 'WebPlumbing.settings')

from django.conf import settings

from PIL import Image

"""
This file is dedicated to any sort of bulk image edit operations. 
Should be modified such that any directories added to a dictionary to undergo the operation.
"""

plumbing_profiles_path = os.path.join(settings.BASE_DIR, "plumbing", "static", "images", "profiles")


def image_toSquare(path, resolution):
    dirs = os.listdir( path )
    
    nwidth, nheight = resolution
    #loops through images
    for item in dirs:
        item_path = os.path.join(path, item)
        image_name, image_extension = os.path.splitext(item_path)

        img = Image.open(item_path)
        img = resizer(img, resolution) 
        img = croppepr(img)

        img.save(image_name + image_extension, 'JPEG', quality=90)



#Crops a 200px wide square from the image center.
def croppepr(img, nwidth, nheight):
    width, height = img.size
    return img.crop(((width/2)-100, (height/2)-100, (width/2)+100, (height/2)+100))

#Resizes the image such that the smallest side is 200px long. Preserves aspect ratio.
def resizer(img, resolution):

    width, height = img.size
    smallest = min(width, height)
    if smallest > min(resolution):
        proportion = smallest/min(resolution)
        return img.resize((int(width/proportion), int(height/proportion)), Image.ANTIALIAS)
    else: 
        return img

