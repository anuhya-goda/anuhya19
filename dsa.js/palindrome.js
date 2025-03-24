function isPalindrome(num) {
  let strNum = num.toString();  
  let reversedNum = strNum.split("").reverse().join(""); 
  return strNum === reversedNum; 
}

// Example 
let num = parseInt(prompt("Enter a number: ")); 

if (isPalindrome(num)) {
  console.log(`${num} is a palindrome.`);
} else {
  console.log(`${num} is not a palindrome.`);
}

// ALORITHM : 

// Take a number as input

// Ask the user to enter a number.


// Convert the number into a string

// This makes it easier to check each digit individually.

// Reverse the string 

// Break the string into diff characters.

// Reverse the order of the characters.

// Join them back together to form a reversed string.

// Compare the original and reversed strings

// If both are the same, it means the number is a palindrome.

// Otherwise, it is not a palindrome.

// Display the result

// If the number is a palindrome, print "The number is a palindrome."

// Otherwise, print "The number is not a palindrome."
