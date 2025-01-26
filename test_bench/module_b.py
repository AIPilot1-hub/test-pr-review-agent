def find_user_in_db(username):
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    print("Executing query:", query)
    return "Simulated DB results for user: " + username

def redundant_logic_2():
    print("Performing some operations.")
    x = 10
    y = 20
    z = x + y
    return z
