###### import random
from IPython.display import display, HTML

def colorful_message(message, color="black"):
    """Helper to display colorful messages in Jupyter/Colab."""
    display(HTML(f"<p style='color:{color}; font-size:16px;'>{message}</p>"))

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    colorful_message("🎲 Welcome to the Number Guessing Game!", "blue")
    colorful_message("I have chosen a number between 1 and 100. Try to guess it!", "purple")
    
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            attempts += 1
            
            if guess < secret_number:
                colorful_message("Too low! Try a higher number.", "orange")
            elif guess > secret_number:
                colorful_message("Too high! Try a lower number.", "red")
            else:
                colorful_message(f"🎉 Congratulations! You guessed it in {attempts} attempts!", "green")
                break
        except ValueError:
            colorful_message("Please enter a valid number!", "brown")

# Run the game
number_guessing_game()
