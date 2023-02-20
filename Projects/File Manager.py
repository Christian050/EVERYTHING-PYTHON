import os

class FileManager:
    def __init__(self):
        self.location = os.getcwd()

    def list_files(self):
        files = os.listdir(self.location)
        for index, file in enumerate(files):
            print(f'{index+1}. {file}')

    def change_directory(self):
        path = input('Enter the path of the directory: ')
        if os.path.isdir(path):
            self.location = path
            print(f'Changed directory to {path}')
        else:
            print(f'{path} is not a valid directory')

    def copy_file(self):
        source = input('Enter the path of the file to copy: ')
        destination = input('Enter the path of the destination: ')
        if os.path.isfile(source):
            os.system(f'cp {source} {destination}')
            print(f'Successfully copied {source} to {destination}')
        else:
            print(f'{source} is not a valid file')

    def move_file(self):
        source = input('Enter the path of the file to move: ')
        destination = input('Enter the path of the destination: ')
        if os.path.isfile(source):
            os.system(f'mv {source} {destination}')
            print(f'Successfully moved {source} to {destination}')
        else:
            print(f'{source} is not a valid file')

    def delete_file(self):
        file = input('Enter the path of the file to delete: ')
        if os.path.isfile(file):
            os.remove(file)
            print(f'Successfully deleted {file}')
        else:
            print(f'{file} is not a valid file')

    def run(self):
        while True:
            print(f'Current directory: {self.location}')
            print('What do you want to do?')
            print('1. List files')
            print('2. Change directory')
            print('3. Copy file')
            print('4. Move file')
            print('5. Delete file')
            print('6. Exit')
            choice = input('Enter your choice: ')
            if choice == '1':
                self.list_files()
            elif choice == '2':
                self.change_directory()
            elif choice == '3':
                self.copy_file()
            elif choice == '4':
                self.move_file()
            elif choice == '5':
                self.delete_file()
            elif choice == '6':
                break
            else:
                print('Invalid choice. Please try again.')

file_manager = FileManager()
file_manager.run()
