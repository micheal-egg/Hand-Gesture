import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

#Set up my webcam
cap = cv2.VideoCapture(0)

#Creates the hand tracker
with mp_hands.Hands(
    #It is a video, so false
    static_image_mode=False,
    #I will just use one hand for now
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
) as hands:
    #Continues to take from my webcam with a loop
    while True:
        #For reading my frame
        ret, frame = cap.read()
        #If it fails, break the loop
        if not ret:
            break

        #For flipping camera, because I look better. 0 is for Vert Flip
        frame = cv2.flip(frame, 1)  # mirror like FaceTime
        #Convert the BGR image to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        #Process the RGB image to find hands
        result = hands.process(rgb)

        #If the hand is found, show the landmark things
        if result.multi_hand_landmarks:
            #For each detected hand(I used One) draw the dots and lines 
            for hand_lms in result.multi_hand_landmarks:
                index_tip = hand_lms.landmark[8]
                #print("Index tip:", round(index_tip.x, 3), round(index_tip.y, 3))
                mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)
                #With enumerate, it gets the pair of the index and the landmark.
                for i, lm in enumerate(hand_lms.landmark):
                    #Put a number next to each landmark, converted the number to a string since it is needed by frame
                    cv2.putText(frame, str(i),
                    #Multiply the x and y by the width and height of the frame to get the correct position
                    (int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)


        #Show the frame in the box called Camera Feed
        cv2.imshow("Camera Feed", frame)

        #Makes it end with pressing q key 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
