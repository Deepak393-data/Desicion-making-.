'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1
'''
# Input
capacity_L1 = int(input())  # Seating capacity of L1
capacity_L2 = int(input())  # Seating capacity of L2
capacity_L3 = int(input())  # Seating capacity of L3
allocated_lab = input().strip()  # Lab allocated for ACE training

# Create a dictionary to store capacities
capacities = {
    "L1": capacity_L1,
    "L2": capacity_L2,
    "L3": capacity_L3
}

# Remove the allocated lab from the options
if allocated_lab in capacities:
    del capacities[allocated_lab]

# Find the lab with minimal seating capacity
min_lab = min(capacities, key=capacities.get)

# Output
print(min_lab)