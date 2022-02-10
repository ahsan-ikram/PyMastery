# Valid anagram
# First and last index in sorted array
# Kth Largest element
# Symmetric tree
# Generate parentheses
# Gas station
# Course schedule
# Kth permutation
# Minimum window substring
# Largest rectangle in histogram

# Reference: https://www.freecodecamp.org/news/10-common-coding-interview-problems-solved/

def valid_anagrams(string_one: str, string_two: str) -> bool:
    """ An anagram is a word or phrase formed by rearranging the letters of a different
        word or phrase, typically using all the original letters exactly once
    :return: bool
    """

    if len(string_one) != len(string_two):
        return False
    s1_dict = {}
    for char in string_one:
        s1_dict[char] = s1_dict.setdefault(char, 0) + 1
    s2_dict = {}
    for char in string_two:
        s2_dict[char] = s2_dict.setdefault(char, 0) + 1

    return s1_dict == s2_dict


def main():
    print(f'alpha and beta are anagrams? {valid_anagrams("alpha", "beta")}')
    print(f'danger and garden are anagrams? {valid_anagrams("danger", "garden")}')


if __name__ == '__main__':
    main()
