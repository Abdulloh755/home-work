class Calcukator:
    def __init__(self, value=0):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Calcukator):
            return Calcukator(self.value + other.value)
        else:
            return Calcukator(self.value + other)

    def __sub__(self, other):
        if isinstance(other, Calcukator):
            return Calcukator(self.value - other.value)
        else:
            return  Calcukator(self.value - other)

    def __mul__(self, other):
        if isinstance(other, Calcukator):
            return  Calcukator(self.value * other.value)
        else:
            return Calcukator(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, Calcukator):
            if other.value ==0:
                raise ValueError("Деление на ноль невозможно")
            return  ValueError(self.value / other.value)
        elif other == 0:
            raise ValueError("Деление на ноль невозможно")
        else:
            return Calcukator(self.value / other)

    def __str__(self):
        return str(self.value)

if __name__ == "__main__":
    calc1 = Calcukator(10)
    calc2 = Calcukator(5)

    result_add = calc1 + calc2
    result_sub = calc1 - calc2
    result_mul = calc1 * calc2
    result_div = calc1 / calc2

    print(f"Сложение:   {result_add}")
    print(f"Вычитание: {result_sub}")
    print(f"Умножение: {result_mul}")
    print(f"Деление: {result_div}")
