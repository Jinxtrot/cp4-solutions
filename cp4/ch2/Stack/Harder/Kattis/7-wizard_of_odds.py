n,k=map(int,input().split())
print("Your wish is granted!"if n<=2**k else"You will become a flying monkey!")

"""
My first solution was to always divide n by 2 only if n was greater than 1. But
this solution was wrong in a special case. Instead I reformulate the problem and
realized that i was always looking to eliminate half the possibilities of N by half, then
I realized that I could use the power of 2 to solve the problem. If N is greater than 2^k
then the wizard will become a flying monkey, otherwise the wish is granted.
"""