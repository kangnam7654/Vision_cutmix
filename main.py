import cv2
import numpy as np


def cutmix(image1, label1, image2, label2):
    width = image1.shape[0]
    height = image1.shape[1]
    random_lambda = np.random.uniform(0, 1)

    random_x = np.random.uniform(0, width)
    random_y = np.random.uniform(0, height)
    random_width = width * np.sqrt(1 - random_lambda)
    random_height = height * np.sqrt(1 - random_lambda)

    x1 = np.clip(a=random_x - random_width / 2,
                 a_min=0,
                 a_max=width)
    x2 = np.clip(a=random_x + random_width / 2,
                 a_min=0,
                 a_max=width)
    y1 = np.clip(a=random_y - random_height / 2,
                 a_min=0,
                 a_max=height)
    y2 = np.clip(a=random_y + random_height / 2,
                 a_min=0,
                 a_max=height)

    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    image1[x1:x2, y1:y2, :] = image2[x1:x2, y1:y2, :]
    lambda_adjusted = 1 - (x2 - x1) * (y2 - y1) / (width * height)
    label = lambda_adjusted * label1 + (1 - lambda_adjusted) * label2
    return image1, label


if __name__ == '__main__':
    cat = cv2.imread('./data/train/cat_0.jpg')
    dog = cv2.imread('./data/train/dog_0.jpg')
    cat = cv2.resize(cat, [224, 224])
    dog = cv2.resize(dog, [224, 224])
    result, label = cutmix(cat, 1, dog, 0)
    print(label)
    cv2.imshow('result', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
