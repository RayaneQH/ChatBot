def check_propability(user_words, words, required_word=[], single_response=False):
    has_required_words = True
    word_propability = 0
    for word in user_words:
        if word in words:
            word_propability += 1
    for r_word in required_word:
        if r_word not in user_words:
            has_required_words = False
            break
    propability = float(word_propability) / float(len(words))
    if has_required_words or single_response:
        return int(propability * 100)
    else:
        return 0


def check_words(user_words: list):
    dict_of_propability = {}

    def response(bot_output, words, required_word=[], single_response=False):
        dict_of_propability[bot_output] = check_propability(
            user_words, words, required_word, single_response
        )

    response("hello", ["hello", "hey", "hi", "I'am new here"], single_response=True)
    response("Fine and you", ["how", "are", "you"], required_word=["how"])
    the_output = max(dict_of_propability, key=dict_of_propability.get)
    return the_output


def get_response(user_input: str):
    import re

    user_words = re.split(r"\s+|[,.;:!?-]\s*", user_input.lower())
    print(user_words)
    response = check_words(user_words)
    return response


def main():
    while True:
        print(f"Bot: {get_response(input('You: '))}")


main()
