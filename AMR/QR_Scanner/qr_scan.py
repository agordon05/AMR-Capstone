import cv2

import numpy as np
from pylibdmtx.pylibdmtx import decode
from Robot_command import robot_camera_vision as camera
from Model import robot as bot

def decode_data(image):
    try:
        # Convert the image to NumPy array
        np_arr = np.frombuffer(image.value, np.uint8)
        # Debug prints
#         print(f"Image size: {len(image.value)}")
#         print(f"NumPy array size: {np_arr.size}")
        
        if len(image.value) == 0 or np_arr.size == 0:
#             print("image is empty")
            return []

        # Ensure the array is not empty
        if np_arr.size > 0:
            # Decode NumPy array to OpenCV image
            cv2_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            # Ensure the image is not None
            if cv2_image is not None:
                # Decode the image
                qr_obj = decode(cv2_image)
                return qr_obj
            else:
                print("Error decoding image: cv2_image is None")
                return []
        else:
            print("Error decoding image: np_arr is empty")
            return []
    except Exception as e:
        print(f"Error in decode_data: {e}")
        return []


def preprocess_image(img):
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)


def run():
    try:
        print("QR Scanner thread started")
        # Rest of the code
    except Exception as e:
        print(f"Exception in QR Scanner Thread: {e}")

    try:

        while True:
            image = camera.get_image()
            
            if image:
#                 pre_img = preprocess_image(image)
                qr_obj = decode_data(image)
                if qr_obj is None:
                    print("No qr object returned")
                if qr_obj:
                    if qr_obj[0] is None:
                        print("qr_obj[0] is none")
                    code = qr_obj[0].data.decode('utf-8')
                    print(code)
                    bot.set_qr_scan(code)

    except Exception as e:
        print(f"Exception in QR Scanner Thread: {e}")


