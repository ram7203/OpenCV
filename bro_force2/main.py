import cv2
from cvzone.HandTrackingModule import HandDetector
import time
import pyautogui

detector = HandDetector(detectionCon=0.8, maxHands=1)

time.sleep(2.0)

video = cv2.VideoCapture(0)

prev_key = "nothing"

while True:
    #setting up and sizing frame
    ret, frame = video.read()
    video.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
    video.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)

    hands, img = detector.findHands(frame)
    cv2.rectangle(img, (0, 480), (300, 425), (50, 50, 255), -2)
    cv2.rectangle(img, (640, 480), (400, 425), (50, 50, 255), -2)

    if hands:   #if hand is detected in frame
        lmList = hands[0]
        fingerUp = detector.fingersUp(lmList)
        direction = lmList['type']

        #detecting right palm (move right)
        if (fingerUp == [1, 1, 1, 1, 1] and direction=="Right"):
            cv2.putText(frame, 'Action', (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, 'Right', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)

            #releasing previous key if any
            if (prev_key == "left"):
                pyautogui.keyUp('left')
                prev_key = "right"

            if (prev_key == "e"):
                pyautogui.keyUp('e')
                prev_key = "right"

            if (prev_key == "up"):
                pyautogui.keyUp('up')
                prev_key = "right"

            pyautogui.keyDown('right')
            prev_key = "right"

        #detecting left palm (move left)
        if (fingerUp == [1, 1, 1, 1, 1] and direction=="Left"):
            cv2.putText(frame, 'Action', (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, 'Left', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)

            #releasing previous key if any
            if (prev_key == "right"):
                pyautogui.keyUp('right')
                prev_key = "left"

            if (prev_key == "e"):
                pyautogui.keyUp('e')
                prev_key = "left"

            if (prev_key == "up"):
                pyautogui.keyUp('up')
                prev_key = "left"

            pyautogui.keyDown('left')
            prev_key = "left"

        #detecting index finger (jump)
        if (fingerUp == [0, 1, 0, 0, 0]):
            cv2.putText(frame, 'Action', (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, 'Jump', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)

            #releasing previous key if any
            if (prev_key == "right"):
                pyautogui.keyUp('right')
                prev_key = "up"
            if (prev_key == "left"):
                pyautogui.keyUp('left')
                prev_key = "up"
            if (prev_key == "e"):
                pyautogui.keyUp('e')
                prev_key = "up"

            pyautogui.keyDown('up')
            prev_key = "up"

        #detecting right fist (jump right)
        if (fingerUp == [0, 0, 0, 0, 0] and direction=="Right"):
            cv2.putText(frame, 'Action', (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, 'Jump Right', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            pyautogui.keyDown('right')
            pyautogui.keyDown('up')
            pyautogui.keyUp('up')
            pyautogui.keyUp('right')

        #detecting left fist (jump left)
        if (fingerUp == [0, 0, 0, 0, 0] and direction=="Left"):
            cv2.putText(frame, 'Action', (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, 'Jump Left', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            pyautogui.keyDown('left')
            pyautogui.keyDown('up')
            pyautogui.keyUp('up')
            pyautogui.keyUp('left')


        #detecting gun symbol (fire)
        if (fingerUp == [1, 1, 1, 0, 0]):
            cv2.putText(frame, 'Action', (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, 'Fire', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)

            #checking which hand is raised to shoot in particular direction
            if direction=="Right":
                pyautogui.keyDown('right')
                pyautogui.keyUp('right')
            else:
                pyautogui.keyDown('left')
                pyautogui.keyUp('left')

            #releasing previous key if any
            if (prev_key == "right"):
                pyautogui.keyUp('right')
                prev_key = "e"

            if (prev_key == "left"):
                pyautogui.keyUp('left')
                prev_key = "e"

            if (prev_key == "up"):
                pyautogui.keyUp('up')
                prev_key = "e"

            pyautogui.keyDown('e')
            prev_key = "e"

        #do nothing/release keys for fingers with no action assigned
        if (sum(fingerUp)==2 or sum(fingerUp)==4):
            cv2.putText(frame, 'Action', (20, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)
            cv2.putText(frame, 'Nothing', (420, 460),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1,
                        cv2.LINE_AA)

            #releasing previous key if any
            if (prev_key == "left"):
                pyautogui.keyUp('left')
                prev_key = "nothing"

            if (prev_key == "right"):
                pyautogui.keyUp('right')
                prev_key = "nothing"

            if (prev_key == "e"):
                pyautogui.keyUp('e')
                prev_key = "nothing"

            if (prev_key == "up"):
                pyautogui.keyUp('up')
                prev_key = "nothing"

    #if hand is not detected release previous key if any
    else:
        if (prev_key == "left"):
            pyautogui.keyUp('left')
            prev_key = "nothing"

        if (prev_key == "right"):
            pyautogui.keyUp('right')
            prev_key = "nothing"

        if (prev_key == "e"):
            pyautogui.keyUp('e')
            prev_key = "nothing"

        if (prev_key == "up"):
            pyautogui.keyUp('up')
            prev_key = "nothing"

    #q to quit
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

#closing window
video.release()
cv2.destroyAllWindows()