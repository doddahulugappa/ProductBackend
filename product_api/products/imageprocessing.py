import glob
import os
from multiprocessing import Process
from PIL import Image


def image_processing(files):
    for file in files:
        path, filename = os.path.split(file)
        name, ext = filename.split(".")
        new_file_name = os.path.join(path, name + "-thumb" + "." + ext)
        # creating a object
        image = Image.open(file)
        MAX_SIZE = (100, 100)
        image.thumbnail(MAX_SIZE)

        # creating thumbnail
        image.save(new_file_name)

        new_file_name = os.path.join(path, name + "-full" + "." + ext)
        base_width = 300
        img = Image.open(file)
        width_percent = (base_width / float(img.size[0]))
        h_size = int((float(img.size[1]) * float(width_percent)))
        img = img.resize((base_width, h_size), Image.ANTIALIAS)
        img.save(new_file_name)


if __name__ == "__main__":
    file_list = glob.glob("S:/personal/Huli_Docs/Yash/*.jpg")
    p = Process(target=image_processing, args=(file_list,))
    p.start()
