import pandas as pd
import os
from PIL import Image
from PIL import ImageFile
def main():
    os.chdir("../csv")
    # df1 = pd.read_csv("train_val_list.csv")
    # train_df = df1[(df1['No Finding'] == 1)]
    # train_df.to_csv('train.csv')

    train = pd.read_csv("train.csv")
    # female_train_df = train[(train['Patient Gender'] == 'F')]
    # female_train_df.to_csv('train_female.csv')
    # male_train_df = train[(train['Patient Gender'] == 'M')]
    # male_train_df.to_csv('train_male.csv')
    pa_train_df = train[(train['View Position'] == 'PA')]
    pa_train_df.to_csv('train_pa.csv')
    ap_train_df = train[(train['View Position'] == 'AP')]
    ap_train_df.to_csv('train_ap.csv')
    # df2 = pd.read_csv('test_list.csv')
    # test_df = df2[(df2['No Finding'] == 0)]
    # test_df.to_csv('test.csv')

    path = "../images"
    images = []
    for file in os.listdir(path):
        if file.lower().endswith(".png"):
            images.append(file)

    # df3 = pd.read_csv('train.csv')
    # df4 = pd.read_csv('test.csv')

    # df5 = pd.read_csv('train_female.csv')
    # df6 = pd.read_csv('train_male.csv')

    df7 = pd.read_csv('train_pa.csv')
    df8 = pd.read_csv('train_ap.csv')

    ImageFile.LOAD_TRUNCATED_IMAGES = True

    # train_female_image_names = df5['Image Index']
    # train_male_image_names = df6['Image Index']
    # train_female_images = []
    # train_male_images = []

    # train_image_names = df3['Image Index']
    # test_image_names = df4['Image Index']
    # train_images = []
    # test_images = []

    train_pa_image_names = df7['Image Index']
    train_ap_image_names = df8['Image Index']
    train_pa_images = []
    train_ap_images = []

    # for i in range(len(train_female_image_names)):
    #     train_female_images.append(train_female_image_names[i])
    # for j in range(len(train_male_image_names)):
    #     train_male_images.append(train_male_image_names[j])
    # for i in range(len(train_image_names)):
    #     train_images.append(train_image_names[i])
    # for j in range(len(test_image_names)):
    #     test_images.append(test_image_names[j])

    for i in range(len(train_pa_image_names)):
        train_pa_images.append(train_pa_image_names[i])
    for j in range(len(train_ap_image_names)):
        train_ap_images.append(train_ap_image_names[j])

    # trainFolderName = '../data/train/'
    # testFolderName = '../data/test/'

    # trainFemaleFolderName = '../data/train/female/'
    # trainMaleFolderName = '../data/train/male/'

    trainPAFolderName = '../data/train2/pa/'
    trainAPFolderName = '../data/train2/ap/'

    # if not os.path.exists(trainFolderName):
    #     os.makedirs(trainFolderName)
    # if not os.path.exists(testFolderName):
    #     os.makedirs(testFolderName)

    # if not os.path.exists(trainFemaleFolderName):
    #     os.makedirs(trainFemaleFolderName)
    # if not os.path.exists(trainMaleFolderName):
    #     os.makedirs(trainMaleFolderName)

    if not os.path.exists(trainPAFolderName):
        os.makedirs(trainPAFolderName)
    if not os.path.exists(trainAPFolderName):
        os.makedirs(trainAPFolderName)

    # for train_image in train_images:
    #     img = Image.open('../images/' + train_image)
    #     img = img.save(trainFolderName + train_image)

    # for train_female_image in train_female_images:
    #     img = Image.open('../images/' + train_female_image)
    #     img = img.save(trainFemaleFolderName + train_female_image)

    for train_pa_image in train_pa_images:
        img = Image.open('../images/' + train_pa_image)
        img = img.save(trainPAFolderName + train_pa_image)

    # for test_image in test_images:
    #     img = Image.open('../images/' + test_image)
    #     img = img.save(testFolderName + test_image)

    # for train_male_image in train_male_images:
    #     img = Image.open('../images/' + train_male_image)
    #     img = img.save(trainMaleFolderName + train_male_image)

    for train_ap_image in train_ap_images:
        img = Image.open('../images/' + train_ap_image)
        img = img.save(trainAPFolderName + train_ap_image)
if __name__ == '__main__':
    main()