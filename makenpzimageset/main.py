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
label_list = ['black', 'white', 'gray','red', 'pink','orange','beige','brown','yellow','green','khaki','mint','blue','navy','skyblue','purple','lavender','wine','neon','gold']
# print(label_list.index("레드"))

one_hot_label = [0] * len(label_list)
#
image_train = []
label_train = []

# test
image_test = []
label_test = []

folder_count = 0

#folder는 label_list값들이 차례로 나오게 된다.
for folder in file_list:
    print(type(folder))
    if folder == ".DS_Store":
        continue
    folder_count += 1
    print(folder_count)
    print(label_list)
    # one-hot encoding형태의 label data array를 설정해준다.
    now_label_idx = label_list.index(str(folder))
    one_hot_label = [0] * len(label_list)
    one_hot_label[now_label_idx] = 1

    now_folder_image_path = path_dir + folder + "/image/"

    # 이미지 데이터를 train, test로 나누어 저장 7:3
    now_folder_image_list = os.listdir(now_folder_image_path)
    now_folder_image_list_num = len(os.listdir(now_folder_image_path))

    # 이 부분은 이미지를 나누어 저장해주면서, 어차피 들어와있는 디렉토리 파일이 label을 의미하니까 같이 append 해줌
    for idx, file_name in enumerate(now_folder_image_list):
        if idx % 100 == 0:
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
            label_train.append(one_hot_label)
        else:
            image_test.append(image)
            label_test.append(one_hot_label)

    # 이 부분에서 one-hot encoding형태로 label데이터에 채워넣어야함.


#npz로 저장하기 전에 numpy array로 변환
image_train = np.array(image_train)
label_train = np.array(label_train)

image_test = np.array(image_test)
label_test = np.array(label_test)
print(image_train.shape, label_train.shape,image_test.shape, label_test.shape)

np.savez_compressed("/Users/ymp/Desktop/KFashionImage/Training/20color/20color", image_train=image_train, label_train=label_train, image_test=image_test, label_test=label_test)



