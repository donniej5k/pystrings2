# Task 1
def check_command(text):
    commands = ["help", "issue", "contact support"]
    for command in commands:
        if command in text:
            return command
    return None


def main():
    user_input = input("How can I help? You can say help, support or issue ")
    command = check_command(user_input)
    if command:
        if command == "help":
            response = input("Is it an issue or do you need to contact support? (issue/support): ")
            if response == "issue":
                handle_issue()
            elif response == "support":
                print("Support can be reached at sample-support@sample.com.")
            else:
                print(input,"i is invalid response.")
        elif command == "issue":
            handle_issue()
        elif command == "support":
            print("Support can be reached at sample-support@sample.com.")
    else:
        print(user_input, "not possible!")

#Task 2
def handle_issue():
    issue_type = input("Is it with login, performance, or error? ")
    if issue_type == "login":
        print("Please check your username and password.")
    elif issue_type == "performance":
        print("Try optimizing your system settings.")
    elif issue_type == "error":
        print("Please contact support at sample-support@sample.com!")
    else:
        print(issue_type,"is invalid.")
if __name__ == "__main__":
    main()
