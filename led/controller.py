import pyfirmata

COM_PORT = "COM5"

board = pyfirmata.Arduino(COM_PORT)
led_1 = board.get_pin("d:13:o")
led_2 = board.get_pin("d:12:o")
led_3 = board.get_pin("d:11:o")

led_1.write(0)