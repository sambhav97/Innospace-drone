from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()

tello.rotate_counter_clockwise(90)
tello.move_left(100)
tello.rotate_clockwise(90)
tello.move_left(100)
tello.move_forward(100)
tello.move_right(100)

tello.move_back(100)
tello.move_left(40)

tello.land()

