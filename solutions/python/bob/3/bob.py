"""
    robot bob responses (this guy has to be ai generated)
"""
def response(hey_bob):
    """
        bob is a weirdo and only responds to questions or screams (or maybe both!) and if they arent he acts all cool
        professional larper

        Params:
            hey_bob: (str) what we tell bob

        Return:
            bob_response: (str) what he tells us after hey_bob
    """
    hey_bob = hey_bob.rstrip()
    question = hey_bob.endswith("?")
    scream = hey_bob.isupper()
    empty = len(hey_bob) == 0 

    if question and scream:
        return "Calm down, I know what I'm doing!"
    if question:
        return "Sure."
    if scream:
        return "Whoa, chill out!"
    if empty:
        return "Fine. Be that way!"
    return "Whatever."
