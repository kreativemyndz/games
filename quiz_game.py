import random
#the question
question=["Faith is","the substance","of things","hoped for",",the evidence","of things","not seen."]

chosen_phrase=random.choice(question)
chosen_phrase=chosen_phrase.upper()

vowels=["A","E","I","O","U","","'"]
puzzle=""
 
for l in chosen_phrase:
	if not l in vowels:
		puzzle+=l


puzzle_with_spaces=""


while len(puzzle)>0:
	group_length=random.randint(1,5)
	puzzle_with_spaces+=puzzle[:group_length]+" "
	puzzle=puzzle[group_length:]

	print("Hebrews 11:1 - Guess what part of the vesre is below")
	print(puzzle_with_spaces)
	guess=input("What is your guess?  ")
	guess=guess.upper()

	if guess == chosen_phrase:
        print("That's correct!")
	else:
        print("No that is the wrong answer, the answer is ", chosen_phrase)
	continue
