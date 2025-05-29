def find_min_subsequence_naive(seq):
    n = len(seq)
    alphabet_set = set(range(1, 27))  # множество от 1 до 26
    min_len = float('inf')
    result = []

    for start in range(n):
        seen = set()
        for end in range(start, n):
            num = seq[end]
            if 1 <= num <= 26:
                seen.add(num)
            if seen == alphabet_set:
                if (end - start + 1) < min_len:
                    min_len = end - start + 1
                    result = seq[start:end + 1]
                break  # уже нашли все 26 — дальше не имеет смысла
    return (min_len if result else "NONE", result)

def main():
    try:
        n = int(input("введите количество чисел в последовательности: "))
        seq_input = input("введите числа, разделённые пробелом:\n")
        seq = list(map(int, seq_input.strip().split()))

        if len(seq) != n:
            print(f"ожидалось {n} чисел, получено {len(seq)}")
            return

        length, subarray = find_min_subsequence_naive(seq)

        if length == "NONE":
            print("\n NONE")
        else:
            print(f"\n длина минимальной подпоследовательности: {length}")

    except ValueError:
        print("ошибка: убедитесь, что вводите только целые числа.")

if __name__ == "__main__":
    main()

