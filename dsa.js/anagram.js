function areAnagrams(str1, str2) {
  // If lengths are different, they can't be anagrams
  if (str1.length !== str2.length) return false;

  // Sort both strings and compare
  return str1.split('').sort().join('') === str2.split('').sort().join('');
}

// Example usage
const str1 = "listen";
const str2 = "silent";

if (areAnagrams(str1, str2)) {
  console.log("The strings are anagrams.");
} else {
  console.log("The strings are not anagrams.");
}


// ## ALGORITHM 

// Take two input strings

// Example: "listen" and "silent".

// Check if both strings have the same length

// If they are of different lengths, they cannot be anagrams.

// Ex: "hello" and "helloo" are not anagrams because they have different lengths.

// Rearrange the letters in both words in alphabetical order

// Convert the string into an array of characters.

// Sort the array alphabetically.

// Convert the sorted array back into a string.

// Ex like this ->

// "listen" → Sort → "eilnst"

// "silent" → Sort → "eilnst"

// Compare the sorted versions of both strings

// If they are identical, the words are anagrams.

// Otherwise, they are not.

//  result-> 

// If they match, print "The strings are anagrams."

// If they don’t match, print "The strings are not anagrams."