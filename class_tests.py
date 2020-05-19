import dis

class FirstSingleton:

    __instance = None

    def __init__(self):
        if FirstSingleton.__instance != None:
            raise "Error"
        else:
            FirstSingleton.__instance = self

    @staticmethod
    def getInstance():
        if FirstSingleton.__instance == None:
            FirstSingleton()
        return FirstSingleton.__instance

    def doSomething(self):
        self.location = ""
        

class SecondSingleton:

    __instance = None

    def __init__(self):
        if SecondSingleton.__instance != None:
            raise "Error"
        else:
            SecondSingleton.__instance = self

    @classmethod
    def getInstance(cls):
        if cls.__instance == None:
            cls()
        return cls.__instance

    def doSomething(self):
        self.location = ""

print("FirstSingleton")
print(dis.disco(FirstSingleton))
print("SecondSingleton")
print(dis.disco(SecondSingleton))