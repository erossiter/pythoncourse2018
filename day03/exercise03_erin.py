## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test file in the terminal and see your results.
def count_vowels(word):
    if type(word) != str:
        raise TypeError, "Use quotes '...' to make a string."
    v = ["a", "e", "i", "o", "u"]
    count = 0
    for letter in word:
        if letter in v:
            count += 1
    return count


