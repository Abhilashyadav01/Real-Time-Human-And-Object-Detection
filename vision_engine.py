import cv2
import time
from ultralytics import YOLO

# Load the model
model = YOLO('yolov8n.pt')

def run_ai():
    cap = cv2.VideoCapture(0)
    phone_timer = None
    
    # Fullscreen Window Setup
    window_name = 'VisionPro AI - Detection Mode'
    cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = cap.read()
        if not ret: break

        results = model(frame, stream=True, verbose=False)
        phone_in_frame = False

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label_name = model.names[cls]
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                
                # --- LOGIC FOR HUMANS ---
                if label_name == "person":
                    color = (0, 255, 0) # Green for humans
                    display_text = "HUMAN DETECTED"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                    cv2.putText(frame, display_text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

                # --- LOGIC FOR MOBILE PHONES ---
                elif label_name == "cell phone":
                    phone_in_frame = True
                    color = (255, 0, 0) # Default Blue
                    display_text = "OBJECT: MOBILE"

                    # Check if held longer than 5 seconds
                    if phone_timer and (time.time() - phone_timer > 3):
                        color = (0, 0, 255) # Warning Red
                        display_text = "!!! ALERT: DROP PHONE !!!"
                        # Screen Border Flash
                        cv2.rectangle(frame, (0,0), (frame.shape[1], frame.shape[0]), (0,0,255), 25)

                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 4)
                    cv2.putText(frame, display_text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 3)

                # --- LOGIC FOR OTHER OBJECTS ---
                else:
                    color = (200, 200, 200) # Gray for generic objects
                    display_text = f"OBJECT: {label_name.upper()}"
                    cv2.rectangle(frame, (x1, y1), (x2, y2), color, 1)
                    cv2.putText(frame, display_text, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

        # Timer Logic for Phone
        if phone_in_frame:
            if phone_timer is None:
                phone_timer = time.time()
        else:
            phone_timer = None

        # Display Help Text on screen
        cv2.putText(frame, "Press 'Q' to Exit Fullscreen", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        cv2.imshow(window_name, frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    run_ai()