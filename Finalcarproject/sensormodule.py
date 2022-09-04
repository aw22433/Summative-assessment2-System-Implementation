#Sensor is the superclass which shares its attributes (location in car and car type) with the sensor components,
#Each of the sub classes below are instantiated in the main document
class Sensor:
    """The Sensor superclass contains location in car and car type attributes which it passes to Speedlimit, Trafficlight and Object detection subclasses"""
    def __init__(self,locationincar,cartype):
        Sensor.location = locationincar
        Sensor.carmake = cartype


#The speed limit class allows us to create an object to represent each speed limit sign we detect
#This class allows us to change the speed limit which becomes the new target speed our car will strive to travel at assuming no other obstructions
class Speedlimit(Sensor):
    """Represents a speed limit sign detected by the sensor module"""
    def __init__(self, limit):
        self.newspeedlimit = limit

#The traffic light class allows us to create an object to represent each traffic light
#The class contains the color of the traffic light (red/green) which dictates how we react to it
class TrafficLight(Sensor):
    """Creates a profile for a traffic light"""
    def __init__(self, color):
        self.col = color


#The object detection class allows us to create objects to represent object in the road.
#We store each of these object in a list which can then be sent to the manufacturer at the end of each journey to allow improvement on the object detection software
class Objectdetection(Sensor):
    """Creates a profile for objects in the road"""
    def __init__(self, Description,risk):
        self.description=Description
        self.Collisionrisk=risk


