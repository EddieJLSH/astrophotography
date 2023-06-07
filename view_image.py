from astropy.io import fits

import numpy as np
import matplotlib.pyplot as plt

import os

def show_image(path):
    image_data = fits.getdata(path)
    plt.imshow(image_data, cmap='gray')
    plt.show()

def show_images(dir_path):
    files = [f for f in os.listdir(dir_path) if f.endswith('.FIT') or f.endswith('.fit')]
    for file in files:
        image_data = fits.getdata(file)
        plt.imshow(image_data)

    plt.show()

if __name__ == '__main__':
    show_image('./fits/M101_SN2023ixf_LRGBHa_2023/M101_Pinwheel_LIGHT_Red_300s_BIN1_-10C_001_20230521_004814_787_GA_100_OF_50_PA329_E.FIT')
    show_images('./fits/M101_SN2023ixf_LRGBHa_2023')
