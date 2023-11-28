import base64

__id: int = 1
__message: str = "Starting up"

# Position
__x_pos: float = 1
__y_pos: float = 1
__rotation: float = 0

# Destination
__x_destination: float = 1
__y_destination: float = 1

# Relevant info
__qr_scan: str = ""
__log = ["Jetbot is starting up"]
__user_command: str = ""
__robot_command: str = ""
__image = None

# Direction the robot is facing
__direction = {
    'Up': False,
    'Down': False,
    'Left': False,
    'Right': True
}
# Update direction
def turn_left():
    if __direction['Up'] is True:
        __direction['Up'] = False
        __direction['Left'] = True
        
    elif __direction['Down'] is True:
        __direction['Down'] = False
        __direction['Right'] = True
        
    elif __direction['Left'] is True:
        __direction['Left'] = False
        __direction['Down'] = True
        
    else:
        __direction['Right'] = False
        __direction['Up'] = True
        
# Update direction
def turn_right():
    if __direction['Up'] is True:
        __direction['Up'] = False
        __direction['Right'] = True
        
    elif __direction['Down'] is True:
        __direction['Down'] = False
        __direction['Left'] = True
        
    elif __direction['Left'] is True:
        __direction['Left'] = False
        __direction['Up'] = True
        
    else:
        __direction['Right'] = False
        __direction['Down'] = True

def get_direction():
    if __direction['Up'] is True:
        return 'Up'
    elif __direction['Down'] is True:
        return 'Down'
    elif __direction['Left'] is True:
        return 'Left'
    else:
        return 'Right'

        
def get_id():
    return __id


def get_message():
    return __message


def get_x_pos() -> float:
    return __x_pos


def get_y_pos() -> float:
    return __y_pos


def get_rotation() -> float:
    return __rotation


def get_x_destination() -> float:
    return __x_destination


def get_y_destination() -> float:
    return __y_destination


def get_qr_scan():
    return __qr_scan


def get_log():
    return __log


def get_user_command():
    return __user_command


def get_robot_command():
    return __robot_command


def get_image():
    return __image


def set_message(message: str):
    global __message
    __message = message


def set_x_pos(x_pos: float):
    global __x_pos
    __x_pos = x_pos


def set_y_pos(y_pos: float):
    global __y_pos
    __y_pos = y_pos


def set_rotation(rotation: float):
    global __rotation
    __rotation = rotation


def set_x_destination(x_destination: float):
    global __x_destination
    __x_destination = x_destination


def set_y_destination(y_destination: float):
    global __y_destination
    __y_destination = y_destination


def set_qr_scan(qr_scan: str):
    global __qr_scan
    __qr_scan = qr_scan


def set_log(log: [str]):
    global __log
    __log = log


def set_user_command(command: str):
    global __user_command
    __user_command = command


def set_robot_command(command: str):
    global __robot_command
    __robot_command = command


def set_image(image):
    global __image
    __image = image


def add_to_log(log):
    global __log
    __log.append(log)


def to_json():
    #b64 image for sending
    global __image
    base64_image = base64.b64encode(__image).decode('utf-8') if __image is not None else None

    return {
        'id': __id,
        'status': "Active",
        'message': __message,
        'x_pos': __x_pos,
        'y_pos': __y_pos,
        'rotation': __rotation,
        'x_destination': __x_destination,
        'y_destination': __y_destination,
        'qrScan': __qr_scan,
        'loggerList': __log,
        # 'userSignal': None,
        'image': base64_image
    }

