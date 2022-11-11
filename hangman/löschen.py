# delete every word bigger than 5 letters in wordlist-german.txt
# and write it in wordlist-german-new.txt

import re

with open('wordlist-german.txt', 'r') as f:
    with open('wordlist-german-new.txt', 'w') as f2:
        for line in f:
            if len(line) <= 3:
                f2.write(line)
