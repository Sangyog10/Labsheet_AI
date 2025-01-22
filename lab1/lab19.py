class Engine:
    def __init__(self, engine_type):
        self.type = engine_type

    def start(self):
        print(f"Engine of type {self.type} started.")

    def stop(self):
        print(f"Engine of type {self.type} stopped.")

class Wheel:
    def __init__(self, wheel_type):
        self.type = wheel_type

    def rotate(self):
        print(f"Wheel of type {self.type} is rotating.")

class Car:
    def __init__(self, engine_type, wheel_type):
        self.engine = Engine(engine_type)
        self.wheels = [Wheel(wheel_type) for _ in range(4)] 

    def start_car(self):
        self.engine.start()
        for wheel in self.wheels:
            wheel.rotate()
        print("Car started.")


my_car = Car(engine_type="V8", wheel_type="Alloy")
my_car.start_car()
