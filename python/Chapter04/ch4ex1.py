nums=set()
counter = 0
while True:
    data = input("enter number:  end to quit")
    if data == 'end':
        break
    if data in nums:
        counter+=1
        continue
    nums.add(data)
print(nums)
print(counter)

