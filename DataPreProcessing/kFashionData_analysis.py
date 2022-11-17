import numpy as np
import matplotlib.pyplot as plt
import cv2
import json

## 렉트좌표 dictionary & 이미지를 매개변수로 전달해주어, 해당 이미지 위에 Rect를 그려줌
# 아우터 : Red
# 하의 : Blue
# 원피스 : Green
# 상의 : Yellow
def plotRect(image, rect_dict):
    for i in rect_dict.values():
        # 각각이 dictionary임
        for j in i:
            if len(j) == 0:
                continue
            x1 = int(j['X좌표'])
            y1 = int(j['Y좌표'])
            x2 = int(x1 + j['가로'])
            y2 = int(y1 + j['세로'])
            cv2.rectangle(image, (x1, y1), (x2, y2), (255, 0, 0), 2)
#dictionary에 담긴 옷 윤곽을 array형태로 반환. (점 갯수, 2)의 shape을 갖도록.
def polyPoints_dictToArray(pointDict):
    num_point = len(pointDict) // 2
    polyPoints = np.array([], dtype=int)
    for i in range(1, num_point + 1):
        x = pointDict["X좌표"+str(i)]
        polyPoints = np.append(polyPoints, np.array([int(pointDict["X좌표"+str(i)]), int(pointDict["Y좌표"+str(i)])]))
    return polyPoints.reshape(num_point, 2)

# 폴리곤좌표 데이터를 넘겨주면, 이미지 위에 모든 폴리곤좌표들을 그려주는 함수
def drawClothesPoly(image, poly_dict):
    for i in poly_dict.values():
        for j in i:
            if len(j) == 0:
                continue
            arr_polyPoints = polyPoints_dictToArray(j)
        image = cv2.polylines(image, [arr_polyPoints], True, (0, 0, 255), 2)

print("lslsl")
file_name = "mannish/223"
# 원본 color image
image_base = cv2.imread("images/" + file_name + ".jpg")
label_name = "label/" + file_name + ".json"
#Change channel BGR to RGB
image = cv2.cvtColor(image_base, cv2.COLOR_BGR2RGB)


# data는 '이미지 정보', '데이터셋 정보' 두 개의 키를 가지고있고,
# '이미지 정보'는 '이미지 식별자', '이미지 높이', '이미지 파일명', '이미지 너비' 총 4개의 key를 갖고있다.
# '데이터셋 정보'는 '파일 생성일자', '데이터셋 상세설명', '파일 번호', '파일 이름' 총 4개의 key를 갖고있다.

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

plt.imshow(image)
plt.show()

