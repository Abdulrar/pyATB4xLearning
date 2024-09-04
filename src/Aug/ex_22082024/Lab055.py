
user_type = input("Enter the user type Admin, Manager, Lead, Guest user\n")
match user_type:
    case "Admin" | "Manager":
        print("Hello sir Good morning..!!")
    case "Lead":
        print("Hello team lead")
    case "Guest":
        print("Hello Guest user welcome to the office")
