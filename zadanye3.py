def beauty_degree(arr):
    expected_min = 1
    current_segment_count = 0
    min_found = 0  # Переменная для отслеживания текущего минимума
    segment_indices = []  # Список для хранения индексов минимальных значений сегментов

    for index, num in enumerate(arr):
        # Обновляем текущий минимум
        if min_found == 0 or num < min_found:
            min_found = num

        # Если текущий минимум равен ожидаемому, увеличиваем счётчик
        if min_found == expected_min:
            current_segment_count += 1
            segment_indices.append(index)  # Добавляем индекс минимального значения
            expected_min += 1  # Ожидаем следующий минимум
            min_found = 0  # Сбрасываем минимум для нового сегмента

        # Если минимум превышает ожидаемое значение, то мы не можем разделить
        if min_found > expected_min:
            return 0, []  # Возвращаем 0 и пустой список

    return current_segment_count, segment_indices

def main():
    # Информация для пользователя о значении цветов
    print("Введите массив цветов в виде последовательности целых чисел, разделённых пробелами.")
    print("В этой задаче числа будут означать следующие цвета:")
    print("1 - Красный")
    print("2 - Зелёный")
    print("3 - Синий")
    print("4 - Жёлтый")
    print("5 - Чёрный")
    print("Например: введите '1 2 1 3 2 1' для красного, зелёного, красного, синего, зелёного, красного.")
    
    # Запрашиваем у пользователя ввод массива
    array_input = input("Введите массив цветов: ")
    # Преобразуем ввод в список целых чисел
    arr = list(map(int, array_input.split()))

    # Находим степень красоты и индексы сегментов
    result, indices = beauty_degree(arr)

    # Выводим результаты
    print(f"Степень красоты массива: {result}")
    if result > 0:
        print(f"Индексы минимальных значений сегментов: {indices}")

if __name__ == "__main__":
    main()