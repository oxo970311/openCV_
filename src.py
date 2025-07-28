import cv2

print("OpenCV version:", cv2.__version__)


path = "img/like_lenna.png"
path2 = "img/pepe.png"

lenna = cv2.imread(path)
pepe = cv2.imread(path2)

print(lenna.shape); print(pepe.shape)

r_lenna = cv2.resize(lenna, (200,200))
r_pepe = cv2.resize(pepe,(r_lenna.shape[0],r_lenna.shape[1]))


print(r_lenna.shape); print(r_pepe.shape)

alpha = 0.6
beta = 0.9

pepe_man = cv2.addWeighted(r_lenna, alpha, r_pepe, beta, 0)
cv2.imshow("pepe_man", pepe_man)

cv2.waitKey(0)
cv2.destroyAllWindows()