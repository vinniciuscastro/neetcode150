from collections import Counter

def is_anagram1(s: str, t: str):
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    """
    # first aproach is to sort the strings and compare them
    # the first step is to remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()

    # second step is to sort the strings and return the comparison
    return sorted(s) == sorted(t)

    # Time complexity: O(n log n)

def is_anagram2(s: str, t: str):
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    The Counter class from Python's collections module counts the frequency of each character in a string. 
    By comparing the Counter objects of both strings, we can determine if they are anagrams.
    """
    # second aproach is to use sing the Counter from collections Module
    # the first step is to remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()

    # second step is to create a dictionary with the characters and their counts
    counter_s = Counter(s)
    counter_t = Counter(t)

    # third step is to compare the dictionaries
    return counter_s == counter_t

    # Time complexity: O(n)
def is_anagram3(s: str, t: str):
    """
    Given two strings s and t, return true if t is an anagram of s, and false otherwise.
    Character frequency count using a dictionary (Hash Table).
    By manually counting the frequency of each character using a dictionary, 
    we can compare these dictionaries to check for anagrams.
    """

    # First step is to remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()

    # Second step is to compare the length of the strings
    if len(s) != len(t):
        return False
    
    # Third step is to create a dictionary with the characters and their counts
    counter1 = {}
    counter2 = {}

    
    # loop through the strings and count the characters "s"
    for char in s:
        # if the character is already in the dictionary, increment the count
        counter1[char] = counter1.get(char, 0) + 1 # using get method to avoid KeyError if the key is not in the dictionary

    # Repeat the process for the second string "t"
    for char in t:
        counter2[char] = counter2.get(char, 0) + 1

    # Fourth step is to compare the dictionaries
    return counter1 == counter2

    # Time complexity: O(n)
def main():
    s = "ana gram"
    t = "n agaRam"

    print('------------------------------------------------------')  
    print(f"Is an Anagram?\nWord 1: {s}\nWord 2: {t}")
    print()
    print(f"Sorting approach\n Is an anagram? {is_anagram1(s, t)}") # True
    print(f"Counter\n Is an anagram? {is_anagram2(s, t)}") # True
    print(f"Frequency approach\n Is an anagram? {is_anagram3(s, t)}") # True

    s = "rat"
    t = "caT"
    print('------------------------------------------------------')  
    print(f"Is an Anagram?\nWord 1: {s}\nWord 2: {t}")
    print()
    print(f"Sorting approach\n Is an anagram? {is_anagram1(s, t)}") # False
    print(f"Counter\n Is an anagram? {is_anagram2(s, t)}") # False
    print(f"Frequency approach\n Is an anagram? {is_anagram3(s, t)}") # False

    print('------------------------------------------------------')  

if __name__ == "__main__":
    main()




