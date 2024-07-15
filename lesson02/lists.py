users = ['metalekan', 'John', 'moyo']
cars = ["lexus", "toyota", "mercedes"]
emptylist = []

print("John" in users)
print(users[0])
print(users[-2])

print(users.index("moyo"))

print(users[0:2])
print(users[1:2])
print(users[1:])
print(users[-3:-1])

cars.append("honda")
print(len(cars))

cars += ["maybach"]

cars.extend(["lincoln", "chevy", "suzuki"])
print(cars)

# users.extend(cars)
# print(users)

users.insert(0, "ade")
print(users)

users[2:2] = ["debby", "tiwa"]
print(users)

users.remove("tiwa")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# delete car
cars.clear()
print(cars)

# sort alphabetically
users[1:2] = ["tope", "micheal"]
users.sort() 
print(users)

users.sort(key=str.lower)
print(users)

nums = [3, 9, 18, 1, 6]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
print(mycopy)

print(type(nums))

mylist = list(["pro", False, 23, "john"])
print(mylist)


# Tuples

mytuple = tuple(('john', 27, True))

anothertuple = (3, 6, 9, 1, 7, 7)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('lekan')
newtuple = tuple(newlist)

print(newtuple)

(one, three, *hey) = anothertuple
print(one)
print(three)
print(hey)

print(anothertuple.count(7))





