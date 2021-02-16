import random
import subprocess
import MyDebugger


class FileFuzzer:
    def __init__(self, exe_path, conf_file_path):
        self.conf_file_path = conf_file_path
        # self.conf_dir_path = conf_dir_path
        # self.conf_num = conf_num
        self.exe_path = exe_path
        self.offset = 1
        self.iteration = 1
        self.running = False

        # self.test_cases = [b'\x00', b'\x80', b'\x7f', b'\xff',
        #                   b'\x7f\xff', b'\x80\x00', b'\x7f\xfe', b'\xff\xff',
        #                   b'\x7f\xff\xff\xff', b'\x80\x00\x00', b'\x7f\xff\xff\xfe', b'\xff\xff\xff',
        #                   b'\x7f\xff\xff\xff\xff', b'\x80\x00\x00\x00', b'\x7f\xff\xff\xff\xfe', b'\xff\xff\xff\xff']

        self.test_cases = ["\x00", "\x80", "\x7f", "\xff",
                           "\x7f\xff", "\x80\x00", "\x7f\xfe", "\xff\xff",
                           "\x7f\xff\xff\xff", "\x80\x00\x00", "\x7f\xff\xff\xfe", "\xff\xff\xff",
                           "\x7f\xff\xff\xff\xff", "\x80\x00\x00\x00", "\x7f\xff\xff\xff\xfe", "\xff\xff\xff\xff",
                           "%s%n%s%n%s%n"]

        #                          ';'      ' '     '.'      ','
        self.dividing_fields = [b'\x3B', b'\x20', b'\x2E', b'\x2C',
                                b'\x21', b'\x3F', b'\x3A', b'\x2F']
        #                          '!'     '?'      ':'       '/'

    def auto_fuzzing(self):
        while 1:

            self.mutate_file()

            # New debugging thread
            proc = subprocess.Popen([self.exe_path], stdout=subprocess.PIPE)
            status = subprocess.Popen.wait(proc)

            print('Error ', status)
            print(proc.stdout.read())

            if status != 0:
                MyDebugger.simple_debugger([self.exe_path])

        return

    def mutate_file(self, rand_range=1000):

        fd = open(self.conf_file_path, "rb")
        stream = fd.read()
        fd.close()

        rand_index = random.randint(0, len(self.test_cases) - 1)
        test_case = self.test_cases[rand_index]
        stream_length = len(stream)
        rand_len = random.randint(1, rand_range)

        # Now take the test case and repeat it
        test_case = test_case * rand_len

        print "File mutation #", self.iteration
        print "Current offset: ", self.offset
        print "Test case`s index: ", rand_index
        print "Test length: ", len(test_case)

        fuzz_file = stream[0:self.offset]
        fuzz_file += bytes(test_case)
        fuzz_file += stream[self.offset:]

        fd = open(self.conf_file_path, "wb")
        fd.write(fuzz_file)
        fd.close()

        # Upgrade the offset
        self.offset += len(test_case)
        self.iteration += 1

        return

    def find_dividing_fields(self):

        exist = False

        fd = open(self.conf_file_path, "rb")
        fd_text = fd.read()
        fd.close()
        fd_size = len(fd_text)

        for fd_iterator in range(0, fd_size):
            for iterator in range(0, len(self.dividing_fields)):
                if fd_text[fd_iterator] == self.dividing_fields[iterator]:
                    exist = True
                    print "Dividing field found - ", str(self.dividing_fields[iterator])
                    print "Offset: ", fd_iterator

        if exist is False:
            print "There is no dividing fields in the file"

        return

    def change_bytes(self, start_offset, end_offset, index, amount):
        self.delete_bytes(start_offset, end_offset)
        self.add_bytes(start_offset, index, amount)
        return

    def add_bytes(self, file_offset, index, amount):

        fd = open(self.conf_file_path, "rb")
        stream = fd.read()
        fd.close()

        if file_offset > len(stream):
            file_offset = len(stream)

        new_bytes = self.test_cases[index] * amount

        fuzz_file = stream[0:file_offset]
        fuzz_file += bytes(new_bytes)
        fuzz_file += stream[file_offset:]

        fd = open(self.conf_file_path, "wb")
        fd.write(fuzz_file)
        fd.close()

        return

    def delete_bytes(self, start_offset, end_offset):

        fd = open(self.conf_file_path, "rb")
        stream = fd.read()
        fd.close()

        if end_offset > len(stream):
            end_offset = len(stream)

        fuzz_file = stream[0:start_offset - 1]
        fuzz_file += stream[end_offset:]

        fd = open(self.conf_file_path, "wb")
        fd.write(fuzz_file)
        fd.close()

        return
