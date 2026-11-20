import random

QUESTIONS = [
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Venus", "Mars", "Jupiter", "Mercury"],
        "answer": "Mars",
        "fact": "Mars looks red because iron minerals in its soil oxidize.",
        "difficulty": "easy",
    },
    {
        "question": "What is the largest ocean on Earth?",
        "choices": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific",
        "fact": "The Pacific Ocean covers more area than all Earth's land combined.",
        "difficulty": "easy",
    },
    {
        "question": "Which animal can change the color of its skin?",
        "choices": ["Chameleon", "Penguin", "Elephant", "Panda"],
        "answer": "Chameleon",
        "fact": "Chameleons change color for communication and temperature, not only camouflage.",
        "difficulty": "easy",
    },
    {
        "question": "How many sides does a hexagon have?",
        "choices": ["5", "6", "7", "8"],
        "answer": "6",
        "fact": "Honeycomb cells are shaped like hexagons because they use space efficiently.",
        "difficulty": "easy",
    },
    {
        "question": "Which country is shaped somewhat like a boot?",
        "choices": ["Greece", "Italy", "Spain", "France"],
        "answer": "Italy",
        "fact": "Italy's famous peninsula is located in southern Europe.",
        "difficulty": "easy",
    },
    {
        "question": "What do bees make using nectar?",
        "choices": ["Wax", "Honey", "Silk", "Sap"],
        "answer": "Honey",
        "fact": "Bees store honey as food for the colony.",
        "difficulty": "easy",
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "choices": ["Oxygen", "Hydrogen", "Carbon dioxide", "Nitrogen"],
        "answer": "Carbon dioxide",
        "fact": "Plants use carbon dioxide during photosynthesis to help make food.",
        "difficulty": "medium",
    },
    {
        "question": "What is the fastest land animal?",
        "choices": ["Lion", "Cheetah", "Horse", "Leopard"],
        "answer": "Cheetah",
        "fact": "A cheetah can sprint at roughly 60–70 miles per hour.",
        "difficulty": "medium",
    },
    {
        "question": "Which instrument has keys, hammers, and strings?",
        "choices": ["Violin", "Trumpet", "Piano", "Flute"],
        "answer": "Piano",
        "fact": "A piano creates sound when felt-covered hammers strike strings.",
        "difficulty": "medium",
    },
    {
        "question": "How many continents are generally recognized?",
        "choices": ["5", "6", "7", "8"],
        "answer": "7",
        "fact": "The seven continents are Africa, Antarctica, Asia, Australia, Europe, North America, and South America.",
        "difficulty": "medium",
    },
    {
        "question": "What is the center of an atom called?",
        "choices": ["Nucleus", "Electron", "Molecule", "Cell"],
        "answer": "Nucleus",
        "fact": "An atom's nucleus contains protons and usually neutrons.",
        "difficulty": "medium",
    },
    {
        "question": "Which language is primarily used to write Android apps?",
        "choices": ["Python", "Kotlin", "HTML", "SQL"],
        "answer": "Kotlin",
        "fact": "Kotlin is Google's preferred language for modern Android app development.",
        "difficulty": "medium",
    },
    {
        "question": "What is the freezing point of water in Celsius?",
        "choices": ["0 degrees", "10 degrees", "32 degrees", "100 degrees"],
        "answer": "0 degrees",
        "fact": "Pure water freezes at 0 degrees Celsius under standard atmospheric pressure.",
        "difficulty": "hard",
    },
    {
        "question": "Which sea creature has three hearts?",
        "choices": ["Dolphin", "Octopus", "Shark", "Sea turtle"],
        "answer": "Octopus",
        "fact": "An octopus has two branchial hearts and one systemic heart.",
        "difficulty": "hard",
    },
    {
        "question": "Which scientist developed the three laws of motion?",
        "choices": ["Isaac Newton", "Marie Curie", "Galileo Galilei", "Albert Einstein"],
        "answer": "Isaac Newton",
        "fact": "Newton published his laws of motion in 1687.",
        "difficulty": "hard",
    },
    {
        "question": "What is the smallest prime number?",
        "choices": ["0", "1", "2", "3"],
        "answer": "2",
        "fact": "Two is the only even prime number.",
        "difficulty": "hard",
    },
    {
        "question": "What is the capital of Mongolia?",
        "choices": ["Ulaanbaatar", "Astana", "Tashkent", "Bishkek"],
        "answer": "Ulaanbaatar",
        "fact": "Ulaanbaatar is the coldest capital city in the world.",
        "difficulty": "hard",
    },
    {
        "question": "Which element has the highest electrical conductivity at standard temperature and pressure?",
        "choices": ["Gold", "Silver", "Copper", "Aluminum"],
        "answer": "Silver",
        "fact": "Silver is the most conductive element, followed by copper and gold.",
        "difficulty": "hard",
    },
    {
        "question": "What is the most abundant gas in Earth's atmosphere?",
        "choices": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
        "answer": "Nitrogen",
        "fact": "Nitrogen makes up about 78% of Earth's atmosphere.",
        "difficulty": "hard",
    },
    {
        "question": "Which planet has the most moons?",
        "choices": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Saturn",
        "fact": "As of now, Saturn has 82 confirmed moons, while Jupiter has 79.",
        "difficulty": "hard",
    },
]


