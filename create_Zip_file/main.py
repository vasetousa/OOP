import zipfile

# my_zipfile = zipfile.ZipFile("files.zip", "w")
# my_zipfile.write("back.jpg")
# my_zipfile.write("face.jpg")
# my_zipfile.write("where_are_the_bodies.jpg")
#
# my_zipfile.close()

# with zipfile.ZipFile("files.zip", "w") as my_zipfile:
#     my_zipfile.write("back.jpg")
#     my_zipfile.write("face.jpg")
#     my_zipfile.write("where_are_the_bodies.jpg")
#
""" with compression """
# with zipfile.ZipFile("files.zip", "w", compression=zipfile.ZIP_DEFLATED) as my_zipfile:
#     my_zipfile.write("back.jpg")
#     my_zipfile.write("face.jpg")
#     my_zipfile.write("where_are_the_bodies.jpg")

""" Zip entire directory """
import shutil

# shutil.make_archive('another', 'zip', 'files')    # formats other than zip -> tar, gztar, bztar, xztar
# shutil.unpack_archive('another.zip', 'another')

""" Download zip online and unzip it """

import requests

req = requests.get('https://drive.google.com/uc?export=download&id=1QOmVDpd8hcVYqqUXDXf68UMDWQZP0wQV')
with open('data.zip', 'wb') as f:
    f.write(req.content)

with zipfile.ZipFile('data.zip', 'r') as data_zip:
    print(data_zip.namelist())



# https://youtu.be/z0gguhEmWiY