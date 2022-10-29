# Using VS Code, create a new file, import the random module at the top of the file, and save the file as sentences.py

# The standard Python random module includes a function named choice that will randomly choose
# one element from a list and return that element. The choice function is easy to call like this:

import random

# Create a list of strings and assign
# the list to a variable named words.
words = ["boy", "girl", "cat", "dog", "bird", "house"]

# Call the random.choice function which will choose
# one string from the words list. Store the chosen
# string in a variable named word.
word = random.choice(words)


def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "some", "many".
    If quantity == 1, this function will return either "a",
    "one", or "the". Otherwise this function will return
    either "some", "many", or "the".

    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        "bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of
    these ten plural nouns:
        "birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"

    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child",
                 "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children",
                 "dogs", "girls", "men", "rabbits", "women"]

    # Randomly choose and return a noun.
    noun = random.choice(nouns)
    return noun


def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past",
    this function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
                 "ran", "slept", "talked", "walked", "wrote"]

    if tense == "present" and quantity == 1:
        verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                 "runs", "sleeps", "talks", "walks", "writes"]

    if tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think",
                 "run", "sleep", "talk", "walk", "write"]

    if tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think",
                 "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = random.choice(verbs)
    return verb


def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """
    words = ["about", "above", "across", "after", "along",
             "around", "at", "before", "behind", "below",
             "beyond", "by", "despite", "except", "for",
             "from", "in", "into", "near", "of",
             "off", "on", "onto", "out", "over",
             "past", "to", "under", "with", "without"]

    # Randomly choose and return a preposition.
    word = random.choice(words)
    return word


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or pluaral.
    Return: a prepositional phrase.
    """
    prepositional_phrase = get_preposition() + " " + get_determiner(
        quantity) + " " + get_noun(quantity)
    return prepositional_phrase


def main():
    # single past
    print(get_determiner(1).capitalize(), get_noun(1), get_verb(
        1, "past"), get_prepositional_phrase(1) + ".")

    # single present
    print(get_determiner(1).capitalize(), get_noun(
        1), get_verb(1, "present"), get_prepositional_phrase(1) + ".")

    # single future
    print(get_determiner(1).capitalize(),
          get_noun(1), get_verb(1, "future"), get_prepositional_phrase(1) + ".")

    # plural past
    print(get_determiner(2).capitalize(),
          get_noun(2), get_verb(1, "past"), get_prepositional_phrase(2) + ".")

    # plural present
    print(get_determiner(2).capitalize(), get_noun(
        2), get_verb(2, "present"), get_prepositional_phrase(2) + ".")

    # plural future
    print(get_determiner(2).capitalize(),
          get_noun(2), get_verb(1, "future"), get_prepositional_phrase(2) + ".")


def exceeds_main():
    # single past
    print(get_determiner(1).capitalize(), get_noun(1), get_verb(
        1, "past"), get_prepositional_phrase(1), get_prepositional_phrase(1) + ".")

    # single present
    print(get_determiner(1).capitalize(), get_noun(
        1), get_verb(1, "present"), get_prepositional_phrase(1), get_prepositional_phrase(1) + ".")

    # single future
    print(get_determiner(1).capitalize(),
          get_noun(1), get_verb(1, "future"), get_prepositional_phrase(1), get_prepositional_phrase(1) + ".")

    # plural past
    print(get_determiner(2).capitalize(),
          get_noun(2), get_verb(1, "past"), get_prepositional_phrase(2), get_prepositional_phrase(2) + ".")

    # plural present
    print(get_determiner(2).capitalize(), get_noun(
        2), get_verb(2, "present"), get_prepositional_phrase(2), get_prepositional_phrase(2) + ".")

    # plural future
    print(get_determiner(2).capitalize(),
          get_noun(2), get_verb(1, "future"), get_prepositional_phrase(2), get_prepositional_phrase(2) + ".")


if __name__ == "__main__":
    main()
    print()
    exceeds_main()
