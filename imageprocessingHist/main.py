import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot as plt

#renkli goruntuyu cikti olarak veriyor
foto = cv2.imread("bina.jpg")
cv2.imshow("bina resmi", foto)


B = foto[:,:,0] #mavi
G = foto[:,:,1] #yesil
R = foto[:,:,2] #kirmizi

cv2.imshow("mavi bina", B)
cv2.imshow("yesil bina", G)
cv2.imshow("kirmizi bina", R)

cv2.waitKey()

#goruntunun yogunlugunu yazdirma

print(foto.shape)
print(R.shape)

x = 0
y = 0
kanal = 0

yogunluk_rgb = foto[y,x,kanal]
print("yogunluk= " , yogunluk_rgb)

yogunluk_r = R[y,x]
print("yogunluk_gray= ", yogunluk_r)

yogunluk_g = G[y,x]
print("yogunluk_gray2= ", yogunluk_g)

yogunluk_b = B[y,x]
print("yogunluk_gray3= ", yogunluk_b)

max_yogunluk = np.max(B)
print("max yogunluk= ", max_yogunluk)

min_yogunluk = np.min(B)
print("min yogunluk= ", min_yogunluk)

#tam koordinatın rgb degerlerini donderme

print(foto[y,x])

#parça piksel alma
parca= R[20:30,40:50]
print("parca= " ,parca)

renkli = cv2.imread("bina.jpg")
gri= cv2.imread("bina.jpg", 0 )

cv2.imshow("gri bina", gri)
histColor = cv2.calcHist(renkli, [0], None, [256], [0,256])
histGray  = cv2.calcHist(gri, [0], None, [256], [0,256])

plt.figure(2, facecolor= "purple")
plt.plot(histGray)

B = renkli[:,:,0]
hist_B = cv2.calcHist([B], [0], None, [256], [0,256])
print("numpy bilmemnesi")
print(np.sum(hist_B)) #satir ve sutunlari topluyor(mus)

plt.figure(3, facecolor= "purple")
plt.hist(gri.ravel(), 256, [0,256])
plt.show()