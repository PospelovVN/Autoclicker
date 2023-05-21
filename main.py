import mouse
import keyboard as keyb
import time
# keyb.wait('a')
# c = mouse.get_position()
# print(c)
def main():
    try:
        respawn = int(input('Enter resp (1 - bottom / 2 - top)'))
    except:
        print('You entered a wrong integer')
        raise SystemExit(0)
    if respawn != 1 and respawn != 2:
        print('You can only enter 1 or 2')
        raise SystemExit(0)
    position_throne = (195, 713) if respawn == 1 else (10, 888)
    def move_mouse():
        time.sleep(5)
        start_position = mouse.get_position()
        mouse.move(position_throne[0], position_throne[1], duration=0.5)
        time.sleep(1)
        mouse.click('right')
        time.sleep(1)
        mouse.move(start_position[0], start_position[1], duration=0.5)
    keyb.wait('ctrl+shift+a')
    while True:
        move_mouse()
        if keyb.is_pressed('ctrl+shift+a') == True:
           break
if __name__ == '__main__':
    main()