import cv2
import mediapipe as mp 

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

#Code to blend the transparent part to frame
def overlay_transparent(frame, overlay, x, y):
    #So if my pictures bugs out again, just return the frame
    if overlay is None:
        return frame

    h, w = overlay.shape[:2]

    #Overlay image color
    bgr = overlay[:, :, :3]
    #Overlay alpha is divided by 255 to get the range of 0 to 1
    alpha = overlay[:, :, 3] / 255.0

    #Blending code I found in reddit
    for c in range(3):
        frame[y:y+h, x:x+w, c] = (
            alpha * bgr[:, :, c] +
            (1 - alpha) * frame[y:y+h, x:x+w, c]
        )

    return frame


#Set up my webcam
cap = cv2.VideoCapture(0)

#Creates the hand tracker
with mp_hands.Hands(
    #It is a video, so false
    static_image_mode=False,
    #I will just use one hand for now
    max_num_hands=1,
    min_detection_confidence=0.9,
    min_tracking_confidence=0.9
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

                lm = hand_lms.landmark
                #Wrist
                wrist = lm[0]
                #Tips 
                thumb_tip  = lm[4]
                index_tip  = lm[8]
                middle_tip = lm[12]
                ring_tip   = lm[16]
                pinky_tip  = lm[20]
                #PIP Joints
                thumb_pip  = lm[2]
                index_pip  = lm[6]
                middle_pip = lm[10]
                ring_pip   = lm[14]
                pinky_pip  = lm[18]
                #Finger up Logic
                thumb_up  = thumb_tip.x < thumb_pip.x 
                index_up = index_tip.y < index_pip.y
                middle_up = middle_tip.y < middle_pip.y
                ring_up   = ring_tip.y < ring_pip.y
                pinky_up  = pinky_tip.y < pinky_pip.y

                #Gesture Logic

                palm = thumb_up and index_up and middle_up and ring_up and pinky_up
                fist = not thumb_up and not index_up and not middle_up and not ring_up and not pinky_up
                peace = not thumb_up and index_up and middle_up and not ring_up and not pinky_up
                naughty = not thumb_up and not index_up and middle_up and not ring_up and not pinky_up
                thumbs_up = thumb_up and not index_up and not middle_up and not ring_up and not pinky_up

                fist_image      = cv2.imread("assets/fist.png", cv2.IMREAD_UNCHANGED)
                peace_image     = cv2.imread("assets/peace-sign.png", cv2.IMREAD_UNCHANGED)
                naughty_image   = cv2.imread("assets/middle-finger.png", cv2.IMREAD_UNCHANGED)
                thumbs_up_image = cv2.imread("assets/thumbs_up.png", cv2.IMREAD_UNCHANGED)
                palm_image      = cv2.imread("assets/palm.png", cv2.IMREAD_UNCHANGED)

                fist_image = cv2.resize(fist_image, (200, 200))
                peace_image = cv2.resize(peace_image, (200, 200))
                naughty_image = cv2.resize(naughty_image, (100, 100))
                thumbs_up_image = cv2.resize(thumbs_up_image, (100, 100))
                palm_image = cv2.resize(palm_image, (100, 100))

                #Using Formatted string to make it easier for me
                cv2.putText(frame, f"Thumb up: {thumb_up}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(frame, f"Pinky up: {pinky_up}", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(frame, f"Index up: {index_up}", (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(frame, f"Middle up: {middle_up}", (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                cv2.putText(frame, f"Ring up: {ring_up}", (50, 250), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            


                mp_draw.draw_landmarks(frame, hand_lms, mp_hands.HAND_CONNECTIONS)

                if palm == True:
                    cv2.putText(frame, "Palm", (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    frame = overlay_transparent(frame, palm_image, 500, 200)

                if fist == True:
                    cv2.putText(frame, "Fist", (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                    fh, fw = frame.shape[:2]
                    emoji_size = 100

                    wrist_x = int(wrist.x * fw)
                    wrist_y = int((wrist.y * fh) - 100)

                    x = max(0, min(wrist_x - emoji_size//2, fw - emoji_size))
                    y = max(0, min(wrist_y - emoji_size//2, fh - emoji_size))

                    frame = overlay_transparent(frame, fist_image, x, y)

                if peace == True:
                    cv2.putText(frame, "Peace", (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    frame = overlay_transparent(frame, peace_image, 500, 200)

                if naughty == True:
                    cv2.putText(frame, "Naughty", (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    frame = overlay_transparent(frame, naughty_image, 500, 200)

                if thumbs_up == True:
                    cv2.putText(frame, "Thumbs Up", (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                    frame = overlay_transparent(frame, thumbs_up_image, 500, 200)

                #Displaying emojis for each gesture
                image = cv2.imread("")
                for i, lm in enumerate(hand_lms.landmark):

                    #Put a number next to each landmark, converted the number to a string since it is needed by frame
                    #Multiply the x and y by the width and height of the frame to get the correct position
                    cv2.putText(frame, str(i), (int(lm.x * frame.shape[1]), int(lm.y * frame.shape[0])), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
                    


        #Show the frame in the box called Camera Feed
        cv2.imshow("Camera Feed", frame)

        #Makes it end with pressing q key 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
