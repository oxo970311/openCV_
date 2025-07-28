import cv2
print("OpenCV version:", cv2.__version__)

path = "C:/Users/oxo97/Downloads/like_lenna.png"

img = cv2.imread(path)
cv2.imshow('lenna',img)
cv2.waitKey(0)
cv2.destroyAllWindows()