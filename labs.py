'''
 There are 3 labs in the CSE department. The labs are L1, L2, and L3 with a seating capacity of x, y, and z respectively. A single lab needs to be allocated to a class of 'n' students. The labs need to be utilized to the maximum i.e the number of systems used should not be minimal. Which lab needs to be allocated to this class?
Input format:
Input consists of 4 integers
The first input denotes 'x'
The second input denotes 'y'
The third input denotes 'z'
The fourth input denotes 'n'
Output format:
Print the lab which is suitable for  'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
L1
'''
# Input
capacity_L1 = int(input())  # Seating capacity of L1
capacity_L2 = int(input())  # Seating capacity of L2
capacity_L3 = int(input())  # Seating capacity of L3
num_students = int(input())  # Number of students

# Initialize variables to track the suitable lab
suitable_lab = None
max_capacity = -1

# Check each lab for suitability
if capacity_L1 >= num_students and capacity_L1 > max_capacity:
    suitable_lab = "L1"
    max_capacity = capacity_L1
if capacity_L2 >= num_students and capacity_L2 > max_capacity:
    suitable_lab = "L2"
    max_capacity = capacity_L2
if capacity_L3 >= num_students and capacity_L3 > max_capacity:
    suitable_lab = "L3"
    max_capacity = capacity_L3

# Output the suitable lab
print(suitable_lab)
