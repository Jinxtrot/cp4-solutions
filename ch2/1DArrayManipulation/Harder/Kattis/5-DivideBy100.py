n = input()

m = input()

n_len = len(n)
m_len = len(m)
zeroes_on_m = m_len - 1

if n_len > m_len:
    interger = n[:n_len-(zeroes_on_m)]
    decimal = n[n_len-(zeroes_on_m):]
    if decimal.count("0") == len(decimal):
        print(interger)
    else:
        decimal = decimal.rstrip("0")
        print(interger + "." + decimal)
else:
    print("0." + "0"*((zeroes_on_m)-n_len) + n)
