import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([2, 4, 6, 8])
y = np.array([81, 93, 91, 97])


plt.scatter(x, y) 
plt.grid()  # 격자 무늬를 만들어줍니다. 
plt.xlabel("time")  # x 축에 대하여 이름을 지어줍니다. 
plt.ylabel("score")  # y 축에 대하여 이름을 지어줍니다. 
plt.savefig("lec02_01_1.png")
# plt.show()  # 만들어진 그래프를 보여줍니다.
plt.close()

x_mean = np.mean(x)
y_mean = np.mean(y)

print("x 평균 : ", x_mean)
print("y 평균 : ", y_mean)

xx = x - x_mean  # [-3. -1.  1.  3.]
yy = y - y_mean  # [-9.5  2.5  0.5  6.5] 

numerator = xx * yy  # [28.5 -2.5  0.5 19.5]
numerator = np.sum(numerator)  # 46.0
denominator = np.sum(((x - x_mean) ** 2))  # 20.0

a = numerator / denominator  # 2.3 
b = y_mean - (x_mean * a)  # 79.0

x_line = np.linspace(0, 10, 100)
y_line = a * x_line + b 

plt.scatter(x, y) 
plt.grid() 
plt.xlabel("time")
plt.ylabel("score")

plt.plot(x_line, y_line, c='r')
plt.savefig("lec02_01_2.png")
plt.close()

y_pred = a * x + b  # [83.6 88.2 92.8 97.4]

error = y - y_pred  # [-2.6  4.8 -1.8 -0.4]
error_sq = error ** 2 # [ 6.76 23.04  3.24  0.16]

mse = np.sum(error_sq) / len(x)  # 8.299999999999985