from collections import Counter
def second_frequent(nums):
    counter = Counter(nums).most_common()
    if len(counter) > 1 and counter[0][1] == counter[1][1]:
        return counter[1][0]
    else:
        return counter[0][0]
import sys
input = sys.stdin.readline
N = int(input())
S = [int(input()) for _ in range(N)]
S.sort()
print(sum(S) // N)
print(S[N // 2])
print(second_frequent(S))
print(S[-1] - S[0])