from PIL import Image
import pdb
import os
import re

# path to composites folder
path = "/Users/etc"

# folder wanting to keep these images in
folder = ""

# example stain
stain = 'VIM'

# subject names as titled in images
patientList = [
    "CA-03",
]

def find_patient_files():
    for patient in patientList:
        files = []
        for fname in os.listdir(path):
            tag = re.findall(f'{patient}', fname)
            if len(tag) <= 0:
                continue
            else:
                files.append(fname)
        
        if len(files) == 0:
            continue
        create_collage(files, patient)


def create_collage(files, patient):

    image = Image.open(f"{path}/{files[0]}")

    sizes = [Image.open(f"{path}/{file}", 'r').size for file in files]
    dimensions_of_largest_composite = max(sizes)

    coordinates_of_composites = {
        0: [(0,0)],
        1: [(image.width+20, 0)],
        2: [(image.width*2+40, 0)],
        3: [(image.width*3+60, 0)],
        4: [(image.width*4+80, 0)],
        5: [(image.width*5+100, 0)]
    }

    num_images = len(files)
    final_composite = Image.new("RGB", (dimensions_of_largest_composite[0]*num_images, dimensions_of_largest_composite[1]))
    files.sort()

    for index, file in enumerate(files):
        print(patient)
        try:
            composite = Image.open(f"{path}/{file}")
            final_composite.paste(composite, coordinates_of_composites[index][0])
        except:
            pdb.set_trace()

    final_composite.save(f"{path}/{folder}/{patient} {stain}.png")

def main():
    find_patient_files()

if __name__ == '__main__':
    main()
