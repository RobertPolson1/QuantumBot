import random

# Sample knowledge graph represented as a dictionary
knowledge_graph = {
    "Python": {
        "type": "programming language",
        "creator": "Guido van Rossum",
        "year": 1991,
        "paradigm": "object-oriented, imperative, functional"
    },
    "Java": {
        "type": "programming language",
        "creator": "James Gosling",
        "year": 1995,
        "paradigm": "object-oriented"
    },
    "Einstein": {
        "type": "scientist",
        "field": "theoretical physics",
        "famous_for": "theory of relativity",
        "year_of_birth": 1879 # 20
    },
    "Beethoven": {
        "type": "composer",
        "famous_for": "symphonies",
        "year_of_birth": 1770,
        "nationality": "German"
    }
}

def get_random_topic():
    """Select a random topic from the knowledge graph."""
    return random.choice(list(knowledge_graph.keys()))

def generate_question(topic):
    """Generate a trivia question based on the selected topic."""
    if topic not in knowledge_graph:
        return None, None
    
    info = knowledge_graph[topic]
    question_type = random.choice(list(info.keys()))
    
    if question_type == "creator":
        return f"Who is the creator of {topic}?", info[question_type]
    elif question_type == "year":
        return f"In what year was {topic} created?", info[question_type]
    elif question_type == "famous_for":
        return f"What is {topic} famous for?", info[question_type]
    elif question_type == "nationality":
        return f"What is the nationality of {topic}?", info[question_type]
    else:
        return None, None

def ask_question(question, answer):
    """Ask the user a question and check their answer."""
    user_answer = input(question + "\nYour answer: ")
    return user_answer.strip().lower() == str(answer).strip().lower()

def play_round():
    """Play a single round of trivia."""
    topic = get_random_topic()
    question, answer = generate_question(topic)
    
    if question:
        if ask_question(question, answer):
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer is: {answer}")
            return False
    else:
        print("No question generated.") # 71
        return False

def trivia_game():
    """Main function to run the trivia game."""
    score = 0
    rounds = 5
    
    print("Welcome to the Trivia Game!")
    
    for _ in range(rounds):
        if play_round():
            score += 1
    
    print(f"Game over! Your score: {score}/{rounds}")

if __name__ == "__main__":
    trivia_game()

