def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    low = 1
    high = 100
    
    while low <= high:
        count += 1
        mid = (low + high) // 2
        if mid == number:
            return count
        elif mid < number:
            low = mid + 1
        else:
            high = mid - 1
    
    # Ваш код заканчивается здесь

    return count

# Пример использования функции
print(game_core_v3())