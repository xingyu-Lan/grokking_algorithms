# # Define the two strings
dp_table_blue = ["b", "l", "u", "e"]
dp_table_clues = ["c", "l", "u", "e", "s"]

# Create a 2D table to store the results of the dynamic programming algorithm
dp_table = [[0 for i in range(len(dp_table_blue))] for j in range(len(dp_table_clues))] # (5,4)

# Loop through the table and fill it in according to the dynamic programming algorithm
for i in range(len(dp_table_blue)):
    for j in range(len(dp_table_clues)):
        # The letters match.
        # Step 2: If they do match. This value is value of top-left neighbor + 1
        if dp_table_clues[j] == dp_table_blue[i]:
            dp_table[j][i] = dp_table[j-1][i-1] + 1
        # The letters don't match
        # Step 1: If the letters don't match. The value is zero
        else:
            dp_table[j][i] = 0

# Print the final table
print(dp_table)
