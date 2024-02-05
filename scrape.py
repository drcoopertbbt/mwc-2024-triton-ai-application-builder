import os
import subprocess

# Run the tree command and capture its output
tree_output = subprocess.run(['tree', '-L', '2', '.'], capture_output=True, text=True).stdout

# Open the output file
with open('output.txt', 'w') as outfile:
  # Write the output of the tree command to the file
  outfile.write(tree_output)
  outfile.write("\n")

  # Walk through the current directory and its subdirectories
  for dirpath, dirnames, filenames in os.walk('.'):
    # Skip .git directory
    if '.git' in dirnames:
      dirnames.remove('.git')
    # For each file in the current directory
    for filename in filenames:
      # Construct the full file path
      filepath = os.path.join(dirpath, filename)
      # Try to open the file and write its contents to the output file
      try:
        with open(filepath, 'r') as infile:
          outfile.write(infile.read())
          outfile.write("\n")
      # If a UnicodeDecodeError occurs, skip the file
      except UnicodeDecodeError:
        print(f"Skipped file due to encoding error: {filepath}")