
__id: int = 1
__message: str = "Starting up"

__x_pos: float = 0
__y_pos: float = 0
__rotation: float = 0

__x_destination: float = 0
__y_destination: float = 0

__qr_scan: str = ""
__log = ["Jetbot is starting up"]
__user_command: str = ""
__robot_command: str = ""
__image = None


def get_id():
    return __id


def get_message():
    return __message


def get_x_pos():
    return __x_pos


def get_y_pos():
    return __y_pos


def get_rotation():
    return __rotation


def get_x_destination():
    return __x_destination


def get_y_destination():
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
    __log = __log + log
