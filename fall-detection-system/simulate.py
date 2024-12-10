# IMU-simulated fall detection using magnitude threshold
import random, time, math
def mag(ax,ay,az): return math.sqrt(ax*ax+ay*ay+az*az)
while True:
    if random.random()<0.03:
        ax,ay,az = [random.uniform(30,60) for _ in range(3)]
    else:
        ax,ay,az = [random.uniform(-2,2) for _ in range(3)]
    m = mag(ax,ay,az)
    if m>25:
        print('ALERT: fall detected, mag=',round(m,2))
    time.sleep(0.2)