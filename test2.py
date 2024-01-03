import time
from scratch2py import Scratch2Py
# Open the text document for writing
with open('output.txt', 'a') as file:
    # Open the text document
    with open('test2.txt', 'r') as input_file:
        # Iterate through each line in the document
        for line in input_file:
            # Remove leading and trailing whitespace from the line
            line = line.strip()

            s2py = Scratch2Py('funny_gifs_guy', 'cody0414')
            # Replace 'replace with user' with the current line from the document
            user = s2py.user(line)

            if not user.exists():
                # Write the user to the output file
                print(user.user, user.exists())
                file.write(user.user)
            time.sleep(0.2)
