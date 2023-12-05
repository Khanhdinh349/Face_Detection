import cv2
import mediapipe as mp
import time

def hide_mesh_and_save_coordinates(img, faceLms, count_points):
    with open("point.txt", "a") as file: 
        for id, lm in enumerate(faceLms.landmark):
            ih, iw, ic = img.shape
            x, y = int(lm.x * iw), int(lm.y * ih)
            file.write(f"{id} {x} {y}\n")  
            count_points += 1 

    mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION, drawSpec, drawSpec)
    return count_points

cap = cv2.VideoCapture(0)  
pTime = 0
count_points = 0  
time_to_close = False  

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)
    
    if results.multi_face_landmarks and not time_to_close:
        for faceLms in results.multi_face_landmarks:
            count_points = hide_mesh_and_save_coordinates(img, faceLms, count_points)
            if count_points >= 468:  
                start_time = time.time()  
                time_to_close = True 
    
    if time_to_close:
        current_time = time.time() - start_time
        if current_time >= 5: 
            break
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (0, 255, 0), 0)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
