import cv2
import dlib
import numpy as np
import sys

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./shape_predictor_68_face_landmarks.dat")
img = cv2.imread("./chara.png")

faces = detector(img)

if len(faces) == 0:
    print("no face")
    img_rec = img

for face in faces:
    img_rec = cv2.rectangle(img, pt1=(face.left(), face.top()), pt2=(face.right(), face.bottom()),color=(255, 255, 255), lineType=cv2.LINE_AA, thickness=2)
    
    dlib_shape = predictor(img,face)
    shape_2d = np.array([[p.x, p.y] for p in dlib_shape.parts()])

    print(shape_2d)

    for s in shape_2d:
        cv2.circle(img, center=tuple(s), radius=1, color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)

cv2.imshow("rec", img_rec)

#dets = detector(frame[:,:,::-1])
#if len(dets) > 0:
#    print("find")
#    parts = predictor(frame, dets[0]).parts()
#
#    img = frame * 0
#    for i in parts:
#        cv2.cicle(img, (i.x, i.y), 3, (255, 0, 0), -1)
#    cv2.imshow("test", img)
#
cv2.waitKey(0)
cv2.destroyAllWindows()
