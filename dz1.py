# задача 1
# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
# weekDays = int(input("введите день недели в числовом формате: "))
# if weekDays>5 and weekDays<=7:
#     print("введенный день недели является выходным")
# elif weekDays>0 and weekDays<6:
#     print("введенный день недели является будним")
# else:
#     print("введеное число выходит за диапазон")

# задача 2
# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
# эта точка (или на какой оси она находится).

# CoordX = int(input("введите координату x: "))
# CoordY = int(input("введите координату y: "))
# if CoordX>0 and CoordY>0:
#     print("I четверть")
# elif CoordX>0 and CoordY<0:
#     print("IV четверть")
# elif CoordX<0 and CoordY<0:
#     print("III четверть")
# elif CoordX<0 and CoordY>0:
#     print("II четверть")
# elif CoordX==0 or CoordY==0:
#     print("введеные координаты лежат на осях")

# задача 3
# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)

# fourthNumber = int(input("введите четверть в числовом формате: "))
# if fourthNumber == 1:
#     print("диапазон значений I четверти [X>0;Y>0]")
# elif fourthNumber == 2:
#     print("диапазон значений II четверти [X<0;Y>0]")
# elif fourthNumber == 3:
#     print("диапазон значений III четверти [X<0;Y<0]")
# elif fourthNumber == 4:
#     print("диапазон значений IV четверти [X>0;Y<0]")
# else:
#     print("такой четверти не существует")

# задача 4
# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.

# import math
# segmentA = (int(input("введите координату х отрезка А: ")),int(input("введите координату y отрезка А: ")))
# SegmentB = (int(input("введите координату х отрезка B: ")),int(input("введите координату y отрезка B: ")))
# lenghtResultSegment = float(math.sqrt(math.pow((SegmentB[0]-segmentA[0]),2)+math.pow((SegmentB[1]-segmentA[1]),2)))
# print(f"длинна отрезка лежащего между кординатами {segmentA} и координатами {SegmentB} = {round(lenghtResultSegment,2)}")

# задача 5
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
decX = int(input("введите значение декаты "))
decY = int(input("введите значение декаты "))
decZ = int(input("введите значение декаты "))
if (decX<0 or decX>1) or (decY<0 or decY>1) or (decZ<0 or decZ>1):
    print("неверный формат данных")
else:
    print(bool((not(decX or decY or decZ))==(not(decX) and not(decY) and not(decZ))))