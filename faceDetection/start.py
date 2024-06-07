import subprocess

def main():
    while True:
        print("Welcome ti the Face Recognition System")
        print("1. Start Video Monitoring")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            subprocess.run(["python", "face_recognize3.py"])

        elif choice == "2":
            print("Exiting the system")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
