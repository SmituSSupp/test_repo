a = 1+1
import json
import scipy.io
import cv2

mat2 = scipy.io.loadmat('mall_gt.mat')


imagePath = 'seq_000013.jpg'
image = cv2.imread('seq_000013.jpg')
print('new')

for item in mat2['frame'][0][12][0][0][0]:
    x_cor = int(round(item[0]))
    y_cor = int(round(item[1]))
    if (x_cor - 9) < 0:
	    x1 = 0
    else:
	    x1 = x_cor-9
    if (y_cor - 9) < 0:
	    y1 = 0
    else:
	    y1 = y_cor-9
    print((x_cor,y_cor))
    low_c = (x1, y1)
    high_c = (x_cor+9, y_cor+9)
    cv2.rectangle(image, low_c, high_c, (0, 255, 0), 1)
    
cv2.imshow("Faces found", image)
    
cv2.imshow("Faces found", image)
cv2.waitKey(0)