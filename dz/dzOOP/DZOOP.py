# Создадим интерфейс для логгера

class Logger:
    def log(self,message):
        pass

#реализуем логгер для вывода в консоль
class ConsoleLogger(Logger):
    def log(self,message):
        print(message)

#реализуем класс калькулятор
class Calculator:
    def __init__(self,logger):
        self.logger = logger

    def add(self,x,y):
        result = x + y
        self.logger.log(f"Сложение: {x} + {y} = {result}")
        return result

    def subtraction(self,x,y):
        result = x - y
        self.logger.log(f"Вычитание: {x} - {y} = {result}")
        return result

    def multiply(self,x,y):
        result = x * y
        self.logger.log(f"Умножение: {x} * {y} = {result}")
        return result

    def devide(self,x,y):
        result = x / y
        self.logger.log(f"Деление: {x} / {y} = {result}")
        return result

#Создаем калькулятор с заданным типом логгера.
class CalculatorFactory:
    def create(logger):
        return Calculator(logger)

if __name__ == "__main__":
    logger = ConsoleLogger()
    calculator = CalculatorFactory.create(logger)
    print(calculator.add(5,3))
    print(calculator.subtraction(8,4))
    print(calculator.devide(15,3))
    print(calculator.multiply(5,5))