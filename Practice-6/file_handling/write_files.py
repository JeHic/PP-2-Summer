# Append new lines and verify content

with open("sample_data.txt", "r") as file:
    data = file.read()

# Append new lines to the file
with open("sample_data.txt", "a") as file:
    file.write("\nThe White Stage led a group of men into the horizon.")
    file.write("\nIt returned next day. But no one knows what happened to those men.")

# Verify the content
with open("sample_data.txt", "r") as file:
    content = file.read()
    print(content)
