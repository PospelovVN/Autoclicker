import mouse
import keyboard as keyb
import time
def main():
    def control():
        nonlocal IsWork
        if IsWork:
            IsWork = False
            print("finish")
        else:
            IsWork = True
    try:
        respawn = int(input('Enter resp (1 - bottom / 2 - top)'))
    except:
        print('You entered a wrong integer')
        raise SystemExit(0)
    if respawn != 1 and respawn != 2:
        print('You can only enter 1 or 2')
        raise SystemExit(0)
    IsWork = False
    position_throne = (192, 679) if respawn == 1 else (16, 846)
    IsWork = False
    keyb.add_hotkey('ctrl+shift+a', control)
    def move_mouse():
        time.sleep(1)
        start_position = mouse.get_position()
        mouse.move(position_throne[0], position_throne[1], duration=0.5)
        time.sleep(1)
        mouse.click('right')
        time.sleep(1)
        mouse.move(start_position[0], start_position[1], duration=0.5)
    while True:
        if keyb.is_pressed("ctrl+shift+a"):
            while IsWork:
                move_mouse()
if __name__ == '__main__':
    main()