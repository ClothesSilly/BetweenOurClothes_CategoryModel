# 로컬의 imageset을 npz로 저장해주는 프로그램

import os
import glob
import cv2


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

for folder in file_list:
    if folder == ".DS_Store":
        continue

    now_folder_image_path = path_dir + folder + "/image/"
    now_folder_label_path = path_dir + folder + "/label/"

    for file_name in os.listdir(now_folder_image_path):
        if file_name == ".DS_Store":
            continue
        print(file_name)

