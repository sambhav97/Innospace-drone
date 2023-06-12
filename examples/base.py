from djitellopy import tello

me = tello.Tello()
me.connect()
print(me.get_battery())

me2 = tello.Tello()
me2.connect()
print(me2.get_battery())

# drone1 = Tello()
# drone1.connect()
# print(drone1.get_battery())
#
# # Drone 2
# drone2 = Tello()
# drone2.connect()
# print(drone2.get_battery())

# tello1 = Tello()
# # tello2 = Tello()
#
# # connect to Tello drones
# tello1.connect()
# print(tello1.get_battery())

me.disconnent()
