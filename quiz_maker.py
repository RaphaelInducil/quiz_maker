# raphael clouiee inducil
# BSCpE 1-2 
# 04-07-25
# assignment 9: this program will ask you to give questions and four different answers
# with one of them being the correct answer and the other three being wrong. 

# while loop
# ask for the name of the quiz
while True:
    with open(input("Enter name of your quiz: " + ".txt")) as file:

    # input questions
    # input answers
    # input correct answer
        question = input("Enter your question: ")
        answer_a = input("Enter answer A: ")
        answer_b = input("Enter answer B: ")
        answer_c = input("Enter answer C: ")
        answer_d = input("Enter answer D: ")
        correct_answer = input("Enter the correct answer: ")

# make a file for the questions and answers to be stored in.
        file.write("Question: " + question + "\n")
        file.write("A: " + answer_a + "\n")
        file.write("B: " + answer_b + "\n")
        file.write("C: " + answer_c + "\n")
        file.write("D: " + answer_d + "\n")
        file.write("Correct Answer: " + correct_answer + "\n")
        file.write("\n")

# ask if done, if conditions yes or no, break or continue loop
        done = input("do you want to input another question? (yes/no): ")
        if done.lower() == "no":
            break
        elif done.lower() == "yes":
            continue
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            break