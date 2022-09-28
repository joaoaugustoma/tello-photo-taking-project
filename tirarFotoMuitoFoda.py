import cv2
from djitellopy import Tello
from time import sleep

me = Tello()
me.connect()

print("Bateria: ", me.get_battery())

me.takeoff()
sleep(20)
me.move_up(50)
sleep(20)
me.move_forward(70)
sleep(20)
me.send_rc_control(0, 0, 0, 30)
sleep(20)

#tirar foto
#me.streamon()
#frame_read = me.get_frame_read()
#cv2.imwrite("picture.png", frame_read.frame)
#sleep(10)

me.move_forward(70)
sleep(20)
me.land()