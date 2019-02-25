import vpython as vp

measuringRod = vp.cylinder(length=6, color=color.yellow, radius=0.5, pos=vector(-3,0,0))

while True:
    rate(20)
    measuringRod.length = random.randint(1,5)

