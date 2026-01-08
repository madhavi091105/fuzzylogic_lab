def all_vowels_exist(s):
    vowels = set("aeiouAEIOU")
    found = set()
    for i in range(len(s)):
        if s[i] in vowels:
            found.add(s[i].lower())
    return len(found) == 5
string = input("Enter a string:")
print(all_vowels_exist(string))