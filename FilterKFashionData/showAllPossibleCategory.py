import sys
import os
import json
import shutil

path_dir = "/Users/ymp/Desktop/KFashionImage/Training/라벨링데이터/"
file_list = os.listdir(path_dir)

final_result_set = [set(), set(), set(), set()]

for style_folder in file_list:
    print(final_result_set)
    if style_folder == ".DS_Store":
        continue

    now_style_folder_path = path_dir + style_folder +"/"
    for file_name in os.listdir(now_style_folder_path):
        if file_name == ".DS_Store":
            continue
        #### final_result 확인하기

        #.json을 제외한 파일 이름 숫자
        file_name_num = file_name.split(".")[0]
        #현재의 json 파일 open
        file = open(now_style_folder_path + file_name)
        data = json.load(file)

        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]["상의"][0]) != 0:
            if data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]["상의"][0].get("카테고리") != None:
                final_result_set[0].add(data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]["상의"][0]["카테고리"])
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]["하의"][0]) != 0:
            if data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]["하의"][0].get("카테고리") != None:
                final_result_set[1].add(data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]["하의"][0]["카테고리"])
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]["아우터"][0]) != 0:
            if data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]["아우터"][0].get("카테고리") != None:
                final_result_set[2].add(data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]["아우터"][0]["카테고리"])
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]["원피스"][0]) != 0:
            if data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]["원피스"][0].get("카테고리") != None:
                final_result_set[3].add(data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]["원피스"][0]["카테고리"])



print(final_result_set)