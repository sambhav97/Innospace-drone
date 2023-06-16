from djitellopy import Tello

tello = Tello()
tello.connect()
tello.takeoff()
tello.move_up(20)
tello.go_xyz_speed(0,50,0,10) #X forward, Y left, Z height, Speed 17 seconds for everything

tello.move_up(30)
tello.move_down(30)
tello.move_up(20)
tello.move_down(20) #9 seconds one 30-20 up down

tello.move_up(30)
tello.move_down(30)
tello.move_up(20)
tello.move_down(20)

tello.go_xyz_speed(0,20,0,10) #2 seconds

tello.move_up(30)
tello.move_down(30)
tello.move_up(20)
tello.move_down(20)

tello.move_up(30)
tello.move_down(30)
tello.move_up(20)
tello.move_down(20)

tello.go_xyz_speed(0,-20,0,10) #2 seconds

tello.move_up(30)
tello.move_down(30)
tello.move_up(20)
tello.move_down(20)

tello.move_up(30)
tello.move_down(30)
tello.move_up(20)
tello.move_down(20)

tello.go_xyz_speed(0,20,0,10)

tello.move_up(30)
tello.move_down(30)
tello.move_up(20)
tello.move_down(20)

tello.move_up(30)
tello.move_down(30)
tello.move_up(20)
tello.move_down(20)

tello.go_xyz_speed(0,-20,0,10)

tello.move_up(30)
tello.move_down(30)
tello.move_up(20)
tello.move_down(20)

tello.land()

