from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()
tello.go_xyz_speed(0,-50,10,100) #X forward, Y left, Z height, Speed
tello.flip_right()
tello.go_xyz_speed(0,-50,10,10) #X forward, Y left, Z height, Speed
tello.flip_right()
tello.land()

