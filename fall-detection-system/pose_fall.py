# Uses MediaPipe Pose to look for sudden drop in hip y-coordinate (MVP heuristic)
import cv2, time, collections
import mediapipe as mp
mp_pose = mp.solutions.pose
cap = cv2.VideoCapture(0)
window = collections.deque(maxlen=10)
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while True:
        ret, frame = cap.read()
        if not ret: break
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = pose.process(img)
        if res.pose_landmarks:
            # use landmark 24 (right hip) y-coordinate as proxy
            hip = res.pose_landmarks.landmark[24].y
            window.append(hip)
            if len(window)==10:
                if max(window)-min(window) > 0.2:
                    print('ALERT: possible fall (hip y change)', max(window)-min(window))
        cv2.imshow('pose', frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
cap.release(); cv2.destroyAllWindows()