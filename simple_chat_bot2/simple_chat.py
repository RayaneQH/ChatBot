import json
from difflib import get_close_matches


def import_data_base(json_path):
    with open(json_path, "r") as json_file:
        data = json.load(json_file)
    return data


def save_data_base(json_path, data):
    with open(json_path, "w") as json_file:
        json.dump(data, json_file, indent=2)


def find_best_match(user_input, questions):
    best_match = get_close_matches(user_input, questions, n=1, cutoff=0.6)
    return best_match[0] if best_match else None


def find_answer(best_match, data):
    for q in data["questions"]:
        if q["question"] == best_match:
            return q["answer"]


def main():
    while True:
        user_input = input("You: ")
        if user_input == "quit":
            exit()
        data = import_data_base("knowledge_base.json")
        question = find_best_match(
            user_input, [q["question"] for q in data["questions"]]
        )
        if question:
            best_answer = find_answer(question, data)
            print("Bot: {}".format(best_answer))
        else:
            print("Bot: I don't know the answer. Can you teach me")
            match input("You: ").lower():
                case "yes":
                    print("Bot: So what is the answer?")
                    best_answer = input("You: ")
                    data["questions"].append(
                        {"question": user_input, "answer": best_answer}
                    )
                    save_data_base("knowledge_base.json", data)
                    print("Bot: Thank you for your help in developing this ChatBot")


main()
