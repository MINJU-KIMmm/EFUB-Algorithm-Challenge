
S = 0b000001
S |= (1<<2)
S &= ~(1<<2)
S ^= (1<<2)

print(S)
print(bin(S))

print(1 if S&(1<<2) !=0 else 0)

S = (1<<3) -1
print(S)
print(bin(S))

def bitCount(x):
    if x==0: return 0

    return x%2 + bitCount(x//2)

print(bitCount(S))
print()

S = 0b1001
subset = 0b1001
while True:
    subset = (subset-1)&S
    if subset == 0:
        break

    print(subset)