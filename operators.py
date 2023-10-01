#arthematic operators

a = 10
b = 30
print(a + b)
print(a)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
#assigenment operator
p = 20
q = 30
p += 2
print(p)
q -= 10
print(q)
q *= 10
print(q)
p /= 2
print(p)
p %= 10
print(p)
q //= 2
print(q)
#logical operator
#and operation
s = 9
t = 4
print(s < t and s > t)
print(s > t or s < t)
print(not(s > t and t < s))
#comparision operator
m = 7
k = 4
print(m <= k)
print(m >= k)
print(m > k)
print(m < k)
print(m != k)
#bitwise operator
#bitwise and operator
x = 234
y = 344
print(x & y)
print(x | y)
print(x ^ y)
#left shift operator
#>>
a=4
b=2
print(a>>b)
a=5
b=8
print(a>>b)
#right shift operator
a=8
b=9
print(a<<b)
a=1
b=2
print(a<<b)
#check address of a variable
a=111
print(id(a))
a=890
print(id(a))
#identity operator
#is
a=50
b=40
print(a is b)
a=30
b=30
print(a is b)

#is not
a=10
b=19
print(a is not b)
a=13
b=13
print(a is not b)

#membership operator
#in
a="sujitha@gmail.com"
print("@" in a)
print("suji" in a)
print("9" in a)
fruits=["mango", "apple", "grapes"]
name = "apple"
print(name in fruits)
name = "grapes"
print(name in fruits)
#not in
names=["suji" ,"mahalya" ,"bhavani"]
name = "suji"
print(name not in names)
name = "mahalya"
print(name not in names)

