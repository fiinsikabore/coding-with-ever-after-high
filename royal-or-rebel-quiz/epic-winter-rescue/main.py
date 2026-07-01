#!/usr/bin/python3
scenarios = [
    {
        "scene": "An eternal winter has swept over the school, called by Crystal Winter's ice magic spiraling out of control. Do you try to calm her down yourself, or alert the teachers immediately?",
        "choices": {
            "a": {"text": "Alert the teachers right away.", "points": "Royal", "danger": -1},
            "b": {"text": "Try to talk to Crystal Winter yourself.", "points": "Rebel", "danger": 2},
        },
    },
    {
        "scene": "Farrah Goodfairy offers to use her fairy magic to fly ahead and scout the worsening storm, but it's risky in this wind. Do you let her go?",
        "choices": {
            "a": {"text": "No, it's too dangerous - find another way.", "points": "Royal", "danger": -1},
            "b": {"text": "Yes, trust her flying skills.", "points": "Rebel", "danger": 2},
        },
    },
    {
        "scene": "The Ice Council has sealed the kingdom's gates to contain the winter curse. Do you respect their authority, or search for a hidden way through?",
        "choices": {
            "a": {"text": "Respect the Ice Council's decision.", "points": "Royal", "danger": 0},
            "b": {"text": "Sneak around and find another way through.", "points": "Rebel", "danger": 2},
        },
    },
    {
        "scene": "Melody Piper's music seems to be the only thing keeping some students calm during the chaos. Do you ask her to keep playing, or pull her away to help evacuate?",
        "choices": {
            "a": {"text": "Ask her to keep playing to maintain calm.", "points": "Royal", "danger": -1},
            "b": {"text": "Pull her away - evacuation matters more right now.", "points": "Rebel", "danger": 1},
        },
    },
    {
        "scene": "A shard of enchanted ice could be the key to reversing the spell, but it's guarded deep inside a frozen cave prone to collapse. Do you go in?",
        "choices": {
            "a": {"text": "No, it's too risky - look for another solution.", "points": "Royal", "danger": -1},
            "b": {"text": "Yes, go in and retrieve it.", "points": "Rebel", "danger": 3},
        },
    },
    {
        "scene": "(Adapted moment) Duchess Swan claims she knows a shortcut through the frozen woods, but she has a reputation for scheming. Do you trust her?",
        "choices": {
            "a": {"text": "No, stick to the known path.", "points": "Royal", "danger": 0},
            "b": {"text": "Yes, take the risk and follow her.", "points": "Rebel", "danger": 2},
        },
    },
    {
        "scene": "Crystal Winter breaks down, blaming herself for the storm. Do you comfort her and help her regain control, or focus on getting everyone to safety first?",
        "choices": {
            "a": {"text": "Focus on getting everyone to safety first.", "points": "Royal", "danger": -1},
            "b": {"text": "Stop to comfort her - she may be the key to stopping this.", "points": "Rebel", "danger": 1},
        },
    },
    {
        "scene": "An avalanche warning sounds near the mountain pass where some students are sheltering. Do you wait for an official rescue team, or lead the group out yourself?",
        "choices": {
            "a": {"text": "Wait for the official rescue team.", "points": "Royal", "danger": -1},
            "b": {"text": "Lead the group out yourself, right now.", "points": "Rebel", "danger": 3},
        },
    },
    {
        "scene": "The only way to break the winter curse for good is a ritual passed down through Crystal Winter's family - but it's never been performed by someone so young. Do you support her doing it, or search for an older, safer method first?",
        "choices": {
            "a": {"text": "Search for an older, tested method first.", "points": "Royal", "danger": -1},
            "b": {"text": "Support her - trust the new approach.", "points": "Rebel", "danger": 2},
        },
    },
    {
        "scene": "With the storm finally breaking, the school wants to hold a big traditional ceremony to celebrate Crystal Winter's role in the rescue. Do you go along with the formal ceremony, or suggest something more low-key and personal instead?",
        "choices": {
            "a": {"text": "Go along with the formal ceremony.", "points": "Royal", "danger": 0},
            "b": {"text": "Suggest something more personal instead.", "points": "Rebel", "danger": 0},
        },
    },
]

def present_scenario(scenario_data):
    print("\n" + scenario_data["scene"])
    for key, choice in scenario_data["choices"].items():
        print(f"  {key}) {choice['text']}")

    answer = input("What do you choose? ").lower()
    while answer not in scenario_data["choices"]:
        answer = input("Please choose a valid option: ").lower()

    chosen = scenario_data["choices"][answer]
    return chosen["points"], chosen["danger"]
def run_mission(scenarios):
    scores = {"Royal": 0, "Rebel": 0}
    danger_level = 5   # starts at a moderate danger level

    for i, scenario_data in enumerate(scenarios, start=1):
        print(f"\n--- Moment {i} of {len(scenarios)} ---")
        print(f"Danger Level: {danger_level}")

        alignment, danger_change = present_scenario(scenario_data)
        scores[alignment] += 1
        danger_level += danger_change

        if danger_level < 0:
            danger_level = 0

        if danger_level >= 10:
            print("\nThe danger has become overwhelming... the mission has failed!")
            return scores, danger_level, False   # False = mission failed

    return scores, danger_level, True   # True = mission survived

def get_outcome(scores, danger_level, survived):
    if not survived:
        return "The winter consumed the school. Mission failed."

    if scores["Royal"] > scores["Rebel"]:
        style = "Royal"
    elif scores["Rebel"] > scores["Royal"]:
        style = "Rebel"
    else:
        style = "Balanced"

    return f"You saved the school with a {style} approach! Final danger level: {danger_level}"

def main():
    print("=== Epic Winter Rescue Mission ===")
    print("An enchanted winter has trapped Ever After High. Every choice matters.\n")

    scores, danger_level, survived = run_mission(scenarios)
    outcome = get_outcome(scores, danger_level, survived)

    print("\n=== Mission Report ===")
    print(f"Royal choices: {scores['Royal']}  |  Rebel choices: {scores['Rebel']}")
    print(outcome)

main()
