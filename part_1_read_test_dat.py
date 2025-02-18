import cc_dat_utils

# Define the input .dat file (update path if needed)
dat_file = "data/pfgd_test.dat"

# Load the level pack
level_pack = cc_dat_utils.make_cc_level_pack_from_dat(dat_file)

# Print unique tile IDs from the first level
if level_pack and level_pack.levels:
    first_level = level_pack.levels[0]
    unique_tile_ids = set(first_level.upper_layer)
    print("Unique Tile IDs in pfgd_test.dat:", sorted(unique_tile_ids))
else:
    print("No levels found in pfgd_test.dat.")

