import cv2
import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def add_person():
    person_name = input("Enter the name of the person: ")
    directory =f"datasets/{person_name}"

    create_directory(directory)

    video_capture = cv2.VideoCapture(0)
    print("Press 'c' to capture an image or 'q' to quit.")

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture image")
            break

        cv2.imshow('Video', frame)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('c'):
            image_path = os.path.join(directory, f"{person_name}.png")
            cv2.imwrite(image_path, frame)
            print(f"Image saved to {image_path}")
            break
        elif key & 0xFF == 27: 
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    add_person()

    
