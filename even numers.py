#finding even numbers from 1 to N
'''def even_nos(n):
    for i in range(1,n+1):
        if i%2==0:
            print(i)
    return i

def main():
    n=int(input("Enter number: "))
    even_nos(n)
main()'''



def even_nos(n):
    count=0
    for i in range(1,n+1):
        if i%2==0:
            print(i)
            count+=1
    return count
def main():
    n=int(input("Enter n: "))
    print("Even numbers: ",even_nos(n))
main()
