import machine

from classes.Log import Log

machine.freq(240000000)


def boot():
    Log.line()
    Log.log("In the jungle, welcome to the jungle")
    Log.log("Watch it bring you to your shananananana knees, knees")


if __name__ == '__main__':
    boot()
