# 4-Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# Пример:
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)

print('Введите номер четверти (1-4): ')
quarter = int(input())


def Coordinator(quarter):
    if (quarter == 1):
        return f"В {quarter} четверти X больше нуля, Y больше нуля"
    if (quarter == 2):
        return f"В {quarter} четверти X меньше нуля, Y больше нуля"
    if (quarter == 3):
        return f"В {quarter} четверти X меньше нуля, Y меньше нуля"
    if (quarter == 4):
        return f"В {quarter} четверти X больше нуля, а Y меньше нуля"
    return "Введено неверное значение"

cord = Coordinator(quarter)
print(cord)