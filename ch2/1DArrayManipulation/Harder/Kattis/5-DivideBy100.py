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

"""
I was asking why this problem was in the 1D Array Manipulation section, and I realized that the problem is about manipulating the number as a string.
In the end, m will always be 10**x, where x is a positive integer. So, checking the length of n and m, we can determine which number is the integer and which is the decimal.
If n has more digits than m, we can split n into an integer and a decimal part. If the decimal part is all zeroes, we can just print the integer part. 
Otherwise, we print the integer part and the decimal part without the trailing zeroes. If m has more digits than n, we print 0. followed by the difference between the lengths of m and n, and n.
"""
