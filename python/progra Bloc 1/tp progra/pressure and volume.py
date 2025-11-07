pressure = float(input("presure :"))
volume = float(input("volume :"))
pressure_limit = 2.3
volume_limit = 7.41
if pressure_limit < pressure and volume_limit < volume :
    print("stop")
elif volume_limit < volume :
    print("volume need to decrease")
elif pressure_limit < pressure :
    print("volume need to  increase")
elif pressure < pressure_limit and volume < volume_limit :
    print("all it's ok")
