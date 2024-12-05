while True:
    a, b = input().split()
    if a == '0' and b == '0':
        break
    a = a.zfill(10)
    b = b.zfill(10)

    b = b[::-1]

    carry = 0
    count = 0
    result = 0

    for index,number in enumerate(a[::-1]):
        numbers = []
        numbers.append(int(number))
        numbers.append(int(b[index]))
        numbers.append(carry)
        result = sum(numbers)
        if result >=10:
            count +=1
            carry = 1
        else:
            carry = 0
            continue
    if count==0:
        print("No carry operation.")
    elif count==1:
        print("1 carry operation.")
    else:
        print(f"{count} carry operations.")

    """
    Well, pretty step forward. First, I thought that the maximun value for a sum of two numbers is 18, so I just need to
    check if the sum is greater than 9, then there is a carry and count from it. But I got wrong the second case because 
    I was not considering the carry in the sum of the numbers. For example 9+0 = 9, but if there is a carry from the previous 
    sum, then 9+0+1 = 10, and the carry now will give you 1 which in my initial approach I was not considering. 
    Once I fixed that, the code worked fine. Ok, nvm I implemented the code now with stack logic on it.
    """
        
    
    