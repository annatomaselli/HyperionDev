# CREATE A PROGRAM FOR A SMALL BUSINESS TO HELP THEM MANAGE TASKS ASSIGNED TO EACH TEAM MEMBER

#=====importing libraries===========
'''This is the section where you will import libraries'''

#====Login Section====
# Write code that will allow a user to login

username = input("Please enter your username: ")
password = input("Please enter your password: ")
print()
allowed_username_list = []
allowed_password_list = []

# for line in txt file: split the line where there is a whitespace and remove comma, then store first (=username) or second(=password) word into a variable, append into list
with open('user.txt', 'r') as file:     # r for read only
    for line in file.readlines():       # readlines() returns a list of all the lines in the txt file
        allowed_username = line.split()[0]  # break a string into a list of words separated by a whitespace, and only considers the first element
        allowed_username = allowed_username.strip(',') #strip away the comma at the end of the username from the user.txt file. This and the command before can be done together, but I'll keep this for now.
        allowed_password = line.split()[1]
        allowed_username_list.append(allowed_username)
        allowed_password_list.append(allowed_password)

#Use a while loop to validate your username and password: check whether they are allowed. otherwise, display error message
while username not in allowed_username_list:
    print("Error: you entered an invalid username or password. Try again.")
    print()
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")

print()

while username == 'admin':
    # presenting the menu to the user and making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    s - display statistics
    e - Exit
    : ''').lower()

    if menu == 'r':
        pass
        print()
        new_username = input("Please enter a new username: ")  # Request input of a new username
        if new_username in allowed_username_list:  # check if username already exists
            print("Error: this username already exists. Please enter a new one.")
            print()
            new_username = input("Please enter a new username: ")

        new_password = input("Please enter your new password: ")  # Request input of a new password
        confirm_password = input("Please confirm your new password: ")
        while new_password != confirm_password:  # Check if the new password and confirmed password are the same.
            print(
                "Error: the two passwords do not correspond. Please enter your password again.")  # if they are not, display error message
            confirm_password = input("Please confirm your new password: ")

        # if the two passwords are the same, add the new username / password to the user.txt file
        with open('user.txt', 'a') as file:  # opens the file for writing, appending (a) the inserted data to the end
            file.write('\n' + new_username + ', ' + new_password)  # use \n to create a new line
        print()

    elif menu == 'a':
        pass  # allow a user to add a new task to task.txt file
        print()
        username_assigned = input("Please enter the name of the user that you want to assign the task to: ")
        task_title = input("Please enter the title of the task: ")
        task_description = input("Please enter the task description: ")
        task_duedate = input("Please enter the due date of the task (in the following format: 01 Jan 2000): ")
        today_date = input("Please enter today's date (in the following format: 01 Jan 2000): ")

        # Add the data to the file task.txt with 'No' at the end to indicate that the task isn't yet completed
        with open('tasks.txt', 'a') as file:  # opens the file for writing, appending (a) the inserted data to the end
            file.write(
                '\n' + username_assigned + ', ' + task_title + ', ' + task_description + ', ' + today_date + ', ' + task_duedate + ', ' + 'No')
        print()


    elif menu == 'va':
        pass  # read the task from task.txt file and print to the console in the format of Output 2 in the task PDF
        print()
        with open('tasks.txt', 'r') as file:  # r for read only
            for line in file.readlines():
                task_content = line.rstrip().split(', ')  # use rstrip to remove trailing whitespaces and newlines
                print("Task:".ljust(20) + task_content[
                    1])  # use str.ljust() to left-align the content of each line at a fixed width of 20 characters, to make sure that the formatting is aligned correctly
                print("Assigned to:".ljust(20) + task_content[0])
                print("Date assigned:".ljust(20) + task_content[3])
                print("Due date:".ljust(20) + task_content[4])
                print("Task complete?".ljust(20) + task_content[5])
                print("Task description:")
                print("  {}".format(task_content[2]))
                print()


    elif menu == 'vm':
        pass
        print()
        with open('tasks.txt', 'r') as file:
            for line in file.readlines():  # Read a line from the file
                task_content = line.rstrip().split(', ')  # Split the line where there is comma and space.
                if username == task_content[
                    0]:  # Check if the username of the person logged in is the same as the username you have read from the file.
                    print("Task:".ljust(20) + task_content[1])
                    print("Assigned to:".ljust(20) + task_content[0])
                    print("Date assigned:".ljust(20) + task_content[3])
                    print("Due date:".ljust(20) + task_content[4])
                    print("Task complete?".ljust(20) + task_content[5])
                    print("Task description:")
                    print("  {}".format(task_content[2]))
                    print()

    elif menu == 's':
        print()
        user_counter = 0    #initialise variables
        task_counter =0
        with open('tasks.txt', 'r') as file:
            for line in file.readlines():
                task_counter += 1
        with open('user.txt', 'r') as file:
            for line in file.readlines():
                user_counter += 1

        print("Number of users:", user_counter)
        print("Number of tasks:", task_counter)
        print()

    elif menu == 'e':
        print()
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")


#=======NOW FOR THE OTHER USERS=======
while username != 'admin':
    #presenting the menu to the user and making sure that the user input is converted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':   #allow access to register new profiles to admin only
        print("Sorry, you do not have permissions to register a new user.")
        print()

    elif menu == 'a':
        pass            # allow a user to add a new task to task.txt file
        print()
        username_assigned = input("Please enter the name of the user that you want to assign the task to: ")
        task_title = input("Please enter the title of the task: ")
        task_description = input("Please enter the task description: ")
        task_duedate = input("Please enter the due date of the task (in the following format: 01 Jan 2000): ")
        today_date = input("Please enter today's date (in the following format: 01 Jan 2000): ")

        #Add the data to the file task.txt with 'No' at the end to indicate that the task isn't yet completed
        with open('tasks.txt', 'a') as file:     #opens the file for writing, appending (a) the inserted data to the end
            file.write('\n' + username_assigned + ', ' + task_title + ', ' + task_description + ', ' + today_date + ', ' + task_duedate + ', ' + 'No')
        print()


    elif menu == 'va':
        pass   # read the task from task.txt file and print to the console in the format of Output 2 in the task PDF
        print()
        with open('tasks.txt', 'r') as file:    # r for read only
            for line in file.readlines():
                task_content = line.rstrip().split(', ')      # use rstrip to remove trailing whitespaces and newlines
                print("Task:".ljust(20) + task_content[1])    # use str.ljust() to left-align the content of each line at a fixed width of 20 characters, to make sure that the formatting is aligned correctly
                print("Assigned to:".ljust(20) + task_content[0])
                print("Date assigned:".ljust(20) + task_content[3])
                print("Due date:".ljust(20) + task_content[4])
                print("Task complete?".ljust(20) + task_content[5])
                print("Task description:")
                print("  {}".format(task_content[2]))
                print()


    elif menu == 'vm':
        pass
        print()
        with open('tasks.txt', 'r') as file:
            for line in file.readlines():                   #Read a line from the file
                task_content = line.rstrip().split(', ')    # Split the line where there is comma and space.
                if username == task_content[0]:             # Check if the username of the person logged in is the same as the username you have read from the file.
                    print("Task:".ljust(20) + task_content[1])
                    print("Assigned to:".ljust(20) + task_content[0])
                    print("Date assigned:".ljust(20) + task_content[3])
                    print("Due date:".ljust(20) + task_content[4])
                    print("Task complete?".ljust(20) + task_content[5])
                    print("Task description:")
                    print("  {}".format(task_content[2]))
                    print()


    elif menu == 'e':
        print()
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")