STREAK_MESSAGES = {
    2: "Double streak! 🔥",
    3: "Three in a row — unstoppable! ⚡",
    4: "Four-answer combo! 🌟",
    5: "Perfect streak unlocked! 🏆",
}

FUN_CHALLENGES = [
    "Bonus challenge: Say the answer with dramatic movie-trailer energy!",
    "Bonus challenge: Explain the answer in five words!",
    "Bonus challenge: Strike a victory pose before continuing!",
]


def ask_question(number, item):
    print(f"\nQuestion {number}")
    print("~" * 40)
    print(item["question"])

    for index, choice in enumerate(item["choices"], start=1):
        print(f"  {index}. {choice}")

    while True:
        answer = input("Choose 1-4: ").strip()
        if answer in {"1", "2", "3", "4"}:
            selected = item["choices"][int(answer) - 1]
            break
        print("Please enter a number from 1 to 4.")

    if selected == item["answer"]:
        print("✨ Correct!")
        print("Fun fact:", item["fact"])
        return True

    print(f"Not quite — the answer is {item['answer']}.")
    print("Fun fact:", item["fact"])
    return False


def choose_mode():
    print("Choose a quiz mode:")
    print("  1. Progressive adventure (Easy → Medium → Hard)")
    print("  2. Easy")
    print("  3. Medium")
    print("  4. Hard")

    while True:
        choice = input("Choose 1-4: ").strip()
        if choice in {"1", "2", "3", "4"}:
            return choice
        print("Please enter a number from 1 to 4.")


def run_round(difficulty, starting_number=1):
    pool = [item for item in QUESTIONS if item["difficulty"] == difficulty]
    number_of_questions = min(5, len(pool))
    selected_questions = random.sample(pool, number_of_questions)
    score = 0
    streak = 0
    best_streak = 0

    print(f"\n{'=' * 40}")
    print(f"  {difficulty.upper()} ROUND  •  {number_of_questions} questions")
    print("=" * 40)

    for offset, item in enumerate(selected_questions):
        if ask_question(starting_number + offset, item):
            score += 1
            streak += 1
            best_streak = max(best_streak, streak)
            if streak in STREAK_MESSAGES:
                print(STREAK_MESSAGES[streak])
            if streak == 3:
                print(random.choice(FUN_CHALLENGES))
        else:
            streak = 0

    print(f"\n{difficulty.title()} round result: {score}/{number_of_questions}")
    if best_streak >= 2:
        print(f"🔥 Best answer streak: {best_streak}")
    return score, number_of_questions


def choose_next_difficulty():
    print("\nWhere would you like to go next?")
    print("  1. Easy")
    print("  2. Medium")
    print("  3. Hard")
    print("  4. Finish game")

    while True:
        choice = input("Choose 1-4: ").strip()
        if choice in {"1", "2", "3", "4"}:
            return choice
        print("Please enter a number from 1 to 4.")


def play():
    print("=" * 40)
    print("   🌟  THE MYSTERY QUIZ  🌟")
    print("=" * 40)

    name = input("What is your name, explorer? ").strip() or "Explorer"
    mode = choose_mode()

    total_score = 0
    total_questions = 0

    if mode == "1":
        for difficulty in ("easy", "medium", "hard"):
            round_score, round_questions = run_round(
                difficulty,
                starting_number=total_questions + 1,
            )
            total_score += round_score
            total_questions += round_questions

            if difficulty != "hard":
                input("\nPress Enter to continue to the next difficulty...")
    else:
        difficulties = {"2": "easy", "3": "medium", "4": "hard"}
        current_difficulty = difficulties[mode]

        while True:
            round_score, round_questions = run_round(
                current_difficulty,
                starting_number=total_questions + 1,
            )
            total_score += round_score
            total_questions += round_questions

            next_choice = choose_next_difficulty()
            if next_choice == "4":
                break

            current_difficulty = {
                "1": "easy",
                "2": "medium",
                "3": "hard",
            }[next_choice]

    print("\n" + "=" * 40)
    print(f"{name}, you scored {total_score} out of {total_questions}!")

    if total_score == total_questions:
        print("🏆 Perfect! You're a true trivia superstar!")
    elif total_score >= total_questions * 0.6:
        print("🌟 Great job! You know quite a lot!")
    else:
        print("🚀 Good try! Every question teaches something new.")

    print("=" * 40)


if __name__ == "__main__":
    while True:
        play()

        while True:
            replay = input("\nWould you like to play again? (yes/no): ").strip().lower()
            if replay in {"yes", "y"}:
                break
            if replay in {"no", "n"}:
                print("Thanks for playing! 👋")
                raise SystemExit
            print("Please answer 'yes' or 'no'.")