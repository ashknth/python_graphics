import random

# A simple function to change the perspective of pronouns (for person change)
def change_person(statement):
    # Simple pronoun replacement
    replacements = {
        "I": "you", "me": "you", "my": "your", "am": "are",
        "you": "I", "your": "my", "are": "am"
    }
    words = statement.split()
    changed_words = [replacements.get(word.lower(), word) for word in words]
    return ' '.join(changed_words)

# The main doctor function
def therapist():
    history = []  # To store the patient's statements
    exchanges = 0  # Keep track of the number of exchanges
    print("Therapist: Hello, how can I help you today?")

    while True:
        # Get input from the user (the patient)
        patient_input = input("You: ")

        # Exit condition
        if patient_input.lower() in ["quit", "exit"]:
            print("Therapist: Goodbye!")
            break

        # Add patient input to history
        history.append(patient_input)
        exchanges += 1

        # Every few exchanges, reference an earlier statement
        if exchanges > 5 and random.random() < 0.3 and len(history) > 1:
            earlier_statement = random.choice(history[:-1])  # Choose a random earlier statement
            # Apply person change logic to the earlier statement
            earlier_response = change_person(earlier_statement)
            print(f"Therapist: Earlier you said that '{earlier_response}'. Can you tell me more about that?")
        else:
            # Normal response (apply person change to current statement)
            response = change_person(patient_input)
            print(f"Therapist: {response}?")

# Main function to run the therapist program
if __name__ == "__main__":
    therapist()
