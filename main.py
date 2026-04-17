# 1-mashq
pattern = "abba"
s = "dog cat cat dog"

words = s.split()
d1, d2 = {}, {}

valid = True
for p, w in zip(pattern, words):
    if d1.get(p, w) != w or d2.get(w, p) != p:
        valid = False
        break
    d1[p] = w
    d2[w] = p

print(valid)
# 2-mashq
nums = [1,2,3,4,2]

seen = set()
for n in nums:
    if n in seen:
        print("Cycle bor")
        break
    seen.add(n)
# 3-mashq
from collections import Counter

nums = [1,1,1,2,2,3]
k = 2

print([x for x,_ in Counter(nums).most_common(k)])
# 4-mashq
nums = [2,1,2,4,3]
stack = []
res = [-1]*len(nums)

for i in range(len(nums)):
    while stack and nums[stack[-1]] < nums[i]:
        res[stack.pop()] = nums[i]
    stack.append(i)

print(res)
# 5-mashq
s = "egg"
t = "add"

d1, d2 = {}, {}
print(all(d1.setdefault(a,b)==b and d2.setdefault(b,a)==a for a,b in zip(s,t)))
