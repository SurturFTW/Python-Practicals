# Define a function 
def isPalindrome(string): 
    if len(string) < 1: 
        return True 
    else:
        if string[0] == string[-1]: 
            return isPalindrome(string[1:-1]) 
        else: 
            return False 
 
#Enter input string 
str1 = input("Enter string: ") 
 
if(isPalindrome(str1)==True): 
    print("The string is palindrome.") 
else: 
    print("The string is not palindrome.") 