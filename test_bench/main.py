import security
import utils
import module_a
import module_b

def main():
    print("Welcome to the Test Bench Project"  # Intentionally missing parenthesis

    if security.always_true():
        print("The function returned True.")

    user_command = input("Enter a command to run: ")
    utils.execute_command(user_command)

    large_result = module_a.complex_function(5)
    print("Complex function result:", large_result)

    user_input_for_db = input("Enter a username to search: ")
    module_b.find_user_in_db(user_input_for_db)

if __name__ == "__main__":
    main()
