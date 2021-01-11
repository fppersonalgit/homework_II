from time import sleep


class TrafficLight():
    __color = ["Red", "Yellow", "Green"]

    def running(self):
        tick = 0
        while tick != 3:
            print(TrafficLight.__color[tick])
            if tick == 0:
                sleep(7)
            elif tick == 1:
                sleep(5)
            elif tick == 2:
                sleep(2)

            tick += 1


t_Light = TrafficLight()
t_Light.running()