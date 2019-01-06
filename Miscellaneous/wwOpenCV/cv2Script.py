import cv2

img=cv2.imread("galaxy.jpg",0)

print(type(img))
print(img.shape)
print(img.ndim)
print(img)

resized=cv2.resize(img,(1000,500))
cv2.imshow("Galaxy",img)
cv2.waitKey(0)
cv2.destroyAllWindows()