#Arrays
#Accessing array
n=[10,20,30]
print(n[0])
print(n[2])

#Traversing array
n=[10,20,30]
for i in n:
    print(n)

#updating array
    n[0]=100
    print(n)

#Adding element
n.append(40)
print(n)


#sum of array elements
def count_sum(arr):
    t=0
    for n in arr:
        t+=n
    return t
arr=[1,2,3,4,5]
print("Sum: ",count_sum(arr))


#counting digits in an array
def count_digits(n):
    c=0
    for i in n:
        c+=len(str(abs(i)))
    return c
n=[12,345,6,7890]
res=count_digits(n)
print("Total number of digits: ",res)


#counting the even digits in an array
def count_even(a):
    c=0
    for i in a:
        i=abs(i)
        while i>0:
            d=i%10
            if d%2==0:
                c+=1
            i//=10
        return c
a=[12,345,6,7890]
print("Even digits: ",count_even(a))


#maximum value
def find_max(arr):
    max_value=arr[0]
    for num in arr:
        if num>max_value:
            max_value=num
    return max_value
arr=[12,45,7,89,23]
print("Maximum value: ",find_max(arr))
