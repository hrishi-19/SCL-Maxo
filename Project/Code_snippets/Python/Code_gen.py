import random
import string

# printing lowercase
letters = string.ascii_lowercase
gencode= ''.join(random.choice(letters) for i in range(11))
