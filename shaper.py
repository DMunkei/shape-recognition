import cv2
import numpy as np

def label_shape(label, x_offset = 30, y_offset = -10):
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    cv2.putText(img, label, (x + x_offset, y + y_offset), font, 1, (0))

font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.imread('shapes.png', cv2.IMREAD_GRAYSCALE)
_, threshold = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    cv2.drawContours(img, [approx], 0, (0), 5)

    if len(approx) == 4:
        label_shape("square")
    elif len(approx) == 5:
        label_shape("pentagon", y_offset=-65)
    elif len(approx) == 6:
        label_shape("hexagon", x_offset=-10)
    elif len(approx) == 10:
        label_shape("star",x_offset=55, y_offset=-75)
    print(len(approx))
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
#
# corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# corners = np.int0(corners)
#
# for index,corner in enumerate(corners):
#     print(index)
#     x, y = corner.ravel()
#     cv2.circle(img, (x, y), 3, 255, -1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()