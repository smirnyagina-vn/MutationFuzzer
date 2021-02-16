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
            start_offset = input("Enter start offset: ")
            end_offset = input("Enter end offset: ")
            print "Choose test case: "
            print fuzzer.test_cases
            test_case_index = input("Enter index of byte: ")
            amount = input("Enter amount: ")
            fuzzer.change_bytes(start_offset, end_offset, test_case_index, amount)
            continue

        if command == 3:
            start_offset = input("Enter start offset: ")
            print "Choose test case: "
            print fuzzer.test_cases
            test_case_index = input("Enter index of byte: ")
            amount = input("Enter amount: ")
            fuzzer.add_bytes(start_offset, test_case_index, amount)

        if command == 4:
            start_offset = input("Enter start offset: ")
            end_offset = input("Enter end offset: ")
            fuzzer.delete_bytes(start_offset, end_offset)

        if command == 5:
            fuzzer.mutate_file()

        if command == 6:
            fuzzer.find_dividing_fields()