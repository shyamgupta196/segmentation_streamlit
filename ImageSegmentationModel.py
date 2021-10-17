"""
shyam gupta
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt


def reader(name):
    img = cv2.imread(name)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # plt.imshow(img)
    # plt.show()
    return img


# trying to imcrease the edge marks


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


# plt.imshow(image_mask,cmap='gray')
# plt.show()

# reducing color palette using kmeans


def color_red(img, k):
    # transform the image
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


def main():
    images = {}
    for i in range(1, 20):
        images[f"img{i}"] = color_red(img, k=i)

    fig = plt.figure(figsize=(30, 20))

    for i in range(1, 20):
        plt.tight_layout()
        axes = plt.subplot(4, 5, i)
        plt.suptitle("Pyari Shruti Junior Transition")
        axes.get_xaxis().set_visible(False)
        axes.get_yaxis().set_visible(False)
        axes.imshow(images[f"img{i}"])
    plt.show()
