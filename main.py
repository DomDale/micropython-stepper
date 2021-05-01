from machine import Pin, PWM

# Motor pins
# Basic
Pstp = Pin(0, Pin.OUT)  # STP
stepPWM = PWM(Pstp)
stepPWM.duty_u16(32768)  # 50% duty cycle
stepPWM.freq(16)

Pfr = Pin(3, Pin.OUT)  # FR
Poe = Pin(5, Pin.OUT)  # OE
Prst = Pin(4, Pin.OUT)  # RST
Pst = Pin(6, Pin.OUT)  # ST
Pst.value(1)  # enable charge pump
Prst.value(1)  # keep in normal operation state

# disable output for now; OE must be enabled at least 0.5ms after ST is enabled
Poe.value(0)
Pfr.value(0)  # default clockwise

# Microstepping
Pmd1 = Pin(1, Pin.OUT)  # MD1
Pmd2 = Pin(2, Pin.OUT)  # MD2
Pmd1.value(1)  # Quarter step
Pmd2.value(1)


pmoni = Pin(7, Pin.IN)  # MONI
pemo = Pin(8, Pin.IN)  # EMO

# Button pins
Pswt1 = Pin(16, Pin.IN)  # SWT1
Pswt2 = Pin(17, Pin.IN)  # SWT2

while True:
    if (Pswt1.value() == 0 and Pswt2.value() == 0):
        print("12")  # stop
        if (Poe.value() == 1):
            Poe.value(0)
    elif (Pswt1.value() == 0):
        print("1")  # go one way
        if (Pfr.value() == 1):
            Pfr.value(0)
        if (Poe.value() == 0):
            Poe.value(1)
    elif (Pswt2.value() == 0):
        print("2")  # go the other
        if (Pfr.value() == 0):
            Pfr.value(1)
        if (Poe.value() == 0):
            Poe.value(1)
