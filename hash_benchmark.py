def search_simplified(pattern, text):
    iteration_count = 0
    m = len(pattern)
    n = len(text)
    pattern_hash = hash(pattern)
    iteration_count += 1  # linha acima

    for i in range(n - m + 1):
        iteration_count += 1  # início do loop
        substring = text[i:i+m]
        iteration_count += 1  # fatia da string
        substring_hash = hash(substring)
        iteration_count += 1  # cálculo do hash

        if substring_hash == pattern_hash:
            iteration_count += 1  # if comparando hashes
            if substring == pattern:
                iteration_count += 1  # comparação de strings
                return i, iteration_count
    return -1, iteration_count


def rabin_karp_search(pattern, text):
    iteration_count = 0
    base = 256
    prime_mod = 101

    m = len(pattern)
    n = len(text)
    iteration_count += 2  # definindo m, n

    pattern_hash = 0
    current_substring_hash = 0
    highest_base_power = 1
    iteration_count += 3  # inicializando variáveis

    for _ in range(m - 1):
        highest_base_power = (highest_base_power * base) % prime_mod
        iteration_count += 1  # loop para calcular highest_base_power

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime_mod
        current_substring_hash = (base * current_substring_hash + ord(text[i])) % prime_mod
        iteration_count += 2  # calculando hashes

    for i in range(n - m + 1):
        iteration_count += 1  # loop principal
        if pattern_hash == current_substring_hash:
            iteration_count += 1  # comparação hash
            if text[i:i+m] == pattern:
                iteration_count += 1  # comparação strings
                return i, iteration_count

        if i < n - m:
            current_substring_hash = (
                base * (current_substring_hash - ord(text[i]) * highest_base_power) +
                ord(text[i + m])
            ) % prime_mod
            iteration_count += 3  # atualização rolling hash

            if current_substring_hash < 0:
                current_substring_hash += prime_mod
                iteration_count += 1  # correção valor negativo

    return -1, iteration_count


# Testando as funções e mostrando iterações:

pattern = "ADF"
text = "ABCDCBDCBDACBDABDCBADF"

result_simple, iters_simple = search_simplified(pattern, text)
print(f"Busca simplificada: índice={result_simple}, iterações={iters_simple}")

result_rk, iters_rk = rabin_karp_search(pattern, text)
print(f"Rabin-Karp com rolling hash: índice={result_rk}, iterações={iters_rk}")

