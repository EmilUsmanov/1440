def strange_function(limit):
    f0, f1 = 1, 3
    A = []

    n = 0
    while len(A) <= limit:
        if n == 0:
            fn = f0
        elif n == 1:
            fn = f1
        else:
            fn = 5 * f1 + f0
            f0, f1 = f1, fn

        if fn % 2 == 1:
            A.append(fn)
        n += 1

    return A[limit]

# найдём A[39]
result = strange_function(39)
print(f"A[39] = {result}")
