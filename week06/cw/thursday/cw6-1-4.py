class SmartPhone:
    def __init__(self, brand, model, storage, battery, camera_magapixels, os):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery
        self.camera_magapixels = camera_magapixels
        self.os = os

    def install_app(self, app_name):
        print(f"{app_name} installed!")

    def make_call(self, number):
        print(f"Calling {number}...")

    def take_photo(self):
        print("Taking photo...")

    def check_battery(self):
        if self.battery < 20:
            print(f"{self.battery}: Battery is low!")
        elif self.battery == 100:
            print(f"{self.battery}: Battery is full!")
        else:
            print(f"{self.battery}")

iphone = SmartPhone("apple", "13", "128gb", 100, "64mp", "ios")
iphone.check_battery()
iphone.take_photo()
iphone.install_app("Instagram")
iphone.make_call("09121111111")