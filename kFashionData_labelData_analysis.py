import numpy as np
import matplotlib.pyplot as plt
import cv2
import json
from os import listdir


def showDict(dict):
    for key in dict.keys():
        print(key, " : ", dict[key])

path = "./label/"
directory_list = listdir(path)
directory_list.remove('.DS_Store')
print ("file_list: {}".format(directory_list))
#label_name = "label/" + file_name + ".json"

elementCountSet = set()
styleDict = {}
outerDict = {}
pantsDict = {}
onePieceDict = {}
topDict = {}

for directory in directory_list:
    dir_path = path + directory + "/"
    file_list = listdir(dir_path)
    print("file list : ", file_list)

    # 각 파일들을 열어 라벨링 데이터만 가져옴
    for i in range(len(file_list)):
        now_file_path = dir_path + file_list[i]
        print("now file path: ", now_file_path)
        with open(now_file_path, "r", encoding='utf8') as f:
            # 하나의 label파일을 받아온 것
            data = json.load(f)
            elementCountSet.add(len(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['스타일']))
            # print(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['스타일'])
            # print(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['아우터'])

            for key in data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['아우터'][0].keys():
                # print("지금 key : ", data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['아우터'][0][key])
                now_value = data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['아우터'][0][key]
                if type(now_value) == list:
                    now_value = tuple(now_value)

                if outerDict.get(key) == None:
                    outerDict[key] = set(now_value)
                else:
                    outerDict[key].add(now_value)

            # print(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['하의'])
            for key in data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['하의'][0].keys():
                # print("지금 key : ", data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['하의'][0][key])
                now_value = data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['하의'][0][key]
                if type(now_value) == list:
                    now_value = tuple(now_value)

                if pantsDict.get(key) == None:
                    pantsDict[key] = set(now_value)
                else:
                    pantsDict[key].add(now_value)

            # print(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['원피스'])
            for key in data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['원피스'][0].keys():
                # print("지금 key : ", data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['원피스'][0][key])
                now_value = data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['원피스'][0][key]
                if type(now_value) == list:
                    now_value = tuple(now_value)

                if onePieceDict.get(key) == None:
                    onePieceDict[key] = set(now_value)
                else:
                    onePieceDict[key].add(now_value)

            # print(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['원피스'])
            for key in data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['상의'][0].keys():
                # print("지금 key : ", data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['상의'][0][key])
                now_value = data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['상의'][0][key]
                if type(now_value) == list:
                    now_value = tuple(now_value)

                if topDict.get(key) == None:
                    topDict[key] = set(now_value)
                else:
                    topDict[key].add(now_value)

print()
print(" =========****========== 아우터 =========****==========")
print()
showDict(outerDict)
print()
print(" =========****========== 하의 =========****==========")
print()
showDict(pantsDict)
print()
print(" =========****========== 원피스 =========****==========")
print()
showDict(onePieceDict)
print()
print(" =========****========== 상의 =========****==========")
print()
showDict(topDict)


            # print(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['원피스'])
            # print(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']['상의'])

exit(0)


