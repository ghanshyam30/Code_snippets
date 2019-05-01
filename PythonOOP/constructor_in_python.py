class Laptop:
    # Attributes
    pass
    # Methods
    def __init__(self):
        self.band_name = "Lenovo"
        self.processor = "Intel core i5 gen 1"
        self.ram = "2 GB"
        # Multiline print statement implementation
        print("""
Brand Name = {0}
Processor = {1}
Ram size = {2}
        """.format(self.band_name,self.processor,self.ram))


# Object creation
laptop1 = Laptop()  # When ever we create an object it executes constructor automatically if exists.


print("""The configurations of Laptop 1 are as follows-
{3}
Brand Name = {0}
Processor = {1}
Ram size = {2}
        """.format(laptop1.band_name,laptop1.processor,laptop1.ram,40*"-"))

'''
OUTPUT -
------
Brand Name = Lenovo
Processor = Intel core i5 gen 1
Ram size = 2 GB

The configurations of Laptop 1 are as follows-
----------------------------------------
Brand Name = Lenovo
Processor = Intel core i5 gen 1
Ram size = 2 GB
'''