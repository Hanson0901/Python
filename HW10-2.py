import numpy as np
import matplotlib.pyplot as plt

Q1 = 1  #Q1的電荷量
Q2 = -1  #Q2的電荷量
k = 1   #庫倫常數
x1 = 30  #Q1的x座標
y1 = 0  #Q1的y座標
x2 = -30  #Q2的x座標
y2 = 0  #Q2的y座標

def V(x,y): #電位
    V1 = k*Q1/np.sqrt((x-x1)**2 + (y-y1)**2) + k*Q2/np.sqrt((x-x2)**2 + (y-y2)**2)
    return  V1

#利用linspace語法產生1D-array(陣列)
x = np.linspace(-50,50,50) 
y = np.linspace(-50,50,50)

#利用meshgrid語法產生2D-array，可簡單想成x-y平面上的網格
X,Y = np.meshgrid(x,y)


plt.figure(figsize=(12,10))     #設定圖表大小
equal_V = plt.contourf(X, Y, V(X, Y),levels = np.linspace(-0.1,0.1,21),cmap = plt.cm.bwr)   #繪製等高線圖
C = plt.contour(X, Y, V(X, Y), levels = np.linspace(-0.1,0.1,21), colors='black')
plt.clabel(C, inline=True, fontsize=10)

plt.scatter(x1,y1,s=100,color = "red")  #加入Q1電荷位置
plt.scatter(x2,y2,s=100,color = "blue")  #加入Q2電荷位置
plt.annotate('Q1', (x1+1, y1+1))
plt.annotate('Q2', (x2+1, y2+1))

plt.colorbar(equal_V)  #於圖表顯示色塊數值
plt.show()