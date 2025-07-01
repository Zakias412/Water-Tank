import sys

class Tank:
    def __init__(self,volume,capacity):
        self.volume = volume
        self.capacity = capacity
        self.is_flowing = False
    
    def Initial_stats(self):
        print(f"Current volume: {self.volume}L / Current Capacity: {self.capacity}L")
    
    def Begin_flow(self):
        Check_flow = input("Do you want to start water flow(y/n): ") 
        CHECK = Check_flow.strip().lower()
        if CHECK == "y":
            self.is_flowing = True
        elif CHECK == "n":
            print("Flow Prevented")
        else:
            print("Invalid Input")
            sys.exit()

    def flow(self):
        if not self.is_flowing:
            return
        else:
            try:
                Rate_flow = float(input("Enter the rate at which water will flow: "))
                if Rate_flow <= 0:
                    print("Impossible value of flow")
                    sys.exit
            
                Remaining_space = (self.capacity - self.volume)
                Time_taken = (Remaining_space/Rate_flow)
                print(f"It will take {Time_taken:.2f} seconds to fill the tank.")
            except ValueError as ve:
                print("Incorrect data inputted",ve)
                sys.exit()
            except ZeroDivisionError:
                print("Can't divide by zero")
                sys.exit()
    
def Main():
    try:
        Start_Volume = float(input("Enter the starting Volume: "))
        Start_Capacity = float(input("Enter the starting Capacity: "))

        if Start_Volume > Start_Capacity:
            print("Can't have greater Volume than Capacity")
            sys.exit()
    except ValueError as ve:
        print("Invalid data input",ve)
    
    Tank1 = Tank(Start_Volume,Start_Capacity)
    Tank1.Initial_stats()
    Tank1.Begin_flow()
    Tank1.flow()

if __name__ == "__main__":
    Main()