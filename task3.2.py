sums=0
for i in range(101):
    if i%2==0:
        sums+=i

print(sums)

nums=[x for x in range(101) if x%2==0]
print(f"total through comprehension is: {sum(nums)}")
