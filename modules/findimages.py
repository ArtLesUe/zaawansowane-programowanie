import os

from modules.processimages import detect_persons_in_image, detect_persons_in_image_with_time


def find_and_process_images() -> None:
    filelist = os.listdir('images')
    for image in filelist:
        detect_persons_in_image("images/" + image)
        detect_persons_in_image_with_time("images/" + image)