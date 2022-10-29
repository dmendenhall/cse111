from sentences import get_determiner, get_noun, get_prepositional_phrase, get_verb, get_preposition, get_prepositional_phrase
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    # 1. Test the single nouns.

    single_nouns = ["bird", "boy", "car", "cat", "child",
                    "dog", "girl", "man", "rabbit", "woman"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_noun function which
        # should return a single noun.
        word = get_noun(1)

        # Verify that the word returned from get_nouns
        # is one of the words in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ["birds", "boys", "cars", "cats", "children",
                    "dogs", "girls", "men", "rabbits", "women"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from get_noun
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns


def test_get_verb():
    # 1. Test the past verbs.

    past_verbs = ["drank", "ate", "grew", "laughed",
                  "thought", "ran", "slept", "talked", "walked", "wrote"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_verb function which
        # should return a past verb.
        word = get_verb(1, "past")

        # Verify that the word returned from get_verbs
        # is one of the words in the past_verbs list.
        assert word in past_verbs

    # 2. Test the single present verbs.

    single_present_verbs = ["drinks", "eats", "grows", "laughs",
                            "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a single present verb.
        word = get_verb(1, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the single_present_verbs list.
        assert word in single_present_verbs

    # 3. Test the plural present verbs.

    plural_present_verbs = ["drink", "eat", "grow", "laugh",
                            "think", "run", "sleep", "talk", "walk", "write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a plural present verb.
        word = get_verb(2, "present")

        # Verify that the word returned from get_verb
        # is one of the words in the plural_present_verbs list.
        assert word in plural_present_verbs

    # 4. Test the future verbs.

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
                    "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_verb function which
        # should return a future verb.
        word = get_verb(1, "future")

        # Verify that the word returned from get_verb
        # is one of the words in the plural_past_verbs list.
        assert word in future_verbs


def test_get_preposition():
    # 1. Test the prepositions.

    prepositions = ["about", "above", "across", "after", "along",
                    "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for",
                    "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over",
                    "past", "to", "under", "with", "without"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_preposition function which
        # should return a preposition.
        word = get_preposition()

        # Verify that the word returned from get_preposition
        # is one of the words in the prepositions list.
        assert word in prepositions


def test_get_prepositional_phrase():
    # 1. Test the get prepositional phrase.

    phrase = get_prepositional_phrase(random.randint(1, 2))

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_preposition function which
        # should return a preposition.

        phrase_list = phrase.split(" ")

        phrase_length = len(phrase_list)

    # Verify that the word returned from get_preposition
    # is one of the words in the prepositions list.
        assert phrase_length == 3


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
