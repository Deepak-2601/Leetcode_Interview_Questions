def getHint(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return f"{bulls}A{cows}B"

secret = "1807"
guess = "7810"
result = getHint(secret, guess)
print(result)