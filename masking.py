import cv2
import numpy as np

path = "img/lion.jpg"
lion = cv2.imread(path)

if lion is None:
    print("이미지 불러오기 실패")
    exit()

# 전체 마스크를 검정색(가림 처리)으로 초기화
mask = np.zeros_like(lion)

drawing = False  # 드래그 중 여부

# 마우스 이벤트 콜백 함수
def reveal(event, x, y, flags, param):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cv2.circle(mask, (x, y), 30, (255, 255, 255), -1)

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        cv2.circle(mask, (x, y), 30, (255, 255, 255), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.namedWindow("Scratch Off Lion")
cv2.setMouseCallback("Scratch Off Lion", reveal)

while True:
    # 매 프레임마다 마스크 적용
    revealed = cv2.bitwise_and(lion, mask)
    cv2.imshow("Scratch Off Lion", revealed)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):
        mask[:] = 0  # 'c' 누르면 다시 다 가리기

cv2.destroyAllWindows()