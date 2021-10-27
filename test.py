import numpy as np
import cv2

img = cv2.imread("./chara.png",cv2.IMREAD_UNCHANGED)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destoryAllWindows()

