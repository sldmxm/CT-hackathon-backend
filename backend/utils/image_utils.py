from PIL import Image

import backend.constants as constants


def resize_image(image_path):
    img = Image.open(image_path)
    if (
            img.height > constants.SMALL_IMAGE_SIZE
            or img.width > constants.SMALL_IMAGE_SIZE
    ):
        img.thumbnail(
            (constants.SMALL_IMAGE_SIZE,
             constants.SMALL_IMAGE_SIZE)
        )
        img.save(image_path)
