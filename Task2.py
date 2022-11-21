# 2- Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.

for x in [0,1]:
    for y in [0,1]:
        for z in [0,1]:
            print(f'Для X = {x} Y = {y} Z = {z} =', x , y , z)
for x in [True,False]:
    for y in [True,False]:
        for z in [True,False]:           
            print(x,'и',y,'или',z,'=',x and y or z)