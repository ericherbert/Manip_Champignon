


def switch_light(on):
    "close or open thorlabs MFF102/M optical switch. 1=on, 0=off"   
    # 0 = lumiere allumé, 1 = lumiere éteinte     
    import thorlabs_apt_protocol as apt
    import serial

    #port= serial.Serial("COM8", 115200, rtscts=True)
    port= serial.Serial("/dev/ttyUSB2", 115200, rtscts=True)
    port.rts = True
    port.reset_input_buffer()
    port.reset_output_buffer()
    port.rts = False

    if on:
        port.write(apt.mot_move_jog(dest=57, source=4, chan_ident=1, direction=1))

    else:
        port.write(apt.mot_move_jog(dest=57, source=4, chan_ident=1, direction=2))

    port.close()	 

    return 





