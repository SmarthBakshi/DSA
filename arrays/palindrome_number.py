def is_palindrome(x: int) -> bool:
    if x < 0:
        return False
    
    return str(x) == str(x)[::-1]

if __name__ == "__main__":
    print(is_palindrome(121))  # True
    print(is_palindrome(-121)) # False
    print(is_palindrome(10))   # False
    print(is_palindrome(12321))# True