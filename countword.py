name = input("Enter a string: ")
vowels = 'aeiouAEIOU'
vowelcount = qmarkcount = consonentcount = 0 

words = name.split()
wordscount = len(words)

for char in name:
    if char in vowels:
        vowelcount += 1
    elif char.isalpha():
        consonentcount += 1
    elif char=='?':
        qmarkcount +=1

print("Number of ... ")
print("Vowels = ",vowelcount)
print("Consonents = ",consonentcount)
print("Question marks = ",qmarkcount)
print("Words = ",wordscount)
