import face_recognition
import cv2, sys
import numpy as np
import math
# import os

# Load the reference image and get face encodings
reference_image = face_recognition.load_image_file("datasets/gabriel/5.png")
reference_face_encoding = face_recognition.face_encodings(reference_image)[0]

face_locations = []
face_encodings = []
face_names = []
process_this_frame = 10
frame_count = 0

video_capture = cv2.VideoCapture(0)


while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]  # Convert from BGR to RGB

    if frame_count % process_this_frame == 0:
        # Find all face locations and encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # Check if the face matches the reference face
            matches = face_recognition.compare_faces([reference_face_encoding], face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance([reference_face_encoding], face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = "Gabriel"

            face_names.append(name)

    # process_this_frame = not process_this_frame

    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == 27: 
        break

video_capture.release()
cv2.destroyAllWindows()

