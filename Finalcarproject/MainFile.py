#importing the Speed control module and sensor module files which provide Speed control and sensor classes
#I kept these files seperate to keep the code easier to read, and to maintain a modular design.
#In theory, the 'Speed control' and 'Sensor' modules could be fitted to another vehicle
import newscm
import sensormodule

#creating global speed variable which defaults to zero at the start of the journey since the car wont be in motion.
global speed
speed=0

#Driver input required to start the car
Drivercommand = input("Press enter to start journey")
#In real conditions the default target speed would be taken from the GPS system however since this module does not exist in the simulation, the user is required to simulate this initial target speed
defaultspeed = input("FROM GPS module: Please enter default speed? ")

#This list stores details of all physical objects detected in the road. 
#I chose to store these in a list as it is the most suitable for objects in this use case.
#This can then be sent to manufacturer for future development 
objects=[]

# The car class is the primary class for this program, allowing us to call on the speed control and sensor modules.
class Car:
    """The car class provides methods which link the sensor module data with the speed control module to allow the car to drive"""
    def __init__(self,speed):
        self.speed = speed

#This method acts when the sensor module detects a speed sign.
#It instantiates a speed sign object, then it sets a new speed limit and calls on the speed control module to adjust the speed to this new target
# In this simulation, it requires the user to input the new speed limit. In real practice, this would come from the camera 
    def speedlim(self, speed):
        """Method to instantiate a speed sign object and to adjust the current speed to the new limit"""
        slimit = input("Speed limit on sign: ")
        speedlimit1 = sensormodule.Speedlimit(int(slimit))
        print("Speed sign detected, new speed limit is " + str(speedlimit1.newspeedlimit) + "MPH")
        targetspeed = speedlimit1.newspeedlimit
        Speedmodule.changespeed(speed,targetspeed)
        global Nspeed
        Nspeed = newscm.newspeed

        return Nspeed
        
        

#This method is called on when the sensors detect a traffic light.
#In this simulation, the user must say which color the light is.
#It instantiates a traffic light object using the applicable class and calls on applicable methods to react accordingly.
    def traffic_li(self, speed):
        """Method to instantiate the traffic light object and to make the car act accordingly"""
        print("traffic light detected")
        tlcolor = input("Traffic light color red or green: ")
        trafficlight1 = sensormodule.TrafficLight(tlcolor)

        if trafficlight1.col=="red":
            Speedmodule.redTL(speed)
            global Nspeed
            Nspeed = newscm.savespeed
            
        elif trafficlight1.col=="green":
            Speedmodule.greenTL()
#if the input from the sensor is unexpected, the driver is prompted to take over
        else:
            print("Traffic light detection failure - unexpected input - Driver to take over control")
            quit()

#This method is called on when the sensors detect an object.
#It will record a description of the object and whether it is a risk. It will save these to a list for use later
#It instantiates an object using the applicable class and calls on applicable methods to react accordingly.
    def obj(self, speed):
        print("Object detected")
        objectdescription=input("Description of object?")
        objectrisk=input("Object is a risk? yes or no: ")
        object1=sensormodule.Objectdetection(objectdescription, objectrisk)
        objects.append(object1)
        risklevel=object1.Collisionrisk

#if the object is a risk, it will call the emergency stop method
        if risklevel == "yes":
            Speedmodule.emergStop(speed)
            speed = newscm.newspeed
            assert speed == 0, "Emergency stop failed"
            quit()
#if there is no risk, the car will continue to travel                
        elif risklevel == "no":
            print("no risk detected. Car continues")
            main()
#if the car cant detect risk level, it will prompt the driver to take over
        else:
            print("Sensor module failure - unexpected input - Driver to take over control")
            quit()

#When the destination is reached, the car is stopped and the driver alerted
    def endJ(self, speed):
        Speedmodule.changespeed(speed,0)
        speed = newscm.newspeed
        assert speed == 0, "Final stop failed"
        print("Destination reached. Car stopped.")
    


targetspeed= int(defaultspeed)
car_top_speed = 200
#The speed control module is instantiated
Speedmodule = newscm.SpeedControl(car_top_speed,int(defaultspeed),speed)

#The car accelerates to initial target speed 
Speedmodule.changespeed(speed,targetspeed)
speed = newscm.newspeed

#The sensor box is the instantiated with car specific details
carsensorbox = sensormodule.Sensor("back", "modelT")
mycar = Car(speed)


#This loop allows us to simulate the journey by entering numbers to simulate each of our functions.
#The loop will keep repeating and await further signals from signs, traffic lights and objects in the road (in this case inputs from the user)
def main():
    global speed
    sensorinput = input("FROM SENSOR MODULE: 1 for speed limit sign, 2 for traffic light, 3 for object detected, 4 to end journey: ")

# 1 simulates a speed limit sign. The user will input the new limit, and the car will react accordingly
    if sensorinput == "1":
        mycar.speedlim(speed)
        speed = Nspeed
        assert speed != 0, "Speed limit not achieved"
        main()

# 2 represents a traffic light. Again, the user must input the applicable color and the car will react
    elif sensorinput== "2":
        mycar.traffic_li(speed)
        speed= Nspeed
        assert speed != 0, "Traffic light issue"
        main()
        
# 3 will simulate an oject in the road.        
    elif sensorinput == "3":
        mycar.obj(speed)   
        main()

# 4 will end the journey
    elif sensorinput == "4":
        mycar.endJ(speed)
        print("All data collected about detected objects sent to Manufacturer for improvement of object recognition")
        print(objects)
        
#if input is not recognised, the driver is prompted to take over
    else: 
        print("Sensor module failure - Driver to take over control")
        quit()

  
main()









