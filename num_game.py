print("I am thinking of a number...")
n = 42
guesses = []
g = int(input("Guess? "))
c = 1
guesses.append(g)

if g == n:
    print("\nWell done! First try!")

while g != n:
    if g < n:
        g = int(input("\nThat number is too small. Guess again? "))
        guesses.append(g)
        c = c + 1
    if g > n:
        g = int(input("\nThat number is too big. Guess again? "))
        guesses.append(g)
        c = c + 1
    if g == n:
        print(f"\nWell done, thats the number! You took {c} guesses:")
        print(sorted(guesses))