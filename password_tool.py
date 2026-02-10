"""
Password Security Tool - INFO 153B/253B Lab 1

Analyze password strength and generate secure passwords.

"""

import string
import random

# Common weak passwords
COMMON_PASSWORDS = [
    "123456", "password", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley"
]


# ============================================
# TODO 1: Password Strength Checker
# ============================================

def check_password_strength(password):
    """
    Analyze password and return strength score.
    
    Scoring:
    - 8+ characters: 20 points
    - 12+ characters: 30 points (instead of 20)
    - Has number: 20 points
    - Has uppercase: 20 points
    - Has lowercase: 20 points
    - Has special char (!@#$%): 20 points
    - Not in common list: 10 points
    
    Returns:
        dict with keys: "password", "score", "strength", "feedback"
        
    Strength levels:
    - 0-39: "Weak"
    - 40-69: "Medium"
    - 70-100: "Strong"
    
    Example:
        >>> result = check_password_strength("Hello123!")
        >>> result["score"]
        90
        >>> result["strength"]
        "Strong"
    
    Hint: Use .isdigit(), .isupper(), .islower() and string.punctuation
    """

    score = 0
    feedback = []

    # check length
    
    length = len(password)
    if length >= 12:
        score += 30
    elif length >= 8:
        score += 20
    else:
        feedback.append("Use at least 8 characters")
    
    hasDigit = 0
    hasLower = 0
    hasUpper = 0
    hasSpecial = 0

    for i in password:
        if i.isdigit():
            hasDigit = 20
        if i.isupper():
            hasUpper = 20
        if i.islower():
            hasLower = 20
        if i in ['!','@','#','$','%']:
            hasSpecial = 20

    score += hasDigit + hasUpper + hasLower + hasSpecial

    if hasDigit == 0:
        feedback.append("Add a number")
    if hasUpper == 0:
        feedback.append("Add an uppercase letter")
    if hasLower == 0:
        feedback.append("Add a lowercase letter")
    if hasSpecial == 0:
        feedback.append("Add a special character (!@#$%)")

    # check common passwords
    if password.lower() not in COMMON_PASSWORDS:
        score += 10
    else:
        feedback.append("This is a commonly used password")

    # determine strength level
    if score >= 70:
        strength = "Strong"
    elif score >= 40:
        strength = "Medium"
    else:
        strength = "Weak"

    if len(feedback) == 0:
        feedback.append("Password looks good!")

    return {"password": password, "score": score, "strength": strength, "feedback": feedback}


# ============================================
# TODO 2: Password Generator
# ============================================

def generate_password(length=12, use_special=True):
    """
    Generate a random secure password.
    
    Requirements:
    - Include uppercase, lowercase, and numbers
    - Include special characters if use_special=True
    - Minimum length: 8
    
    Args:
        length: Password length (default 12)
        use_special: Include special characters (default True)
    
    Returns:
        str: Generated password
    
    Example:
        >>> pwd = generate_password(10, True)
        >>> len(pwd)
        10
    
    Hint: Use string.ascii_uppercase, string.ascii_lowercase, 
          string.digits, and random.choice()
    """

    # enforce minimum length
    if length < 8:
        length = 8

    # build the character pool
    charPool = string.ascii_uppercase + string.ascii_lowercase + string.digits
    if use_special:
        charPool += "!@#$%"

    # guarantee at least one of each required type
    password = []
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.digits))
    if use_special:
        password.append(random.choice("!@#$%"))

    # fill the rest with random chars from the pool
    remaining = length - len(password)
    for i in range(remaining):
        password.append(random.choice(charPool))

    # shuffl
    random.shuffle(password)

    result = ""
    for i in password:
        result += i

    return result


# ============================================
# Simple Testing
# ============================================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("PASSWORD SECURITY TOOL - Quick Test")
    print("=" * 60 + "\n")
    
    # Check if functions are implemented
    try:
        # Test TODO 1
        result = check_password_strength("TestPassword123!")
        
        if result is None:
            print("❌ TODO 1 not implemented yet (returned None)")
            print("\nImplement check_password_strength() and try again.\n")
            exit()
        
        if not isinstance(result, dict):
            print("❌ TODO 1 should return a dictionary")
            exit()
        
        required_keys = ["password", "score", "strength", "feedback"]
        missing_keys = [key for key in required_keys if key not in result]
        
        if missing_keys:
            print(f"❌ TODO 1 missing keys in return dict: {missing_keys}")
            exit()
        
        print("✓ TODO 1 implemented - returns correct structure")
        print(f"  Example: '{result['password']}' → {result['strength']} ({result['score']}/100)")
        
        # Test TODO 2
        pwd = generate_password(12, True)
        
        if pwd is None:
            print("\n❌ TODO 2 not implemented yet (returned None)")
            print("\nImplement generate_password() and try again.\n")
            exit()
        
        if not isinstance(pwd, str):
            print("\n❌ TODO 2 should return a string")
            exit()
        
        print(f"\n✓ TODO 2 implemented - generates passwords")
        print(f"  Example: '{pwd}' (length: {len(pwd)})")
        
        # Success!
        print("\n" + "=" * 60)
        print("✅ Both functions implemented!")
        print("=" * 60)
        print("\nRun the full test suite to verify correctness:")
        print("  python test_password_tool.py")
        print()
        
    except AttributeError as e:
        print(f"❌ Error: {e}")
        print("\nMake sure both functions are defined.\n")
    except Exception as e:
        print(f"❌ Error running functions: {e}")
        print("\nCheck your implementation and try again.\n")