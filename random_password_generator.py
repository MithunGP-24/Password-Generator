
import string
import random

# Get password length from user
password_len = int(input("Enter the password length: "))

# Define the character sets for the password
s1 = string.ascii_lowercase  # Lowercase letters
s2 = string.ascii_uppercase  # Uppercase letters
s3 = string.punctuation      # Special characters
s4 = string.digits           # Digits

# Combine all character sets
s = []
s.extend(s1)
s.extend(s2)
s.extend(s3)
s.extend(s4)

# Shuffle the combined character set
random.shuffle(s)

# Generate the password
password = ''.join(s[:password_len])
print(password)
