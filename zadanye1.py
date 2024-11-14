def sum_of_and_pairs(n):
    MOD = 10**9 + 7
    total_sum = 0

    # Проходим по каждому биту
    for bit in range(31):  # 0 <= bit < 31
        power_of_two = 1 << bit  # 2^bit
        count = (n >> (bit + 1)) * (1 << (bit + 1))
        
        # Считаем оставшиеся числа
        remainder = n % (1 << (bit + 1))
        if remainder >= power_of_two:
            count += max(0, remainder - power_of_two + 1)
        
        # Полное количество пар, где оба числа имеют установленный бит
        total_sum += (count * count) % MOD * power_of_two % MOD
        total_sum %= MOD

    return total_sum

n = int(input("Введите n: "))
result = sum_of_and_pairs(n)
print(result)
