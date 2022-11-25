"""
오류없이 끝까지 돌아간 결과

"""
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
#아우터
length_dict = ["미니", "니렝스","미디", "발목", "맥시"]
final_result = [0] * 5

for style_folder in file_list:

    if style_folder == ".DS_Store":
        continue

    now_style_folder_path = path_dir + style_folder +"/"
    for file_name in os.listdir(now_style_folder_path):
        if file_name == ".DS_Store":
            continue
        if sum(final_result) % 1000 == 0:
            print(final_result)
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
            continue

        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["하의"][0]) != 0:
            count += 1
            check[1] = True
            continue
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["아우터"][0]) != 0:
            count += 1
            check[2] = True
            continue

        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["원피스"][0]) != 0:
            count += 1
            check[3] = True

        # 일단 상/하의/아우터/원피스 중 한가지만 이미지에 존재하는 이미지들만 가져올 것임. 그래야 학습에 유리하므로.
        # 즉, count가 1인 것만 가져올 것임
        if count == 1:
            now_true_idx = check.index(True)
            #상/하의/아우터/원피스
            now_category_main = category[now_true_idx]

            if now_category_main != "원피스":
                continue

            if data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"][now_category_main][0].get("기장") != None:
                now_fit = data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"][now_category_main][0].get("기장")

                # if now_material not in material_dict:
                #     continue
                #각 카테고리 별 10000개씩만 가져오도록
                if final_result[length_dict.index(now_fit)] >= 10000:
                    continue
                final_result[length_dict.index(now_fit)] += 1
                # json 파일 복사
                shutil.copyfile(now_style_folder_path + file_name, base_dir + "5length_onepiece/" + now_fit + "/label/" + file_name)
                # 이미지 파일 복사
                shutil.copyfile(base_dir + style_folder + "/" + file_name_num + ".jpg", base_dir + "5length_onepiece/" + now_fit + "/image/" + file_name_num + ".jpg")

