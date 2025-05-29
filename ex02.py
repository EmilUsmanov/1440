from collections import defaultdict

def min_subarray_covering_alphabet(seq):
    required = set(range(1, 27))  #  только до 26
    count = defaultdict(int)
    formed = 0
    left = 0
    min_len = float('inf')
    min_window = (-1, -1)  # границы окна

    for right in range(len(seq)):
        num = seq[right]
        if 1 <= num <= 26:
            if count[num] == 0:
                formed += 1
            count[num] += 1

        while formed == 26:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)

            num_left = seq[left]
            if 1 <= num_left <= 26:
                count[num_left] -= 1
                if count[num_left] == 0:
                    formed -= 1
            left += 1

    if min_len == float('inf'):
        return "NONE", []

    start, end = min_window
    return min_len, seq[start:end + 1]

def main():
    try:
        n = int(input("введите количество чисел в последовательности: "))
        seq_input = input("введите числа, разделённые пробелом:\n")
        seq = list(map(int, seq_input.strip().split()))

        if len(seq) != n:
            print(f"ожидалось {n} чисел, получено {len(seq)}")
            return

        length, subarray = min_subarray_covering_alphabet(seq)

        if length == "NONE":
            print("\n   подходящая подпоследовательность не найдена: NONE")
        else:
            print(f"\n длина минимальной подпоследовательности: {length}")

    except ValueError:
        print("ошибка: убедитесь, что вводите только целые числа.")

if __name__ == "__main__":
    main()

