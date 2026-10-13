import matplotlib.pyplot as plt
import math
x = [i/10 for i in range(-50, 50)]
y = [2*i + math.sin(i)**2 +3 for i in x]
plt.xlabel("x") 
plt.ylabel("y")
plt.title("Hello, po!")
plt.grid(True)
plt.plot(x, y, marker=".")
plt.show()