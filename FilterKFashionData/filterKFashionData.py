import numpy as np
import sys
import os
import json
import shutil

path_dir = "/Users/ymp/Desktop/KFashionImage/Training/라벨링데이터/"
file_list = os.listdir(path_dir)

base_dir = "/Users/ymp/Desktop/KFashionImage/Training/"
count = 0
check = [False, False, False, False]
category = ["상의", "하의", "아우터", "원피스"]

for style_folder in file_list:
    now_style_folder_path = path_dir + style_folder +"/"
    for file_name in os.listdir(now_style_folder_path):
        #.json을 제외한 파일 이름 숫자
        file_name_num = file_name.split(".")[0]
        #현재의 json 파일 open
        file = open(now_style_folder_path + file_name)
        data = json.load(file)
        count = 0
        check = [False, False, False, False]

        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["상의"][0]) == 0:
            count += 1
            check[0] = True
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["하의"][0]) == 0:
            count += 1
            check[1] = True
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["아우터"][0]) == 0:
            count += 1
            check[2] = True
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["원피스"][0]) == 0:
            count += 1
            check[3] = True

        if count == 1:
            now_true_idx = check.index(True)
            now_category = category[now_true_idx]
            # json 파일 복사
            shutil.copyfile(now_style_folder_path + file_name, base_dir + now_category + "/label/" + file_name)
            # 이미지 파일 복사
            shutil.copyfile(base_dir + style_folder + "/" + file_name_num + ".jpg", base_dir + now_category + "/image/" + file_name_num + ".jpg")
            print("끝")
            exit(0)
