# Import the json module to allow us to read and write data in JSON format.
import json

# This function repeatedly prompts for input until an integer is entered.

def input_int(prompt):
    while True:
        value = input(prompt)
        try:
            numResponse = int(value)
            if numResponse > 0:
                break       
        except ValueError:
            print('Invalid input - Try again.')
    return numResponse
    
# This function repeatedly prompts for input until something other than whitespace is entered.

def input_something(prompt):       
    response = input(prompt)
    while not response.strip():
        response = input(prompt)
    return response  
# This function opens "data.txt" in write mode and writes the data to it in JSON format.

def save_data(data_list):
    data = open('data.txt', 'w')
    json.dump(data_list, data)
    data.close()

# Try and open the file here.

try:
    file = open('data.txt', 'r')
    try:
        data = json.load(file)
    except ValueError:
        data = []  
    file.close()
except FileNotFoundError:
    data = []


# Print welcome message, an infinite loop prompts the user for a choice.

print('Welcome to the Quiz Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ')
        
    if choice == 'a':
        # Add a new question.
        
        question = input_something("Enter the question: ")
        ans = []
        while True:
            answer = input_something('Enter a valid answer (enter "q" when done): ')
            if answer == 'q' and len(ans) > 0:
                break
            ans.append(answer.lower())
        
        difficulty = 0 #input_int("Enter question difficulty (1-5): ")
        while True:
            difficulty = input_int('Enter question difficulty (1-5): ')
            if difficulty < 6:
                break
            
        newQuestion = {'questions': question, 'answers': ans, 'difficulty': difficulty}
        data.append(newQuestion)
        save_data(data)
    elif choice == 'l':                
        # List the current questions.
        

        if len(data) == 0:
            print("There are no questions saved.")
        else:
            for count, quest in enumerate(data):
                print(str(count) + ") " + quest['questions'])
    elif choice == 's':
        if len(data) == 0:
            print("No questions saved")
            #break
        search_item = input_something("Enter a search term: ").lower()
        print("Search results:")
        for count, quest in enumerate(data):
            q = quest['questions']
            if search_item in q:               
                print("\t" + str(count) + ") " + quest['questions'])
        # Search the current questions.
    

    elif choice == 'v':
        # View a question.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        if len(data) == 0:
            print("No questions saved")
            #break
        quest_index = 0
        quest_index = input_int("Question number to view: ")
        if  quest_index > len(data) - 1 :
            print("Invalid index number")
            continue
        else:
            requested_question = data[quest_index]
            print("Question:")
            print("  " + requested_question['questions'])
            answer_string = ""
            for a in requested_question['answers']:
                answer_string = answer_string + a + ", "
            answer_string = answer_string[:-2]              
            print("Valid Answers: " + answer_string)
            print("Difficulty: " + str(requested_question['difficulty']))

    elif choice == 'd':
        # Delete a question.

        if len(data) == 0:
            print("No questions saved")
            continue

        quest_index = input_int("Question number to delete: ")
        if  quest_index >= len(data) -1 :
            print("Invalid index number")
            continue
        del data[quest_index]
        save_data(data)

    elif choice == 'q':
        print("Goodbye!")
        break
        # Quit the program.


    else:
        print("invalid choice")

