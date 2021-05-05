#!/usr/bin/python3

# Copyright 2021 Melwyn Francis Carlo

import sys
from PIL import Image

n = len(sys.argv)

img_list = []
img01 = Image.open(sys.argv[1], mode='r').convert('RGB')

for i in range(2, n):
    img_list.append(Image.open(sys.argv[i], mode='r').convert('RGB'))

img01.save(r'img2pdf.pdf',save_all=True, append_images=img_list)

