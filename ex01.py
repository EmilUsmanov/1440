from typing import List, Tuple

def min_points_to_cover_segments(segments: List[Tuple[int, int]]) -> List[int]:
    sorted_segments = sorted(segments, key=lambda seg: seg[1])

    points = []
    last_point = None

    for seg in sorted_segments:
        start, end = seg
        if last_point is None or last_point < start:
            last_point = end
            points.append(last_point)

    return points

# тут вводим данные, я не стал читать с файла, просто вставляю число 200 в терминал и далее вставляю остальные точки простым копированием в терминал:
if __name__ == "__main__":
    #  200
    n = int(input("количество отрезков: "))
    segments = []
    print("Отрезки  через пробел (x y):")
    for _ in range(n):
        x, y = map(int, input().split())
        segments.append((x, y))

    result = min_points_to_cover_segments(segments)
    print("минимальное количество точек:", len(result))
    print("сами точки:", result)
