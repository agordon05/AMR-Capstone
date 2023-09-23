import movement
import user_control


def controller(control: str):
    user_flag = user_control.get_user_flag()

    if user_flag is True:
        return

    if control == "forward" or control == "backward" or control == "rotating left" or control == "rotating right" or control == "stop":
        movement.set_signal(control)

    else:
        movement.set_signal(None)
