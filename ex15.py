from collections import Counter

def char(s):
    al = ''.join(char for char in s.upper() if char.isalpha())

 
    count = Counter(al)

    for char in sorted(count):
        print(f"{char}: {count[char]}")

string = input()
char(string)
