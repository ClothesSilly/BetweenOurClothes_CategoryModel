# 로컬의 imageset을 npz로 저장해주는 프로그램

import os
import glob
import cv2
import numpy as np


# 가로는 모든 이미지가 800인 듯 하지만, 세로크기가 800이 아닌 image가 종종 있으므로
# 이를 800으로 수정해주는 함수
def adjust_size_800(image):
    if image.shape[0] < 800:
        zeros = np.zeros((800 - image.shape[0], 800, 3))
        image = np.vstack((image, zeros))
    elif image.shape[0] > 800:
        image = image[:800, :, :]

    if image.shape[1] < 800:
        zeros = np.zeros((800, 800 - image.shape[1], 3))
        image = np.hstack((image, zeros))
    elif image.shape[1] > 800:
        image = image[:, :800, :]
    return image

path_dir = "/Users/ymp/Desktop/KFashionImage/Training/20color/"
file_list = os.listdir(path_dir)
# 라벨 데이터를 one-hot encoding형태로 구성해줘야하기 때문에 순서대로 list에 작성해준다
label_list = ["블랙", "화이트", "그레이","레드", "핑크","오렌지","베이지","브라운","옐로우","그린","카키","민트","블루","네이비","스카이블루","퍼플","라벤더","와인","네온","골드"]

#
image_train = []
label_train = []

# test
image_test = []
label_test = []

#folder는 label_list값들이 차례로 나오게 된다.
for folder in file_list:
    if folder == ".DS_Store":
        continue

    now_folder_image_path = path_dir + folder + "/image/"
    now_folder_label_path = path_dir + folder + "/label/"

    # 이미지 데이터를 train, test로 나누어 저장 7:3
    now_folder_image_list = os.listdir(now_folder_image_path)
    now_folder_image_list_num = len(os.listdir(now_folder_image_path))

    for idx, file_name in enumerate(now_folder_image_list):
        print(idx)
        if file_name == ".DS_Store":
            continue

        now_file = now_folder_image_path + file_name
        image = cv2.imread(now_file,cv2.IMREAD_COLOR)
        #사이즈를 (800, 800, 3)으로 확정
        image = adjust_size_800(image)
        image = list(image)

        # 나누어 train과 test에 이어붙임
        if idx < (now_folder_image_list_num * 7) // 10:
            image_train.append(image)
        else:
            image_test.append(image)

    break
#npz로 저장하기 전에 numpy array로 변환
image_train = np.array(image_train)
label_train = np.array(label_train)

image_test = np.array(image_test)
label_test = np.array(label_test)
print(image_train.shape, image_test.shape)

        # print(len(image_train))
        # s = np.array(image_train)
        # print(s.shape)


        # cv2.imshow("ll",image)
        # cv2.waitKey(0)
        #print(file_name)




