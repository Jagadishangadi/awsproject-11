from src.auth import authenticate
from src.file_manager import upload_file

def main():
    print("Secure File System")
    user = input("Username: ")
    pwd = input("Password: ")

    if not authenticate(user, pwd):
        print("Invalid login")
        return

    print("Login successful")
    print("1. Upload file")
    choice = input("Enter choice: ")

    if choice == "1":
        path = input("Enter file path: ")
        if upload_file(path):
            print("File uploaded")
        else:
            print("Upload failed")

if __name__ == "__main__":
    main()