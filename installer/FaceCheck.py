import cv2
import mediapipe as mp
import numpy as np

def read_coordinates_from_file(file_path):
    points = []
    with open(file_path, "r") as file:
        for line in file:
            data = line.split()
            points.append((int(data[1]), int(data[2])))
    return points

def count_face_landmarks(image):
    mp_drawing = mp.solutions.drawing_utils
    mp_face_mesh = mp.solutions.face_mesh

    with mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=2, min_detection_confidence=0.5) as face_mesh:
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(image_rgb)

        if results.multi_face_landmarks:
            face_landmarks_count = len(results.multi_face_landmarks[0].landmark)
            return face_landmarks_count
        else:
            return 0

# Đọc tọa độ từ tệp point.txt
file_path = "point.txt"
saved_points = read_coordinates_from_file(file_path)

cap = cv2.VideoCapture(0)
time_counter = 0

while True:
    success, image = cap.read()
    if not success:
        break

    face_landmarks_count = count_face_landmarks(image)
    if face_landmarks_count > 20 and len(saved_points) > 80:
        print("Yes")
    else:
        print("No")

    cv2.imshow('Face Landmarks Count', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    time_counter += 1
    if time_counter == 75:
        break

cap.release()
cv2.destroyAllWindows()
