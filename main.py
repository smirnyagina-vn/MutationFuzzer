import FileFuzzer

badBytes = [b'\x00', b'\x80', b'\x7f', b'\xff',
            b'\x7f\xff', b'\x80\x00', b'\x7f\xfe', b'\xff\xff',
            b'\x7f\xff\xff\xff', b'\x80\x00\x00', b'\x7f\xff\xff\xfe', b'\xff\xff\xff',
            b'\x7f\xff\xff\xff\xff', b'\x80\x00\x00\x00', b'\x7f\xff\xff\xff\xfe', b'\xff\xff\xff\xff']

if __name__ == "__main__":

    print "1 - Auto-fuzzing\n"
    print "2 - Change byte\\bytes\n"
    print "3 - Add byte\\bytes\n"
    print "4 - Show config file\n"
    print "5 - Save file\n"
    print "6 - Parse config files"

    while True:
        command = input("Enter command:\n")

        # if command == 1:

        # if command == 2:

        # if command == 3:

        # if command == 4:

        # if command == 5:

        # if command == 6:
