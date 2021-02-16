import fileFuzzer

exe_path = "C:\\Users\\Veronika\\PycharmProjects\\testFuzzer2\\vuln11.exe"
config_path = "C:\\Users\\Veronika\\PycharmProjects\\testFuzzer2\\config_11"

# vulns1\\

if __name__ == "__main__":

    print "1 - Auto-fuzzing"
    print "2 - Change byte\\bytes"
    print "3 - Add byte\\bytes"
    print "4 - Delete byte\\bytes"
    print "5 - Random mutation"
    print "6 - Find dividing fields"

    fuzzer = fileFuzzer.FileFuzzer(exe_path, config_path)

    while True:
        command = input("Enter command: ")

        if command == 1:
            fuzzer.auto_fuzzing()

        if command == 2:
            print "Enter start offset: "
            start_offset = input()
            print "Enter end offset: "
            end_offset = input()
            print "Enter symbol: "
            symbol = input()
            print "Enter amount: "
            amount = input()
            fuzzer.change_bytes(start_offset, end_offset, symbol, amount)

        if command == 3:
            print "Enter start offset: "
            start_offset = input()
            print "Enter symbol: "
            symbol = input()
            print "Enter amount: "
            amount = input()
            fuzzer.add_bytes(start_offset, symbol, amount)

        if command == 4:
            print "Enter start offset: "
            start_offset = input()
            print "Enter end offset: "
            end_offset = input()
            fuzzer.delete_bytes(start_offset, end_offset)

        if command == 5:
            fuzzer.mutate_file()

        if command == 6:
            fuzzer.find_dividing_fields()