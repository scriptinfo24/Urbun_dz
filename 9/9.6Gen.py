def all_variants(text):

    from itertools import permutations


    unique_permutations = set(permutations(text))

    for variant in sorted(unique_permutations):

        yield ''.join(variant)


# Пример использования функции
a = all_variants("abc")

for i in a:
    print(i)
