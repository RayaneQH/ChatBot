def check_propability(
    all_words, reqegnizerd_word, required_words=[], single_response=False
):
    has_required_words = True
    word_certenty = 0
    for word in all_words:
        if word in reqegnizerd_word:
            word_certenty += 1
    propability = float(word_certenty) / float(len(reqegnizerd_word))
    for r_word in required_words:
        if r_word not in all_words:
            has_required_words = False
            break
    if single_response or has_required_words:
        return int(propability * 100)
    else:
        return 0


def check_all_words(user_words):
    dict_of_propability = {}

    def response(
        Bot_responce, reqegnizerd_word, required_words=[], single_response=False
    ):
        nonlocal dict_of_propability
        dict_of_propability[Bot_responce] = check_propability(
            user_words, reqegnizerd_word, required_words, single_response
        )

    response("hello", ["hello", "hey", "hi"], single_response=True)
    response("I'm fine and you ?", ["how", "are", "you"], required_words=["how"])
    response("Exit", ["turnoff", "exit"], single_response=True)
    highest = max(dict_of_propability, key=dict_of_propability.get)
    return highest


def get_responce(message):
    import re

    user_words = re.split(r"\s+|[{,.;:!-?}]\s*", message.lower())
    print(user_words)
    responce = check_all_words(user_words)
    return responce


def main():
    while True:
        print(f"Bot: {get_responce(input('You:'))}")


main()
