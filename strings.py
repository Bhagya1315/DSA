#concatination
'''first='Hello'
second='Students'
result=first+'_'+second
print(result)'''


#count characters in string
'''def count_chars(text):
    c=0
    for char in text:
        c+=1
    return c
text=input("Enter the text: ")
print("Characters count:  ",count_chars(text))'''

#Counting vowels in string
'''def count_vowels(text):
    c=0
    vowels='aeiouAEIOU'
    for char in text:
        if char in vowels:
            c+=1
    return c
text=input("Enter the text: ")
print("The vowels count: ",count_vowels(text))'''

#Revering the text
def rev_text(text):
    reversed_text = ' '
    for char in text:
        reversed_text=char+reversed_text
    return reversed_text
text=input("Enter text: ")
print("reversed text: ",rev_text(text))
