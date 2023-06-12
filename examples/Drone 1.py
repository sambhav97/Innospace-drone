from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()
tello.go_xyz_speed(0,100,50,10) #X forward, Y left, Z height
tello.land()

