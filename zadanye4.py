def compute_final_value(functions, initial_value):
    result = initial_value
    # Применяем функции в обратном порядке
    for a, b in reversed(functions):
        result = (a * result + b) % (10**9 + 7)
    return result

def find_perfect_sound():
    functions = []
    print("Введите набор линейных функций в формате 'a b' (для f(x) = ax + b). Вводите 'end' для завершения ввода:")
    
    while True:
        user_input = input("> ")
        if user_input.lower() == 'end':
            break
        try:
            a, b = map(int, user_input.split())
            functions.append((a, b))
        except ValueError:
            print("Некорректный ввод, пожалуйста, введите два целых числа, разделенных пробелом.")

    initial_value = 2  # Начальное значение
    mod = 10**9 + 7

    for i in range(len(functions)):
        remaining_functions = functions[:i] + functions[i+1:]  # Удаляем i-ю функцию
        final_value = compute_final_value(remaining_functions, initial_value)
        print(f"После удаления функции {functions[i]}: f(g(...(2))) = {final_value}")

if __name__ == "__main__":
    find_perfect_sound()