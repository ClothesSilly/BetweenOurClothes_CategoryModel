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
category_detial_dict = ["탑", "브라탑","티셔츠","셔츠","후드티","블라우스","니트웨어","조거팬츠","청바지","팬츠","래깅스","스커트","패딩","베스트","코트","가디건","재킷","짚업","점퍼","점프수트","드레스"]
final_result = [0] * 21

for style_folder in file_list:

    if style_folder == ".DS_Store":
        continue

    now_style_folder_path = path_dir + style_folder +"/"
    for file_name in os.listdir(now_style_folder_path):
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
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["하의"][0]) != 0:
            count += 1
            check[1] = True
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["아우터"][0]) != 0:
            count += 1
            check[2] = True
        if len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["원피스"][0]) != 0:
            count += 1
            check[3] = True

        # 일단 상/하의/아우터/원피스 중 한가지만 이미지에 존재하는 이미지들만 가져올 것임. 그래야 학습에 유리하므로.
        # 즉, count가 1인 것만 가져올 것임
        if count == 1:
            #print([len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["상의"][0]), len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["하의"][0]),len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["아우터"][0]),len(data["데이터셋 정보"]["데이터셋 상세설명"]["렉트좌표"]["원피스"][0])])
            now_true_idx = check.index(True)
            #상/하의/아우터/원피스
            now_category_main = category[now_true_idx]

            if data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"][now_category_main][0].get("카테고리") != None:
                now_category_detail = data["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"][now_category_main][0].get("카테고리")
                #각 카테고리 별 10000개씩만 가져오도록
                if final_result[category_detial_dict.index(now_category_detail)] >= 5000:
                    continue
                final_result[category_detial_dict.index(now_category_detail)] += 1
                # json 파일 복사
                shutil.copyfile(now_style_folder_path + file_name, base_dir + "21카테고리/" + now_category_detail + "/label/" + file_name)
                # 이미지 파일 복사
                shutil.copyfile(base_dir + style_folder + "/" + file_name_num + ".jpg", base_dir + "21카테고리/" + now_category_detail + "/image/" + file_name_num + ".jpg")

