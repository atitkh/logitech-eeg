import sys
sys.path.append('../logidrivepy')
from logidrivepy import LogitechController
import time

def spin_controller(controller):
    for i in range(-100, 102, 2):
        controller.LogiPlaySpringForce(0, i, 100, 40)
        controller.logi_update()
        time.sleep(0.1)

def get_wheel():
    controller = LogitechController()
    if not controller.steering_initialize():
        print("Failed to initialize the controller.")
        return

    try:
        while True:
            controller.logi_update()
            state_pointer = controller.LogiGetStateENGINES(0)
            state = state_pointer.contents
            print(state)
            print(f"Steering: {state.lX}")
            print(f"Throttle: {state.lY}")
            print(f"Brake: {state.lRz}")
            print("\n")
            # ("lX", ctypes.c_int),
            # ("lY", ctypes.c_int),
            # ("lZ", ctypes.c_int),
            # ("lRx", ctypes.c_int),
            # ("lRy", ctypes.c_int),
            # ("lRz", ctypes.c_int),
            # ("rglSlider", ctypes.c_int * 2),
            # ("rgdwPOV", ctypes.c_uint * 4),
            # ("rgbButtons", ctypes.c_byte * 128),
            # ("lVX", ctypes.c_int),
            # ("lVY", ctypes.c_int),
            # ("lVZ", ctypes.c_int),
            # ("lVRx", ctypes.c_int),
            # ("lVRy", ctypes.c_int),
            # ("lVRz", ctypes.c_int),
            # ("rglVSlider", ctypes.c_int * 2),
            # ("lAX", ctypes.c_int),
            # ("lAY", ctypes.c_int),
            # ("lAZ", ctypes.c_int),
            # ("lARx", ctypes.c_int),
            # ("lARy", ctypes.c_int),
            # ("lARz", ctypes.c_int),
            # ("rglASlider", ctypes.c_int * 2),
            # ("lFX", ctypes.c_int),
            # ("lFY", ctypes.c_int),
            # ("lFZ", ctypes.c_int),
            # ("lFRx", ctypes.c_int),
            # ("lFRy", ctypes.c_int),
            # ("lFRz", ctypes.c_int),
            # ("rglFSlider", ctypes.c_int * 2)
            time.sleep(0.1)
    finally:
        controller.steering_shutdown()


def spin_test():
    controller = LogitechController()

    controller.steering_initialize()
    print("\n---Logitech Spin Test---")
    spin_controller(controller)
    print("Spin test passed.\n")

    controller.steering_shutdown()


if __name__ == "__main__":
    # spin_test()
    get_wheel()


# import sys
# sys.path.append('../logidrivepy')
# from logidrivepy import LogitechController
# import time

# controller = LogitechController()
# controller.steering_initialize()

# while True:
#     state_pointer = controller.LogiGetStateENGINES(0)
#     state = state_pointer.contents

#     # Retrieve force feedback values
#     force_x = state.lFX
#     force_y = state.lFY
#     force_z = state.lFZ

#     # Print or use the force feedback values
#     print(f"Force X: {force_x}")
#     print(f"Force Y: {force_y}")
#     print(f"Force Z: {force_z}")


# controller.steering_shutdown()