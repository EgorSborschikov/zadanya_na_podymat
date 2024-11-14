def can_construct_album():
    # Ввод количества композиций
    M = int(input("Введите количество композиций: "))
    
    # Ввод количества условий по настроению
    N = int(input("Введите количество условий (отрезков настроения): "))
    
    conditions = []
    
    print("Введите условия в формате 'L R S', где:")
    print("L - начальный индекс (1 <= L <= M)")
    print("R - конечный индекс (L <= R <= M)")
    print("S - необходимое общее настроение (целое число)")
    
    for _ in range(N):
        while True:
            try:
                L, R, S = map(int, input("Введите L, R и S: ").split())
                if 1 <= L <= R <= M:
                    conditions.append((L, R, S))
                    break
                else:
                    print(f"Ошибка: L должно быть от 1 до {M}, R должно быть не меньше L и не больше {M}. Повторите ввод.")
            except ValueError:
                print("Ошибка: Пожалуйста, введите три целых числа, разделенных пробелами.")

    # Инициализируем границы настроения
    min_values = [0] * (M + 1)
    max_values = [0] * (M + 1)

    for L, R, S in conditions:
        if S > 0:  # нужно положительное настроение
            min_values[L] += S
            max_values[R] += float('inf')
        elif S < 0:  # нужно отрицательное настроение
            min_values[L] += float('-inf')
            max_values[R] += S
        else:  # S == 0
            min_values[L] += 0
            max_values[R] += 0

    for i in range(1, M + 1):
        min_values[i] += min_values[i - 1]
        max_values[i] += max_values[i - 1]
    
    # Проверяем итоговые ограничения
    for i in range(1, M + 1):
        if min_values[i] > max_values[i]:
            print("Невозможно составить альбом с заданными условиями.")
            return

    print("Альбом можно составить с заданными условиями!")

if __name__ == "__main__":
    can_construct_album()
