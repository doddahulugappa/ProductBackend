import os
from multiprocessing import Process
from PIL import Image


def image_processing(files):
    for file in files:
        path, filename = os.path.split(file)
        name, ext = filename.split(".")

        # creating thumbnail
        new_file_name = os.path.join(path, name + "-thumb" + "." + ext)
        image = Image.open(file)
        MAX_SIZE = (100, 100)
        image.thumbnail(MAX_SIZE)
        image.save(new_file_name)

        # Creating specific full size
        new_file_name = os.path.join(path, name + "-full" + "." + ext)
        img = Image.open(file)
        MAX_SIZE = (500, 500)
        img = img.resize(MAX_SIZE, Image.ANTIALIAS)
        img.save(new_file_name)


def start_parallel_processing(files):
    p = Process(target=image_processing, args=(files,))
    p.start()

