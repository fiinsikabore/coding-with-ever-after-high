#!/usr/bin/python3
questions = [
    {
        "question": "Legacy Day is here. The Storybook of Legends is open. Do you sign it?",
        "choices": {
            "a": {"text": "Yes, it's my destiny.", "points": "Royal"},
            "b": {"text": "No, I choose my own path.", "points": "Rebel"},
        },
    },
    {
        "question": "How do you feel about your parent's story repeating with you?",
        "choices": {
            "a": {"text": "Excited, it's an honor.", "points": "Royal"},
            "b": {"text": "Uneasy, I want something different.", "points": "Rebel"},
        },
    },
    {
        "question": "The Dragon Games are starting. How do you want to compete?",
        "choices": {
            "a": {"text": "Follow the traditional rules and prove myself the classic way.", "points": "Royal"},
            "b": {"text": "Find a clever workaround nobody's tried before.", "points": "Rebel"},
        },
    },
    {
        "question": "You're invited to a royal ball. What's your reaction?",
        "choices": {
            "a": {"text": "Thrilled — I love royal traditions.", "points": "Royal"},
            "b": {"text": "I'd rather skip it and do something unexpected instead.", "points": "Rebel"},
        },
    },
    {
        "question": "An enchanted winter has trapped the school (Epic Winter). What's your move?",
        "choices": {
            "a": {"text": "Trust that a hero will come save everyone, like in the old tales.", "points": "Royal"},
            "b": {"text": "Take charge and find a new way to break the spell myself.", "points": "Rebel"},
        },
    },
    {
        "question": "You fall down a rabbit hole into Wonderland. What do you do?",
        "choices": {
            "a": {"text": "Look for a way back to the world I know.", "points": "Royal"},
            "b": {"text": "Explore — this is exactly the kind of adventure I want.", "points": "Rebel"},
        },
    },
    {
        "question": "Spring is unsprung and the seasons are out of balance. How do you respond?",
        "choices": {
            "a": {"text": "Follow the old rituals to restore order.", "points": "Royal"},
            "b": {"text": "Question whether the old rituals even make sense anymore.", "points": "Rebel"},
        },
    },
    {
        "question": "Your roommate has the opposite destiny alignment as you. How do you feel?",
        "choices": {
            "a": {"text": "It's fine, everyone has their own story to follow.", "points": "Royal"},
            "b": {"text": "It makes me want to fight for the right to choose, for both of us.", "points": "Rebel"},
        },
    },
    {
        "question": "There's a school tradition you personally don't agree with. What do you do?",
        "choices": {
            "a": {"text": "Follow it anyway — traditions matter.", "points": "Royal"},
            "b": {"text": "Speak up and try to change it.", "points": "Rebel"},
        },
    },
    {
        "question": "You're offered a shortcut that skips a key part of your parent's story. Do you take it?",
        "choices": {
            "a": {"text": "No, I want the full story exactly as it was written.", "points": "Royal"},
            "b": {"text": "Yes, why suffer through something I can avoid?", "points": "Rebel"},
        },
    },
    {
        "question": "Thronecoming is approaching. What matters most to you about it?",
        "choices": {
            "a": {"text": "Being crowned and celebrated like royalty.", "points": "Royal"},
            "b": {"text": "Having fun and being myself, crown or not.", "points": "Rebel"},
        },
    },
    {
        "question": "A magic mirror shows you your future exactly as your story dictates. Your reaction?",
        "choices": {
            "a": {"text": "Relief — I know exactly what to expect.", "points": "Royal"},
            "b": {"text": "Frustration — I want an unwritten future.", "points": "Rebel"},
        },
    },
    {
        "question": "You're chosen to give a speech about your family's legacy. What do you say?",
        "choices": {
            "a": {"text": "I'm proud to carry on what my parents started.", "points": "Royal"},
            "b": {"text": "I'll honor where I come from, but I'm writing my own ending.", "points": "Rebel"},
        },
    },
    {
        "question": "The school debates changing the rules around Legacy Day. Where do you stand?",
        "choices": {
            "a": {"text": "The old system works — it shouldn't change.", "points": "Royal"},
            "b": {"text": "Everyone deserves a choice — it's time for change.", "points": "Rebel"},
        },
    },
    {
        "question": "At the end of the day, what matters most to you?",
        "choices": {
            "a": {"text": "Honoring my story and the legacy before me.", "points": "Royal"},
            "b": {"text": "Writing a story that's truly, completely mine.", "points": "Rebel"},
        },
    },
]


def ask_question(question_data):
    print(question_data["question"])
    for key, choice in question_data["choices"].items():
        print(f"  {key}) {choice['text']}")

    answer = input("Your answer: ").lower()
    while answer not in question_data["choices"]:
        answer = input("Please choose a valid option: ").lower()

    return question_data["choices"][answer]["points"]

def run_quiz(questions):
    scores = {"Royal": 0, "Rebel": 0}

    for question_data in questions:
        result = ask_question(question_data)
        scores[result] += 1

    return scores

def get_result(scores):
    if scores["Royal"] > scores["Rebel"]:
        return "Royal"
    elif scores["Rebel"] > scores["Royal"]:
        return "Rebel"
    else:
        return "Neutral — a true Royal Rebel!"

def main():
        print("=== Royal or Rebel? ===")
        scores = run_quiz(questions)
        result = get_result(scores)
        print(f"\nYour result: {result}")
        print(f"Final scores: {scores}")

main()
