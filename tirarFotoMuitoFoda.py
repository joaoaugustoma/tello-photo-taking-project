from time import sleep

import cv2
from djitellopy import Tello

me = Tello()
me.connect()

print("Bateria: ", me.get_battery())
me.streamon()

me.takeoff()
sleep(3)
me.move_up(200)
me.move_forward(400)
me.rotate_counter_clockwise(180)

#tirar foto
frame_read = me.get_frame_read()
cv2.imwrite("picture.png", frame_read.frame)

me.move_forward(390)
me.rotate_counter_clockwise(180)
me.move_down(200)
me.land()