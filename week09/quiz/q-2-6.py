class Singleton:
   instance = None
   def __new__(cls):
       if not cls.instance:
           cls.instance = super().__new__(cls)
       return cls.instance