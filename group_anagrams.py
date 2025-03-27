def group_anagrams1(strs:list[str]) -> list[list[str]]:
    """
    Given an array of strings strs, group the anagrams together.
    You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    """

    # First step is to create a dictionary to hold the grouped anagrams
    anagrams = {}
    for s in strs:
        # Sort the string and use it as a key in the dictionary
        key = ''.join(sorted(s))
        # If the key is not in the dictionary, create a new list for it
        anagrams[key] = anagrams.get(key, []) + [s]
    return list(anagrams.values())

    # Time complexity: O(n * k log k), where n is the number of strings and k is the maximum length of a string

def group_anagrams2(strs:list[str]) -> list[list[str]]:
    """
    Given an array of strings strs, group the anagrams together.
    You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    """
    # First step is to create a dictionary to hold the grouped anagrams
    anagrams = {}   

    # Second step is to loop through the strings and count the characters
    for s in strs:
        # Create a list of 26 zeros to count the frequency of each character (assuming only lowercase letters)
        count = [0] * 26
        for char in s:
            count[ord(char) - ord('a')] += 1  # Increment the count for the character
        # Convert the list to a tuple to use it as a key in the dictionary
        key = tuple(count)
        # If the key is not in the dictionary, create a new list for it
        anagrams[key] = anagrams.get(key, []) + [s]
    return list(anagrams.values())

def main():
    """
    Test the group_anagrams function with some sample input.
    """
    # Sample input
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    # Call the group_anagrams function and print the result
    print("------------------------------------------------\n")
    print("Group Anagrams using sorting method:")
    print(group_anagrams1(strs))
    print("\n------------------------------------------------\n")
    print("Group Anagrams using character count method:")
    print(group_anagrams2(strs))

if __name__ == "__main__":  
    main()
    
