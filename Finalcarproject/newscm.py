#The speed control class is instantiated in the main file.
#The class contains attributes such as default target speed, starting speed (0mph) and topspeed of the vehicle in which the module is fitted.
#It also contains all methods related to speed control: Acceleration, Decceleration, Emergency stopping and temporarily stopping at traffic lights.
class SpeedControl:
    """Speed control class contains all speed related methods."""
    def __init__(self,topspeed,defaultspeed,startingspeed):
        SpeedControl.maxspeed=topspeed
        SpeedControl.defaultspeedlimit=defaultspeed
        SpeedControl.startspeed=startingspeed

#This method changes the current speed to match the target speed
#I create the newspeed variable which I return to avoid changing the speed variable directly in this method.
    def changespeed(self,targetspeed,speed):
        
        """The changespeed function adjust current speed to target speed"""
        global newspeed
        newspeed = speed

#if the current speed is less than target speed, the car will accelerate to target speed.
#likewise if the current speed is greater, it will deccelerate. And if it is currently at target speed, it will continue at this speed.
        if targetspeed<speed:
            print("Accelerating..")
            while newspeed < targetspeed:
                newspeed+=1
            print("Car now travelling at " + str(newspeed) + "MPH")
            return newspeed
            assert newspeed == targetspeed, "Target speed not achieved"
            
        elif targetspeed>speed:
            print("Deccelerating..")
            while newspeed>targetspeed:
                newspeed-=1
            print("Car now travelling at " + str(newspeed) + "MPH")
            
            return newspeed
        else:
            print("Car travelling at " +str(speed) + "MPH")
            

#The emergency stop method will brake harshly cause the car to stop and shut down.    
    def emergStop(self,speed):
        """The emergency stop function stops the car completely"""
        global newspeed
        print("Emergency Stop!")
        newspeed = speed
        while newspeed > 0:
            newspeed -= 1
        print("Car has stopped due to object in the road.")
        assert newspeed == 0, "Emergency stop not achieved"
        return newspeed


#A red traffic light will cause the car to stop temporarily until the green light at which point it will return to previous speed.
# I use savespeed to record the speed prior to slowing. I then call on this variable when the green light is shown, so I can return to this previous speed.
# Again, I used the newspeed variable to avoid changing the speed variable directly.    
    def redTL(self,speed):
        """The red light function stops the car temporarily until the light goes green at which point it will resume previous speed"""
        global savespeed
        global newspeed
        print("Stopping at traffic light")
        savespeed = speed
        newspeed = speed
        while newspeed > 0:
            newspeed -= 1
        print("Car has stopped at the traffic lights. Awaiting green light..")
        assert newspeed == 0, "Target speed not achieved"
#Once the car has stopped it will wait for the prompt from the Sensor module. To simulate this, the user of this program must press enter to simulate the light turning green.
        greenyet=input("From Sensor module: Press enter when light turns green")

        print("Green light. Car will accelerate to previous speed")
        self.changespeed(0,savespeed)
        return savespeed

#If the light is green when the car is still travelling at pace, the car will continue travelling.    
    def greenTL(self):
        """The green light function allows the car to continue travelling at previous speed."""
        print("Traffic light is green. Car continues travelling at target speed.")



