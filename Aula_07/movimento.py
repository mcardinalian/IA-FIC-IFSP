import cv2
import numpy as np

WIN = "Frame-diff Tracker"
MIN_AREA = 600
BLUR_K = 7
THRESH = 25

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise RuntimeError("Cannot open webcam")

ok, prev = cap.read()
if not ok:
    raise RuntimeError("Cannot read first frame")
prev_gray = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)
prev_gray = cv2.GaussianBlur(prev_gray, (BLUR_K, BLUR_K), 0)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ok, frame = cap.read()
    if not ok:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (BLUR_K, BLUR_K), 0)

    diff = cv2.absdiff(gray, prev_gray)
    _, binm = cv2.threshold(diff, THRESH, 255, cv2.THRESH_BINARY)
    binm = cv2.morphologyEx(binm, cv2.MORPH_OPEN, kernel, iterations=1)
    binm = cv2.dilate(binm, kernel, iterations=2)

    cnts = cv2.findContours(binm, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]

    out = frame.copy()
    if cnts:
        c = max(cnts, key=cv2.contourArea)
        if cv2.contourArea(c) >= MIN_AREA:
            M = cv2.moments(c)
            if M["m00"] != 0:
                cx, cy = int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])
                cv2.circle(out, (cx, cy), 6, (0, 0, 255), -1)
                x, y, w, h = cv2.boundingRect(c)
                cv2.rectangle(out, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(out, f"({cx},{cy})", (cx+10, cy-10),
                            font, 0.6, (0, 255, 0), 2, cv2.LINE_AA)

    h, w = out.shape[:2]
    mask_vis = cv2.cvtColor(cv2.resize(binm, (w//3, h//3), interpolation=cv2.INTER_NEAREST),
                            cv2.COLOR_GRAY2BGR)
    out[10:10+mask_vis.shape[0], 10:10+mask_vis.shape[1]] = mask_vis
    cv2.putText(out, "mask", (12, 12 + mask_vis.shape[0] + 20),
                font, 0.6, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow(WIN, out)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    prev_gray = gray

cap.release()
cv2.destroyAllWindows()
