file = open("sample.txt", "w")
text = input("Enter the text: ")
file.write(text)
file.close()
file = open("sample.txt", "r")
data = file.read()
characters = len(data)
words = len(data.split())
lines = len(data.splitlines())
vowels = 0
for i in data.lower():
    if i in "aeiou":
        vowels += 1
print("Characters =", characters)
print("Words =", words)
print("Lines =", lines)
print("Vowels =", vowels)
file.close()
