import json


# 3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.

input_list = []
user_input_str = None
# user_input_str = input("Write something: ")


# 4) Adjust the logic to load the file content to work with pickled/ json data.
def save_text():
    global user_input_str
    print(user_input_str)
    input_list.append(user_input_str)
    with open('a6.txt', mode='w') as f:
        f.write(json.dumps(input_list))
        f.write('\n')


def load_text():
    with open('a6.txt', mode='r') as f:
        file_content = f.readlines()
        list_state = json.loads(file_content[0])
        for line in list_state:
            print(line)


def user_input():
    global user_input_str
    user_input_str = input("Write something: ")
    print(user_input_str)


# 1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
waiting_for_input = True
while waiting_for_input:
    print('1: save text')
    print('2: load text')
    print('3: write text')
    print('q: exit')
    user_choice = input("Choose an action: ")
    if user_choice == '1':
        save_text()
# 2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
    elif user_choice == '2':
        load_text()
    elif user_choice == '3':
        user_input()
    elif user_choice == 'q':
        waiting_for_input = False
