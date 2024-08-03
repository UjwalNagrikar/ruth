def check_voting_eligibility(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Example usage
age = int(input("Enter your age: "))
print(check_voting_eligibility(age))
