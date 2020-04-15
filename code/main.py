import pandas as pd
import os
from PIL import Image
import PIL

def main():
    os.chdir("../csv")
    df1 = pd.read_csv("train_val_list.csv")
    train_df = df1[(df1['No Finding'] == 1)]
    train_df.to_csv('train.csv')

    df2 = pd.read_csv('test_list.csv')
    test_df = df2[(df2['No Finding'] == 0)]
    test_df.to_csv('test.csv')

    path = "../images"
    images = []
    for file in os.listdir(path):
        if file.lower().endswith(".png"):
            images.append(file)

    df3 = pd.read_csv('train.csv')
    df4 = pd.read_csv('test.csv')

    train_image_names = df3['Image Index']
    test_image_names = df4['Image Index']
    train_images = []
    test_images = []

    for i in range(len(train_image_names)):
        train_images.append(train_image_names[i])
    for j in range(len(test_image_names)):
        test_images.append(test_image_names[j])

    trainFolderName = '../data/train/'
    testFolderName = '../data/test/'

    if not os.path.exists(trainFolderName):
        os.makedirs(trainFolderName)
    if not os.path.exists(testFolderName):
        os.makedirs(testFolderName)

    for train_image in train_images:
        img = Image.open('../images/' + train_image)
        img = img.save(trainFolderName + train_image)

    for test_image in test_images:
        img = Image.open('../images/' + test_image)
        img = img.save(testFolderName + test_image)


if __name__ == '__main__':
    main()