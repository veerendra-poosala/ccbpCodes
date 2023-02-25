#RemoveTheLastItems

programming_languages = ['Python', 'C', 'Java', 'Ruby', 'C++', 'CSS', 'HTML', 'Bash', 'Perl', 'R', 'Swift', 'SQL', 'PHP', 'JavaScript']
# Write your code here
n = int(input())

for i in range(n):
    programming_languages.pop()

print(programming_languages)