import math
#определим нужные функции
def Discriminant(a,b,c):
    return (b * b) - (4 * a * c);
def Roots(a,b,d):
    if d == 0:
        return [(-b) / (2 * a)];
    if d > 0:
        return [(-b - math.sqrt(d)) / (2 * a),(-b + math.sqrt(d)) / (2 * a)];
#получим нужные данные
print("Решение квадратного уравнения");
print("Введите коэффициент a");
a = float(input());
print("Введите коэффициент b");
b = float(input());
print("Введите коэффициент c");
c = float(input());
print("Ваши коэффициенты: a =", a, "b =", b, "c =", c);
#решение квадратного уравнения
d = Discriminant(a,b,c);
print("Дискриминант: ", d);
if d < 0:
    print("Уравнение не имеет корней");
else:
    print("Ответ", Roots(a,b,d));
