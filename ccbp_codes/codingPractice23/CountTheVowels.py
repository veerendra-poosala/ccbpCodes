#CountTheVowels

def count_the_vowels(word):
    vowels = ['a','e','i','o','u']
    count = 0
    for char in word:
        for letter in vowels:
            is_vowel = char == letter
            if is_vowel:
                count += 1 
    return count


word = input()
result = count_the_vowels(word)
print(result)
