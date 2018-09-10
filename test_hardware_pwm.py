import pigpio

pi = pigpio.pi()
pi.hardware_PWM(18, 38000, 500000)
