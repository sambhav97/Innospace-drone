from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()

tello.move_up(30)
tello.move_forward(100)
tello.move_down(30)

tello.rotate_counter_clockwise(360)

tello.land()

