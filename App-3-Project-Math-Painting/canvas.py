import numpy as np
from PIL import Image


class Canvas:
    def __init__(self, height, width, color):
        self.width = width
        self.height = height
        self.color = color

        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make_canvas(self, image_path):
        img = Image.fromarray(self.data, "RGB")
        img.save(image_path)