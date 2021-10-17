"""
shyam gupta
"""
import os

import cv2
import numpy as np
import matplotlib.pyplot as plt

if not os.path.exists('uploads'):
    os.mkdir('uploads')
if not os.path.exists('uploads/transformed/'):
    os.mkdir('uploads/transformed/')


def reader(name):
    img = cv2.imread(name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(img)
    # plt.show()
    return img


# trying to increase the edge marks


def edge_mask(img, line_size, blur_value):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray_blur = cv2.medianBlur(gray, blur_value)

    edges = cv2.adaptiveThreshold(
        gray_blur,
        255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        line_size,
        blur_value,
    )

    return edges


# reducing color palette using kmeans


def color_reduction(img, k):
    # transform the image
    print(type(img))
    data = np.float32(img).reshape((-1, 3))
    # determine the criteria

    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

    # implementing k - means
    ret, label, center = cv2.kmeans(
        data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS
    )
    center = np.uint8(center)

    result = center[label.flatten()]
    result = result.reshape(img.shape)
    return result


template_path = r"uploads/transformed/"


def main(img, filename: str, k=5, title=None):
    # img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    red_image = color_reduction(img, k=int(k))
    path = os.path.join(template_path, filename)
    cv2.imwrite(path, red_image)
    return red_image, path
