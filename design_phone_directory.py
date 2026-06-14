class PhoneDirectory:
    def __init__(self, maxNumbers):
        self.available = set(range(maxNumbers))

    def get(self):
        if not self.available:
            return -1
        return self.available.pop()

    def check(self, number):
        return number in self.available

    def release(self, number):
        self.available.add(number)


directory = PhoneDirectory(3)
print(directory.get())
print(directory.get())
print(directory.check(2))
print(directory.get())
print(directory.check(2))
directory.release(2)
print(directory.check(2))
