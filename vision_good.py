#우리는 깃을 사용합니다
import cv2
cap = cv2.VideoCapture("lion.mp4")

edge_bool = False
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(image=gray_img, threshold1=100, threshold2=200)

    if edge_bool:
        image = edges
    else:
        image = frame

    cv2.imshow("Video", image)
    key = cv2.waitKey(1)
    if key == ord("q"):break
    elif key ==ord("b"):
        edge_bool = not edge_bool
    
 
cap.release()
cv2.destroyAllWindows()