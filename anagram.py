def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)
str1 = "mug"
str2 = "gum"

if are_anagrams(str1, str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")










## Algorithm to Check if Two Strings Are Anagrams
# Take two input strings – Let's call them str1 and str2.

# Check if their lengths are the same – If the lengths are different, they cannot be anagrams, so return False.

# Sort both strings alphabetically – Rearranging the letters in order ensures that identical words will look the same.

# Compare the sorted versions of both strings – If they are identical, then the original strings are anagrams. Otherwise, they are not.

# Return the result – If they match, print "The strings are anagrams.", otherwise print "The strings are not anagrams."