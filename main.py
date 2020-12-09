import pyautogui
import time
from PIL import Image, ImageGrab


def hit (key):
    pyautogui.keyDown(key)


def isCollide (data):

    for i in range(150,270):
        for j in range(382, 461):
            if data[i, j]<150:
                hit('up')
                return True
    for i in range(150,180):
        for j in range(333,382):
            if data[i, j]<100:
                hit('down')
                return True
        return False

if __name__=='__main__':
    print('wait 3 second')
    time.sleep(3)
    #hit('up')

    while  True:
        image=ImageGrab.grab().convert('L')
        data=image.load()
        isCollide(data)

        # for i in range(170,240):
        #     for j  in range(343,378):
        #         data[i,j]=5
        #
        # # for i in range(10,240):
        # #     for j in range(388, 460):
        # #         data[i, j] = 150
        #
        # image.show()
        # break
