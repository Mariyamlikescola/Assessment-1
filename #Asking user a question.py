# Defining a dictionary of countries and their capitals
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Netherlands": "Amsterdam",
    "Belgium": "Brussels",
    "Sweden": "Stockholm",
    "Norway": "Oslo",
    "Portugal": "Lisbon",
    "Austria": "Vienna"
}

# Looping through the dictionary to ask questions to user for quiz.
for country, capital in capitals.items():
    user_answer = input(f"What is the capital of {country}? ").strip()
    
    #Checking if answer is correct or wrong.
    if user_answer.lower() == capital.lower():
        print("Your answer is correct! +1 point")
    else:
        print(f" Your answer is wrong! The capital of {country} is {capital}.")
#Finishing quiz.
print("Quiz completed!")


        