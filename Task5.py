# 5- Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21
import math
def Distance(x1,y1,x2,y2):
    if (x1 == x2 and y1 == y2):
        return 0
    numX = x1 - x2
    numY = y1 - y2
    return round(math.sqrt(numX*numX + numY*numY),3)
print("Введите координаты первой точки")
print("X: ")
x1 = float(input())
print("Y: ")
y1 = float(input())
print("Введите координаты второй точки")
print("X: ")
x2 = float(input())
print("Y: ")
y2 = float(input())

dist = Distance(x1,y1,x2,y2)
print(f"Расстояние между точками равно {dist}")