from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def compress(self):
        pass

    @abstractmethod
    def release(self):
        pass

    @abstractmethod
    def cool(self):
        pass

    @abstractmethod
    def heat(self):
        pass


class Solid(State):
    def __init__(self, matter: 'Matter'):
        self.__matter = matter

    def compress(self):
        print("Compressing")

    def release(self):
        print("Releasing")
        self.__matter.changeState(Liquid(self.__matter))
    
    def cool(self):
        print("Cooling")
    
    def heat(self):
        print("Heating")
        self.__matter.changeState(Liquid(self.__matter))

    def __str__(self):
        return "Solid"

class Liquid(State):
    def __init__(self, matter: 'Matter'):
        self.__matter = matter

    def compress(self):
        print("Compressing")
        self.__matter.changeState(Solid(self.__matter))
    
    def release(self):
        print("Releasing")
        self.__matter.changeState(Gas(self.__matter))
    
    def cool(self):
        print("Cooling")
        self.__matter.changeState(Solid(self.__matter))
    
    def heat(self):
        print("Heating")
        self.__matter.changeState(Gas(self.__matter))
    
    def __str__(self):
        return "Liquid"

class Gas(State):
    def __init__(self, matter: 'Matter'):
        self.__matter = matter

    def compress(self):
        print("Compressing")
        self.__matter.changeState(Liquid(self.__matter))
    
    def release(self):
        print("Releasing")

    def cool(self):
        print("Cooling")
        self.__matter.changeState(Liquid(self.__matter))
    
    def heat(self):
        print("Heating")
    
    def __str__(self):
        return "Gaseous"

class Matter:
    def __init__(self, name: str):
        self.__name = name
        self.__state =  Liquid(self) #change this to the appropriate initial state (liquid)
    
    def changeState(self, newState):
        self.__state = newState
    
    def compress(self):
        self.__state.compress()
    
    def release(self):
        self.__state.release()
    
    def cool(self):
        self.__state.cool()
    
    def heat(self):
        self.__state.heat()
    
    def __str__(self):
        return "%s is currently a %s" % (self.__name, self.__state) #formatting strings just like you format strings in C

def main():
    a = Matter("Water")
    print(a)
    a.compress()
    print(a)
    a.heat()
    print(a)
    a.heat()
    print(a)
    a.cool()
    print(a)
    a.cool()
    print(a)
    a.compress()
    print(a)

if __name__ == "__main__":
    main()