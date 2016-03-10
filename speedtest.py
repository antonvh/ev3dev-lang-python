__author__ = 'anton'

# Run 1000 file accesses and measure time

import time
import ev3dev.auto as ev3

m = ev3.Motor(ev3.OUTPUT_A)
s = ev3.Sensor(ev3.INPUT_1)

t = time.time()

for i in range(1000):
    p = m.position
    v = s.value()
    m.duty_cycle_sp = 30

td = time.time() - t

print "Read/write time per action:", td