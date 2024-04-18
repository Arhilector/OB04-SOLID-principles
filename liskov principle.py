class Bird():

    def fly(self):
        print ("птица летает")


class Duck(Bird):
    def fly(self):
        print("утка летает быстро")


def fly_in_the_sky(animal):
    animal.fly()


birdy = Bird()
ducky = Duck()

fly_in_the_sky(birdy)
fly_in_the_sky(ducky)

