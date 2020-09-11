import machine
import uos

def main():
    try:    
        uos.dupterm(None, 1) # disable REPL on UART(0)
    
        uart = machine.UART(0)                 
        uart.init(115200, timeout=3000) 

        while True:
            if uart.any():
                hostMsg = uart.readline()
                if hostMsg is not None:                    
                    strMsg = hostMsg.decode().strip('\r\n')
                    if strMsg == '\x00':
                        raise Exception
                    else:                        
                        uart.write('I received: ' + strMsg + '\r\n')                                    
    except Exception:
        uart.write('Exception was raised')
    finally:
        uos.dupterm(machine.UART(0, 115200), 1)

# Run main loop
main()