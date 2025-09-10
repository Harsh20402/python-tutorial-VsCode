# Define a function named https_status that takes one argument 'status'
def https_status(status):

    # The 'match' statement (introduced in Python 3.10) is similar to switch-case in other languages.
    # It compares 'status' against multiple possible values.
    match status:

        # If status is 200, return "OK."
        case 200:
            return "OK."

        # If status is 404, return "Not Found."
        case 404:
            return "Not Found."

        # If status is 500, return "Internal Server Error."
        case 500:
            return "Internal Server Error."

        # If status doesn't match any of the above, execute the default case.
        case _:
            return "Unknown Status."


# Function calls and their outputs:

print(https_status(200))   # Matches case 200 → Output: "OK."
print(https_status(404))   # Matches case 404 → Output: "Not Found."
print(https_status(500))   # Matches case 500 → Output: "Internal Server Error."
print(https_status(00))    # '00' is treated as integer 0 → No case match → Output: "Unknown Status."
print(https_status("100")) # "100" is a string, not an integer → No case match → Output: "Unknown Status."
