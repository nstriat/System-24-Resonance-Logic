import math

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def structural_resonance_analysis(a, b):
    """
    Анализ структуры (L, P, S). 
    L - Logic (Логика), P - Proportion (Пропорция), S - Structure (Структура).
    """
    expansion = a + b
    compression = abs(b - a)
    # Формирование Центрального Узла на базе Системы 24
    central_node = int(str(expansion) + str(compression))
    
    status = "ПРОСТОЕ (Резонанс)" if is_prime(central_node) else "СОСТАВНОЕ (Коррекция)"
    
    print(f"Входные координаты: A={a}, B={b}")
    print(f"Вектор расширения: {expansion}, Вектор сжатия: {compression}")
    print(f"ЦЕНТРАЛЬНЫЙ УЗЕЛ: {central_node} [{status}]")
    
    if is_prime(central_node):
        return "Структура самодостаточна."
    return "Требуется бинарная коррекция."

# Тестовый запуск (твои данные из Colab)
if __name__ == "__main__":
    print(structural_resonance_analysis(5, 8))
