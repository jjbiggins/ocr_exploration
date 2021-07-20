#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import pytesseract
from PIL import Image

def process_image(iamge_name, lang_code):
    print("got here")
    return pytesseract.image_to_string(Image.open(iamge_name), lang=lang_code)

def print_data(data):
    print(data)

def output_file(**kwargs):
    with open(kwargs.get("filename"), "w+") as ofile:
        ofile.write(kwargs.get("data"))

def main():
    data_eng = process_image("./test_image.png", "eng")
    print_data(data_eng)
    output_file(filename="eng.txt", data=data_eng)


if __name__ == "__main__":
    main()
