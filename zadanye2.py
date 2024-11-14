def find_min_distance_and_cost(t, costs):
    n = len(costs)
    results = []

    # Создаём перечисление с индексами и сортируем по стоимости
    indexed_costs = sorted((costs[i], i) for i in range(n))

    # Двигаемся по отсортированному списку
    for start in range(n):
        current_cost = 0
        for end in range(start, n):
            current_cost += indexed_costs[end][0]
            if end - start + 1 > t:  # Слишком много пробирок, выходим из цикла
                break
            if end - start + 1 == t:  # У нас есть t пробирок
                # Получаем индексы пробирок
                indices = [indexed_costs[i][1] for i in range(start, end + 1)]
                distance = max(indices) - min(indices) + 1  # Расстояние
                results.append((current_cost, distance))

    # Находим минимальные затраты и соответствующее расстояние
    min_cost = float('inf')
    min_distance = float('inf')
    
    for cost, distance in results:
        if cost < min_cost:
            min_cost = cost
            min_distance = distance
        elif cost == min_cost:
            min_distance = min(min_distance, distance)

    return min_distance if min_distance != float('inf') else -1  # Если не нашли

def main():
    # Запрашиваем количество пробирок
    t = int(input("Введите количество пробирок, которые нужно купить (t): "))
    
    # Запрашиваем стоимость пробирок
    costs = input("Введите стоимости пробирок, разделённые пробелами: ").split()
    costs = list(map(int, costs))  # Преобразуем в список целых чисел

    # Проверяем, достаточно ли пробирок в магазине
    if len(costs) < t:
        print("Ошибка: недостаточно пробирок в магазине.")
        return
    
    # Находим минимальное расстояние
    min_distance = find_min_distance_and_cost(t, costs)
    if min_distance == -1:
        print("Не удалось найти подходящие пробирки.")
    else:
        print(f"Минимальное расстояние: {min_distance}")

if __name__ == "__main__":
    main()