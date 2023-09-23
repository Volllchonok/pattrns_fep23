import math

def f(x):
    # Задайте функцію f(x) згідно вашим потребам
    return x**2  # Приклад: функція y = x^2

def compute_values(a, b, eps):
    # Визначення кроку для обчислення значень функції
    step = eps

    # Виведення заголовка таблиці
    print(f"x\tf(x)")

    # Ітеруємося від a до b з кроком step
    x = a
    while x <= b:
        y = f(x)  # Обчислення значення функції f(x)
        print(f"{x:.2f}\t{y:.2f}")
        x += step

if __name__ == "__main__":
    # Зчитування вхідних даних з клавіатури
    a = float(input("Введіть початкове значення a: "))
    b = float(input("Введіть кінцеве значення b: "))
    epsilon = float(input("Введіть точність epsilon: "))

    # Обчислення та виведення значень функції
    compute_values(a, b, epsilon)
