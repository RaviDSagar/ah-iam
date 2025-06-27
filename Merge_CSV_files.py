#Following codes is generated to merge all CSV Files into single CSV file as output

import os
import glob

with open('output.txt', 'w') as output_file:
    for csv_file in glob.glob('*.csv'):
        with open(csv_file, 'r') as f:
            next(f)  # Skip first line (header)
            for line in f:
                output_file.write(f"{csv_file},{line.rstrip()}\n")
        
        # Show progress - filename completed
        print(f"Completed: {csv_file}")

print("All files processed!")