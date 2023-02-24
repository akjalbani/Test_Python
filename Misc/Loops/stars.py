# Define the maximum number of stars in a row
max_stars = 5

# Loop through each row
for i in range(1, max_stars * 2):
# Calculate the number of stars to print based on the row number
    if i <= max_stars:
        num_stars = i
    else:
        num_stars = max_stars * 2 - i

    # Print the stars for the row
    for j in range(num_stars):
        print("*", end=" ")

    # Move to the next line
    print()
