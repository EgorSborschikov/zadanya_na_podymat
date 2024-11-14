def main():
    # Считываем размерности массивов X и Y
    n = int(input("Введите длину массива X: "))
    m = int(input("Введите длину массива Y: "))

    # Считываем массивы X и Y
    X = list(map(int, input("Введите элементы массива X, разделенные пробелами: ").split()))
    Y = list(map(int, input("Введите элементы массива Y, разделенные пробелами: ").split()))

    # Проверяем, что размеры массивов совпадают с введенными значениями
    if len(X) != n or len(Y) != m:
        print("Ошибка: Размеры массивов не совпадают с введенными значениями.")
        return

    # Функция для вычисления мультимножества
    def compute_multiset():
        A = []
        for x in X:
            for y in Y:
                if y != 0:  # избегаем деления на ноль
                    A.append(x / y)
        return sorted(A)

    # Основной цикл обработки запросов
    while True:
        query = input("Введите запрос (или 'exit' для выхода): ").strip().split()
        if query[0].lower() == 'exit':
            break
        q_type = int(query[0])

        if q_type == 1:  # Запрос на вывод k-й статистики
            k = int(query[1]) - 1  # Приводим к 0-индексации
            A = compute_multiset()
            if 0 <= k < len(A):
                print(f"{k + 1}-я статистика: {A[k]}")
            else:
                print("Ошибка: k выходит за пределы размеров мультимножества.")

        elif q_type == 2:  # Присвоение X[i] := v
            i = int(query[1]) - 1  # Приводим к 0-индексации
            v = int(query[2])
            if 0 <= i < n:
                X[i] = v
            else:
                print("Ошибка: индекс i выходит за пределы массива X.")

        elif q_type == 3:  # Присвоение Y[i] := v
            i = int(query[1]) - 1  # Приводим к 0-индексации
            v = int(query[2])
            if 0 <= i < m:
                Y[i] = v
            else:
                print("Ошибка: индекс i выходит за пределы массива Y.")
        else:
            print("Ошибка: Неизвестный тип запроса.")

if __name__ == "__main__":
    main()
