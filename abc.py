import random
def dancing_lights(c1, c2, c3, r):
    if r <= 6:
        lights_seq = c1 * r + c3 * r + c2
        print(lights_seq)
    else:
        lights_seq = c2 * r  + c1* r + c3
        print(lights_seq)
r = random.randrange(1,10,1)
dancing_lights("blue","green","yellow", r)
dancing_lights("yellow", "green", "brown", r)
dancing_lights("blue", "green", "red", r)
