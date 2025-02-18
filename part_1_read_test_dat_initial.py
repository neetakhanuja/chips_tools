import cc_dat_utils  # Import the cc_dat_utils module

# Define the input .dat file
dat_file = "data/pfgd_test.dat"

# Use the function to load the level pack
level_pack = cc_dat_utils.make_cc_level_pack_from_dat(dat_file)

# Print the string representation of the level pack
print(level_pack)

# Save the output to a text file
output_file = "data/pfgd_test.txt"
with open(output_file, "w") as f:
    f.write(str(level_pack))

print(f"Output saved to {output_file}")
