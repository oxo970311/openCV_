import cv2
import numpy as np


# 이미지 및 동영상 읽기

path = "../img/img.jpg"    # 경로 지정
img = cv2.imread(path)     # cv2.imread 호출 -> 경로의 이미지를 img 변수에 할당
cv2.imshow(img)            # cv2.imshow 호출 -> img 변수에 할당된 이미지를 보여줌

cv2.waitKey(0)              # mm 초 만큼 화면을 유지
cv2.destroyAllWindows()    # 창 모두 닫기

cap = cv2.VideoCapture(0)  # cv2.VideoCapture 객체 생성 (웹캠 : 0)
cap.isOpened()             # 객체 연결 확인
ret, frame = cap.read()    # cv2.read 는 2개의 값을 반환함
                           # ret = 성공, 실패 여부 boolean type : True, False 를 반환
                           # frame = 동영상 데이터를 가지고 있음


# 관심 영역(ROI) 표시

img = cv2.imread('../img/sunset.jpg')

x=320; y=150; w=50; h=50    # roi 좌표
roi = img[y:y+h, x:x+w]     # roi 지정

print(roi.shape)
cv2.rectangle(roi, (0,0), (h-1, w-1), (0,255,0)) # roi 전체에 사각형 그리기
cv2.imshow("img", img)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()


# 이미지 색상 바꾸기

img = cv2.imread('road.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 그레이 변환 다른 변환 생각 예시 cv2.COLOR_ ...
                                              # GRAY2BGR GRAY -> BGR
                                              # BGR2RGB BGR -> RGB
                                              # BGR2HSV BGR -> HSV
                                              # HSV2BGR HSV -> BGR
                                              # BGR2YUV BGR -> YUV
                                              # YUV2BGR YUV -> BGR ...

cv2.imwrite('gray_road.jpg', gray)  # 저장


# 흐림/에지/필터 등 기본이미지 처리

blur = cv2.GaussianBlur(img, (5, 5), 0)    # 5x5 커널 만큼 블러를 적용
edges = cv2.Canny(img, 50, 150)            # 엣지 추출
cv2.imshow('Edges', edges)