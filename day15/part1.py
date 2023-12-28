import sys

def hash_of_string(s):
    val = 0
    for char in s:
        val = ((val + ord(char)) * 17) % 256
    
    return val

strings = sys.stdin.readline().split(',')

print(sum([hash_of_string(s) for s in strings]))