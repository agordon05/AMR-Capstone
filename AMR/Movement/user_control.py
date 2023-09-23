import movement

__user_flag = False  # when this flag is true, the user is controlling the robot, any other signals to control are void


def get_user_flag():
    global __user_flag
    return __user_flag


def controller(control: str):
    global __user_flag

    if control == "forward" or control == "backward" or control == "rotating left" or control == "rotating right" or control == "stop":
        __user_flag = True
        movement.set_signal(control)

    else:
        __user_flag = False
        movement.set_signal(None)
