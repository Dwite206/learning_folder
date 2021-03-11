import sys
import os
from PIL import Image


# Grab first and second argument
# folders = input(sys.argv[1], sys.argv[2])
path1 = (sys.argv[1])
path2 = (sys.argv[2])


# check if new/ --folder exists, if not create
isExist = os.path.exists(path2)
try:
    if isExist == False:
        os.mkdir(path2)
    print(isExist)
    print(path2)
except OSError as err:
    print(err)

for pic in os.listdir(path1):
    img = Image.open(f'{path1}{pic}')
    clean_name = os.path.splitext(pic)
    # print(clean_name)
    img.save(f'{path2}{clean_name}.png', 'png')
    print('all done')

    # loop through Pokedex folder
    # convert image to png
    # save to the new folder