with open(label_name, "r", encoding='utf8') as f:
    data = json.load(f)
    print(len(data))
    print(data.keys())
    print(data['이미지 정보'])
    print(len(data['데이터셋 정보'].keys()))
    print(data['데이터셋 정보'].keys())
    print("-----")
    print("파일 생성일자 = ", data['데이터셋 정보']['파일 생성일자'])
    print("파일 번호 = ",data['데이터셋 정보']['파일 번호'])
    print("파일 이름 = ", data['데이터셋 정보']['파일 이름'])
    print("-------------------")
    print("데이터셋정보 -> 데이터셋 상세설명 key들 = ", data['데이터셋 정보']['데이터셋 상세설명'].keys())
    # print(data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표'].keys())
    # print(data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표'])
    # print(data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표']['상의'])
    # print(data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표']['상의'][0])

    # x1 = int(data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표']['아우터'][0]['X좌표'])
    # y1 = int(data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표']['아우터'][0]['Y좌표'])
    # x2 = int(x1 + data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표']['아우터'][0]['가로'])
    # y2 =int(y1 + data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표']['아우터'][0]['세로'])
    # cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
    plotRect(image, data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표'])
    print("------------------ 폴리곤 좌표 -----------------")
    # print(data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표'].keys())
    # # print(data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표'])
    # print(data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표']['아우터'])
    # print(len(data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표']['아우터']))
    # print(len(data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표']['아우터'][0]))
    # print(data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표']['아우터'][0].keys())
    drawClothesPoly(image, data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표'])




#
# ## 렉트좌표 dictionary & 이미지를 매개변수로 전달해주어, 해당 이미지 위에 Rect를 그려줌
# # 아우터 : Red
# # 하의 : Blue
# # 원피스 : Green
# # 상의 : Yellow
# def plotRect(image, rect_dict):
#     for i in rect_dict.values():
#         # 각각이 dictionary임
#         for j in i:
#             if len(j) == 0:
#                 continue
#             x1 = int(j['X좌표'])
#             y1 = int(j['Y좌표'])
#             x2 = int(x1 + j['가로'])
#             y2 = int(y1 + j['세로'])
#             cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
# #dictionary에 담긴 옷 윤곽을 array형태로 반환. (점 갯수, 2)의 shape을 갖도록.
# def polyPoints_dictToArray(pointDict):
#     num_point = len(pointDict) // 2
#     polyPoints = np.array([], dtype=int)
#     for i in range(1, num_point + 1):
#         x = pointDict["X좌표"+str(i)]
#         polyPoints = np.append(polyPoints, np.array([int(pointDict["X좌표"+str(i)]), int(pointDict["Y좌표"+str(i)])]))
#     return polyPoints.reshape(num_point, 2)
#
# # 폴리곤좌표 데이터를 넘겨주면, 이미지 위에 모든 폴리곤좌표들을 그려주는 함수
# def drawClothesPoly(image, poly_dict):
#     for i in poly_dict.values():
#         for j in i:
#             if len(j) == 0:
#                 continue
#             arr_polyPoints = polyPoints_dictToArray(j)
#         image = cv2.polylines(image, [arr_polyPoints], True, (0, 0, 255), 2)
#
# print("lslsl")
# file_name = "mannish/223"
# # 원본 color image
# image_base = cv2.imread("images/" + file_name + ".jpg")
# label_name = "label/" + file_name + ".json"
# #Change channel BGR to RGB
# image = cv2.cvtColor(image_base, cv2.COLOR_BGR2RGB)
#
#
# # data는 '이미지 정보', '데이터셋 정보' 두 개의 키를 가지고있고,
# # '이미지 정보'는 '이미지 식별자', '이미지 높이', '이미지 파일명', '이미지 너비' 총 4개의 key를 갖고있다.
# # '데이터셋 정보'는 '파일 생성일자', '데이터셋 상세설명', '파일 번호', '파일 이름' 총 4개의 key를 갖고있다.
#
# with open(label_name, "r", encoding='utf8') as f:
#     data = json.load(f)
#     print(len(data))
#     print(data.keys())
#     print(data['이미지 정보'])
#     print(len(data['데이터셋 정보'].keys()))
#     print(data['데이터셋 정보'].keys())
#     print("-----")
#     print("파일 생성일자 = ", data['데이터셋 정보']['파일 생성일자'])
#     print("파일 번호 = ",data['데이터셋 정보']['파일 번호'])
#     print("파일 이름 = ", data['데이터셋 정보']['파일 이름'])
#     print("-------------------")
#     print("데이터셋정보 -> 데이터셋 상세설명 key들 = ", data['데이터셋 정보']['데이터셋 상세설명'].keys())
#     # print(data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표'].keys())
#     # print(data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표'])
#     # print(data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표']['상의'])
#     # print(data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표']['상의'][0])
#
#     # x1 = int(data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표']['아우터'][0]['X좌표'])
#     # y1 = int(data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표']['아우터'][0]['Y좌표'])
#     # x2 = int(x1 + data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표']['아우터'][0]['가로'])
#     # y2 =int(y1 + data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표']['아우터'][0]['세로'])
#     # cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
#     plotRect(image, data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표'])
#     print("------------------ 폴리곤 좌표 -----------------")
#     # print(data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표'].keys())
#     # # print(data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표'])
#     # print(data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표']['아우터'])
#     # print(len(data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표']['아우터']))
#     # print(len(data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표']['아우터'][0]))
#     # print(data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표']['아우터'][0].keys())
#     drawClothesPoly(image, data['데이터셋 정보']['데이터셋 상세설명']['폴리곤좌표'])
#
# plt.imshow(image)
# plt.show()


# print("------------------ 라벨링 -----------------")
# print(len(data['데이터셋 정보']['데이터셋 상세설명']['라벨링']))
# print(data['데이터셋 정보']['데이터셋 상세설명']['라벨링'])
# print(data['데이터셋 정보']['데이터셋 상세설명']['라벨링'].keys())
