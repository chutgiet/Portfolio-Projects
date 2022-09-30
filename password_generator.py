# ~Code with Dau Giet

import random
import string


size = int(input("Password Length: "))

# randomly choose a upper case letter
char = [random.choice(string.ascii_uppercase)]

# Make half/half+1 of all characters alphabetical
for i in range(0, (size - size//2)):
    char.append(random.choice(string.ascii_lowercase))
# Make remaining values-1 random numbers between 0-9
for i in range(0, size//2):
    char.append(str(random.randint(0, 9)))

# End with a non-alphanumeric character
non_alphanumeric = [".", "!", "_", "@", "#", "%", "()", "/", ">", "<"]
char.append(random.choice(non_alphanumeric))
# if password is too long, generate 1 more different non-alphanumeric characters
while size > 7:
    last = random.choice(non_alphanumeric)
    if last not in char:
        char.append(last)
        break
    else:
        continue

# Shuffle list content before final password
random.shuffle(char)
# join the list items into a password
password_generated = ''.join(char)


print("Your Password:", password_generated)
