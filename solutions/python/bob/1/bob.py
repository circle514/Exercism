def response(hey_bob):
    hey_bob = hey_bob.rstrip()
    question = hey_bob.endswith("?")
    scream = hey_bob.isupper()
    empty = True if len(hey_bob) == 0 else False

    if question and scream:
        return "Calm down, I know what I'm doing!"
    if question:
        return "Sure."
    if scream:
        return "Whoa, chill out!"
    if empty:
        return "Fine. Be that way!"
    return "Whatever."
