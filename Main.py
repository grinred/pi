import time
from pynput import keyboard
from adafruit_servokit import ServoKit


def map_value(throttle, in_min=0, in_max=100, out_min=750, out_max=2250):
    result = (throttle - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    return int((result - out_min) * (180 - 0) / (out_max - out_min) + 0)


if __name__ == '__main__':
    throttle_val = 0

    print("ESC calibration")
    for x in range(0, 3).__reversed__():
        if x != 0:
            print(f'Wait {x} sec to launch.')
            time.sleep(1)
        else:
            print("Start ESC calibration.")

    kit = ServoKit(channels=8)
    kit.servo[4].angle = map_value(100)
    print("100%")
    time.sleep(2)
    kit.servo[4].angle = map_value(0)
    print("Throttle 0%")
    print("End ESC calibration")


    def on_press(key):
        global throttle_val
        try:
            if key == keyboard.Key.up:
                if throttle_val < 100:
                    throttle_val = min(throttle_val + 5, 100)
                    kit.servo[4].angle = map_value(throttle_val)
                    print(f"Throttle: {throttle_val}%")

            elif key == keyboard.Key.down:
                if throttle_val > 0:
                    throttle_val = max(throttle_val - 5, 0)
                    kit.servo[4].angle = map_value(throttle_val)
                    print(f"Throttle: {throttle_val}%")

            elif key == keyboard.Key.esc:
                print("Stop")
                return False
        except:
            pass


    print(" Throttle ↑ and ↓. For exit press ESC.")
    print(f"Throttle: {throttle_val}%")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
