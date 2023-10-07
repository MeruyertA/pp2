n = int(input())
all_n = set(range(1, n + 1))
possible = all_n
while True:
    guess = input()
    if guess == 'HELP':
        break
    guess = {int(x) for x in guess.split()}
    answer = input()
    if answer == 'YES':
        possible &= guess
    else:
        possible &= all_n - guess

print(' '.join([str(x) for x in sorted(possible)]))