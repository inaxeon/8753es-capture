import pyvisa as visa

def read_capture(resource_string="GPIB0::16::INSTR"):
    rm = visa.ResourceManager()
    instr = rm.open_resource(resource_string)
    # Override the default timeout as the transfer can exceed this
    instr.timeout = 10000
    instr.write("OPC?;SING")
    instr.write("OUTPPLOT")
    capture = instr.read_raw()
    with open('capture.hpgl', 'wb') as fp:
        for byte in capture:
            fp.write(bytes([byte]))
    instr.write("CONT")
    instr.write("OPC?;WAIT")
    instr.close()
    rm.close()
