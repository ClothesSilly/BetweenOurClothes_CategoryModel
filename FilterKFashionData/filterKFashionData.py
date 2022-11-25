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
#상->하->아우터->원피스
final_result = [0,0,0,0]
now_style_dir_count = 0

for style_folder in file_list:

    if style_folder == ".DS_Store":
        continue
    now_style_dir_count += 1500

    now_style_folder_path = path_dir + style_folder +"/"
    for file_name in os.listdir(now_style_folder_path):
        #### final_result 확인하기
        if sum(final_result) % 1000 == 0:
            print("final_result 중간점검 : ", final_result)
        #.json을 제외한 파일 이름 숫자
        file_name_num = file_name.split(".")[0]
        #현재의 json 파일 open
        file = open(now_style_folder_path + file_name)
        data = json.load(file)
        count = 0
        check = [False, False, False, False]

        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["상의"][0]) != 0:
            count += 1
            check[0] = True
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["하의"][0]) != 0:
            count += 1
            check[1] = True
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["아우터"][0]) != 0:
            count += 1
            check[2] = True
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["원피스"][0]) != 0:
            count += 1
            check[3] = True

        if count == 1:
            #print([len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["상의"][0]), len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["하의"][0]),len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["아우터"][0]),len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["원피스"][0])])
            now_true_idx = check.index(True)
            now_category = category[now_true_idx]
            if final_result[now_true_idx] >= now_style_dir_count:
                continue
            final_result[now_true_idx] += 1
            # json 파일 복사
            shutil.copyfile(now_style_folder_path + file_name, base_dir + now_category + "/label/" + file_name)
            # 이미지 파일 복사
            shutil.copyfile(base_dir + style_folder + "/" + file_name_num + ".jpg", base_dir + now_category + "/image/" + file_name_num + ".jpg")

print("최종 갯수 상/하/아우터/원피스")
print(final_result)