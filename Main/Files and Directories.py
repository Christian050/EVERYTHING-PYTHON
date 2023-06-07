from pathlib import Path

# Absolute path (from  hard disk 'c:\')
# Relative path(from within current directory 'Python')
# Variable necessary

# Set path.
path = Path('Ecommerce')


# Check if current path exists.
print(path.exists())


# Creating directory
new_path = Path('Emails')
print(new_path.mkdir())     # Returns None but path is created.


# Deleting Directory
print(new_path.rmdir())     # Returns None as well.


# Search for files and folders in current path.
search_path = Path('Exercises\Exercise 11')

# '*' prints all files and folders in current path. Extensions can be added.
for files in search_path.glob('*.py'):
    print(files)


# Nothing is returned if file or folder isn't found in directory.
search_path = Path('Exercise')

for files in search_path.glob('*'):
    print(files)
