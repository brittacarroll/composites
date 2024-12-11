from PIL import Image
import pdb
import os
import re

# path to composites folder
path = "/Users/britta/Desktop/Pfizer CCCA pictures/Composites/Vimentin Composites"
stain = 'VIM'
patientList = [
    "CA-03",
    "CA-07",
    "CA-17",
    "CA-18",
    "CA-19",
    "CA-20",
    "CA-21",
    "CA-22",
    "CA-23",
    "CA-24",
    "CA-25",
    "CA-26",
    "CA-27",
    "CA-28",
    "CA-29",
    "CA-31",
    "CA-32",
    "CA-33",
    "CA-34",
    "CA-35",
    "CA-36",
    "CA-37",
    "CA-38",
    "CA-39",
    "CA-40",
    "CA-41",
    "CA-42",
    "CA-43",
    "CA-44",
    "CA-45",
    "CA-46",
    "CA-47",
    "CA-48",
    "CA-49",
    "CA-50",
    "CON079"

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

    final_composite.save(f"{path}/Vimentin collage of composites/{patient} {stain}.png")

def main():
    find_patient_files()

if __name__ == '__main__':
    main()
