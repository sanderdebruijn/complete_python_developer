import logging
from pathlib import Path
from PIL import Image

logging.basicConfig(level=logging.INFO)


def get_jpgs(jpg_folder):
    try:
        input_folder = Path(f"./Scripting/{jpg_folder}")
        input_files = input_folder.glob("**/*")
        files = [file for file in input_files if file.is_file() and ".jpg" in file.name]
        return files
    except Exception as e:
        print(e)


def jpg_to_png(path_to_jpg, save_folder):
    img = Image.open(path_to_jpg)
    image_name = path_to_jpg.name
    image_new_name = image_name.replace(".jpg", ".png")
    img.save(f"./Scripting/{save_folder}/{image_new_name}", "png")


if __name__ == "__main__":
    jpg_folder = input("Please provide the name of the folder with jpg images: ")
    png_folder = input("PLease provide the name of the new (png) folder: ")
    logging.info("Received input")

    # create new directory if not exists
    Path(f"./Scripting/{png_folder}").mkdir(parents=True, exist_ok=True)
    logging.info("Created new directory")

    # save files
    file_paths = get_jpgs(jpg_folder=jpg_folder)
    for file_path in file_paths:
        jpg_to_png(path_to_jpg=file_path, save_folder=png_folder)
    logging.info("Converted all jpgs")
