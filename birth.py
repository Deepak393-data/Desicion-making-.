'''
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38
'''
# Input
birth_year = int(input())  # Last 2 digits of the birth year
current_year = int(input())  # Last 2 digits of the current year

# Calculate the full years
# Assuming the years are in the 1900s for simplicity
if current_year < birth_year:
    current_year += 100  # Adjust if current year is less than birth year

# Calculate age
age = current_year - birth_year

# Output
print(age)
