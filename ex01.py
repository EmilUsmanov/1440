from typing import List, Tuple

def min_points_to_cover_segments(segments: List[Tuple[int, int]]) -> List[int]:
    # Шаг 1: Отсортировать отрезки по правой границе
    sorted_segments = sorted(segments, key=lambda seg: seg[1])
    
    points = []
    last_point = None

    for seg in sorted_segments:
        start, end = seg
        # Если текущий отрезок не покрыт последней точкой
        if last_point is None or last_point < start:
            # Выбираем правый конец отрезка как новую точку
            last_point = end
            points.append(last_point)
    
    return points

# Пример использования:
if __name__ == "__main__":
    # Ввод данных
    n = int(input("Введите количество отрезков: "))
    segments = []
    print("Введите каждый отрезок через пробел (x y):")
    for _ in range(n):
        x, y = map(int, input().split())
        segments.append((x, y))

    result = min_points_to_cover_segments(segments)
    print("Минимальное количество точек:", len(result))
    print("Сами точки:", result)
