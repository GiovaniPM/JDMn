import re
from datetime import datetime

# Define the string
s = "The event will be on 01/12/2023 at 2:00 PM."

# Define the date format
date_format = "%d/%m/%Y"

# Use a regular expression to find the date in the string
match = re.search(r'\b(\d{2}/\d{2}/\d{4})\b', s)

if match:
    # Extract the date string
    date_string = match.group(1)

    # Convert the date string to a datetime object
    dt = datetime.strptime(date_string, date_format)

    # Print the datetime object
    print(dt)
else:
    print("No date found in the string.")
