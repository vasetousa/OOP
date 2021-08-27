import zipfile

# """ with compression """
# with zipfile.ZipFile("files.zip", "w", compression=zipfile.ZIP_DEFLATED) as my_zipfile:
#     my_zipfile.write("back.jpg")
#     my_zipfile.write("face.jpg")
#     my_zipfile.write("where_are_the_bodies.jpg")


with zipfile.ZipFile("files.zip", "r") as my_zipfile:
    """ just to see the files in the Zip """
    print(my_zipfile.namelist())
    my_zipfile.extractall('files')




# https://youtu.be/z0gguhEmWiY