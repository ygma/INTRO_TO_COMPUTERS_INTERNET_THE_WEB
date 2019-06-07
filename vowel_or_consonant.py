def check(char):
    vowels = ['a', 'e', 'i', 'o', 'u']

    return 'vowel' if char.lower() in vowels else 'consonant'

char = input('need a char: ')
print(check(char))
