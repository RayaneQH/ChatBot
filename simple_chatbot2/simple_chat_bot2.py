import json
from difflib import get_close_matches


def import_knowledge_base(json_path):
    with open(json_path, "r") as json_file:
        data = json.load(json_file)
    return data


def save_knowledge_base(json_path, data):
    with open(json_path, "w") as json_file:
        json.dump(data, json_file, indent=2)


def find_best_matches(user_question, questions):
    best_match = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return best_match[0] if best_match else None


def find_answer(best_match, data):
    for q in data["questions"]:
        if q["question"] == best_match:
            return q["answer"]


def main():
    while True:
        user_input = input("You: ")
        data = import_knowledge_base("Knowledge_base.json")
        best_match = find_best_matches(
            user_input, [q["question"] for q in data["questions"]]
        )
        if best_match != None:
            answer = find_answer(best_match, data)
            print(f"Bot: {answer}")
        else:
            print("Bot: I don't know the answe, can you teach me?")
            match input("You:").lower():
                case "yes":
                    print("Bot: So what is the answer?")
                    answer = input("You: ")
                    data["questions"].append({"question": user_input, "answer": answer})
                    save_knowledge_base("Knowledge_base.json", data)
                    print("Bot: Thank you I have learnt something new")
                case "no":
                    print("Bot: Thank you")
                case _:
                    print("Bot: Invalid input")


main()
