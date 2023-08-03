import cv2
from pyzbar.pyzbar import decode

def qr_scanner():
    cap = cv2.VideoCapture(0)
    
    while True:
        _, frame = cap.read()
        
        # Detect and decode QR codes in the frame
        qr_codes = decode(frame)
        
        for qr_code in qr_codes:
            qr_data = qr_code.data.decode('utf-8')
            print(f"QR Code Data: {qr_data}")
            
            # Draw a rectangle around the detected QR code
            rect_points = qr_code.polygon
            for i in range(4):
                cv2.line(frame, rect_points[i], rect_points[(i + 1) % 4], (0, 255, 0), 3)
        
        cv2.imshow("QR Scanner", frame)
        
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit the loop
            break
            
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    qr_scanner()
