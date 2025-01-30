#    GNU GENERAL PUBLIC LICENSE
#    Version 2, June 1991


import random
import customtkinter as ctk #The Gui Libuary
import os
def about():
    # Create a new top-level window for the "About" section
    about = ctk.CTkToplevel()
    about.title("About:")
    about.geometry("350x200")
    about.resizable(False,False)
    about.attributes('-topmost', 'true')


    # Add content to the about window
    about_label = ctk.CTkLabel(about, text="Rock Paper Scissors Game:", font=("Ubuntu",26, "underline"))
    about_label.pack(pady=10)

    version_label = ctk.CTkLabel(about, text="Version: 1.0", font=("Ubuntu", 16))
    version_label.pack(pady=5)

    author_label = ctk.CTkLabel(about, text="Developer: Jonathan Steadman", font=("Ubuntu", 16))
    author_label.pack(pady=5)

# Define the game logic
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "IT IS A DRAW!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        return "YOU WIN!"
    else:
        return "COMPUTER WIN!"

# Function to handle player choice
def play(player_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(player_choice, computer_choice)
    # Update the GUI with the result
    computer_choice_label.configure(text=f"Computer has chosen: {computer_choice}.")
    player_choice_label.configure(text=f"You have chosen: {player_choice}.")
    result_label.configure(text=f"{result}")

# Initialize the mcomputern window
app = ctk.CTk()
app.title("Rock Paper Scissors Game For Linux")
app.geometry("400x430")
app.resizable(False,False)

# Set the theme for the application
ctk.set_appearance_mode("dark")  #The application is in Dark mode
ctk.set_default_color_theme("green")  

#Navigation Bar - About section.
nav = ctk.CTkFrame(app,height=40, corner_radius= 0)
nav.pack(fill="x",side="top")
about = ctk.CTkButton(nav, text="About", width=80, fg_color="transparent", hover_color="#333333", command=about)
about.pack(side="left", padx=5, pady=5)
# Create and place widgets
title_label = ctk.CTkLabel(app, text="Rock Paper Scissors Game:", font=("Ubuntu", 30, "underline"))
title_label.pack(pady=10)

# Buttons for player choices
rock_button = ctk.CTkButton(app, text="Rock",height=60,font=("Ubuntu",20), command=lambda: play("Rock"))
rock_button.pack(pady=5)

paper_button = ctk.CTkButton(app, text="Paper",height=60,font=("Ubuntu",20), command=lambda: play("Paper"))
paper_button.pack(pady=5)

scissors_button = ctk.CTkButton(app, text="Scissors",font=("Ubuntu",20),height=60, command=lambda: play("Scissors"))
scissors_button.pack(pady=5)

# Label to display the result
result_label = ctk.CTkLabel(app, text="", font=("Ubuntu", 25, "underline"))
result_label.pack(pady=5)

player_choice_label = ctk.CTkLabel(app, text="", font=("Ubuntu", 20))
player_choice_label.pack(pady=5)

computer_choice_label = ctk.CTkLabel(app, text="", font=("Ubuntu", 20))
computer_choice_label.pack(pady=5)


# Run the application
app.mainloop()