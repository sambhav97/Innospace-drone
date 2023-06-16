from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()

tello.move_up(30)

tello.rotate_counter_clockwise(90)
tello.move_left(150)
tello.rotate_clockwise(90)
tello.move_left(150)
tello.move_forward(150)
tello.move_right(150)

tello.move_back(150)
tello.move_left(60)

tello.land()

