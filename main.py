import cv2
import mediapipe as mp
import pydirectinput

# Setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

accel = False
brake = False

def press_accel():
    global accel
    if not accel:
        pydirectinput.keyDown("right")   # Accelerate
        accel = True
        print(">>> Accelerate Pressed")

def release_accel():
    global accel
    if accel:
        pydirectinput.keyUp("right")
        accel = False
        print(">>> Accelerate Released")

def press_brake():
    global brake
    if not brake:
        pydirectinput.keyDown("left")   # Brake
        brake = True
        print(">>> Brake Pressed")

def release_brake():
    global brake
    if brake:
        pydirectinput.keyUp("left")
        brake = False
        print(">>> Brake Released")

cap = cv2.VideoCapture(0)
tips = [4,8,12,16,20]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(rgb)
    fc = 0
    gesture = "No Hand"

    if res.multi_hand_landmarks:
        lm = [(int(l.x * frame.shape[1]), int(l.y * frame.shape[0])) for l in res.multi_hand_landmarks[0].landmark]
        mp_draw.draw_landmarks(frame, res.multi_hand_landmarks[0], mp_hands.HAND_CONNECTIONS)

        # Count fingers
        if lm[tips[0]][0] < lm[tips[0]-1][0]:
            fc += 1
        for t in tips[1:]:
            if lm[t][1] < lm[t-2][1]:
                fc += 1

        if fc == 5:
            press_accel(); release_brake()
            gesture = "Accelerate (5 fingers)"
        elif fc == 0:
            press_brake(); release_accel()
            gesture = "Brake (0 fingers)"
        else:
            release_accel(); release_brake()
            gesture = f"No Control ({fc} fingers)"
    else:
        release_accel(); release_brake()

    cv2.putText(frame, gesture, (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
