import numpy as np
import matplotlib.pyplot as plt
import random

x = np.linspace(-10, 10, num=100)

constants = []
for i in range(3):
    constants.append(random.randint(-10, 10))

print("Välkommen!")
print("Du kommer få se en graf när du är redo")
print("Stäng rutan med grafen när du är redo att gissa")
correct = False
while not correct:
    svar = input("Skriv \"""ja\" när du vill köra: ")
    correct = True if svar.strip().lower() == "ja" else False

fx = []
for i in range(len(x)):
    fx.append(constants[0] * x[i] ** 2 + constants[1] * x[i] + constants[2])

plt.plot(x, fx)
axis_width = 10
plt.xlim(-axis_width, axis_width)
plt.ylim(-axis_width, axis_width)
plt.grid()
plt.axvline()
plt.axhline()
plt.show()

a = int(input("Vilken tal tror du a är: "))
b = int(input("Vilken tal tror du b är: "))
c = int(input("Vilken tal tror du c är: "))

if a == constants[0] and b == constants[1] and c == constants[2]:
    print("Helt rätt!")
else:
    print("Fel!")
    print(f'Rätt svar var: a={constants[0]}, b={constants[1]} och c={constants[2]}')
