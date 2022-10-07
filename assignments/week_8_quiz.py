print("\tQuestions \n1.Fastest land mammal? \n2.Fastest reptile ? \n3.Slowest land animal ?")
with open('answers.txt', 'w') as f:
    f.write("\tSolutions \n1. Cheetah. \n2. Black Mamba.\n3. Snail.")
with open("answers.txt") as f:
    contents = f.read()
    print(contents)