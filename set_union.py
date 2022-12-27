# Enter your code here. Read input from STDIN. Print output to STDOUT
english_size = int(input())
english = set(map(int,input().split(' ')))
french_size = int(input())
french = set(map(int,input().split(' ')))
only_english = {}
only_english = english.union(french)
print(len(only_english))
