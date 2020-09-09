# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
#import webrepl
#webrepl.start()
gc.collect()


import network

#disabling access point interface
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect("<eesid>", "<password>")
        while not sta_if.isconnected():
            print(".",end="")
        print()
    print('network config:', sta_if.ifconfig())

# do_connect()