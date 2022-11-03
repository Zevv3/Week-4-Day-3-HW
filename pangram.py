# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown 
# fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
# https://www.codewars.com/kata/545cedaa9943f7fe7b000048

def is_pangram_original(s):
    pangram = True
    s = s.lower()
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    while pangram:
        for letter in alphabet:
            if letter.lower() not in s:
                pangram = False
                return False
            
        return True
print(is_pangram_original("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram_original("1bcdefghijklmnopqrstuvwxyz"))

#not sure why I had a while loop in there,
# although I'm not sure how much time it really saves
# since it wasn't really doing anything

def is_pangram_updated(s):
    s = s.lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if letter not in s:
            return False
    return True
print(is_pangram_updated("The quick, brown fox jumps over the lazy dog!"))
print(is_pangram_updated("1bcdefghijklmnopqrstuvwxyz"))