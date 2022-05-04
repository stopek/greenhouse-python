class Log:
    @staticmethod
    def line():
        print("----------------------------------------------------------------------")

    @staticmethod
    def print(data):
        print(data)

    @staticmethod
    def empty(num: int = 1):
        for i in range(num):
            print()

    @staticmethod
    def log(text):
        print(text)
