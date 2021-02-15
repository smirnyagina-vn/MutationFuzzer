import time
import subprocess
from debugger import *
from winappdbg import *


class FileFuzzer:
    def __init__(self, exe_path, conf_file_path, conf_dir_path, conf_num):
        self.conf_file_path = conf_file_path
        self.conf_dir_path = conf_dir_path
        self.conf_num = conf_num
        self.exe_path = exe_path
        self.offset = 1
        self.mutation = 1
        self.running = False
        self.ready = False

        with open(conf_file_path, 'rb') as f:
            self.orig_data = list(f.read())

        def auto_fuzzing():
            while 1:
                if not self.running:
                    self.mutate_file()
                    # new debugging thread
                    proc = subprocess.Popen([self.exe_path], stdout=subprocess.PIPE)
                    status = subprocess.Popen.wait(proc)

                    print('Error ', status)
                    print(proc.stdout.read())

                    # if status != 0:
                    # simple_debugger([self.exe_path])

                else:
                    time.sleep(1)
            return

        def mutate_file(self):
            return

        def start_debugger():
            return

        def get_dividing_fields():
            symbFF = (0xff).to_bytes(1, 'big')
            main_config = open(conf_file_path, "br")
            main_config_text = main_config.read()
            main_config.close()
            main_size = len(main_config_text)  # 1 config size

            for i in range(1, 24):
                if i != conf_num:
                    text = b''
                    cur_config = open(conf_dir_path + 'config_' + str(i), "br")
                    cur_config_text = cur_config.read()
                    cur_config.close()
                    cur_size = len(cur_config_text)  # others config size

                    if main_size > cur_size:
                        main_size = cur_size
                        main_config_text = main_config_text[:main_size]
                    else:
                        cur_config_text = cur_config_text[:main_size]

                    for j in range(0, main_size):
                        if cur_config_text[j] == main_config_text[j]:
                            text += cur_config_text[j].to_bytes(1, 'big')
                        else:
                            text += symbFF

                    main_config_text = text

            fields = []
            i = 0
            while i < len(main_config_text):
                if main_config_text[i] == 0xff:
                    field = [i + 1]
                    while (i < len(main_config_text)
                           and main_config_text[i] == 0xff):
                        i += 1
                    field.append((i - 1) + 1)
                    fields.append(field)
                i += 1

            for field in fields:
                print(field)
            return

        def change_bytes(start_index, value):
            config_file = open(conf_file_path, "br")
            config_text = config_file.read()
            config_file.close()

            end_index = start_index + len(value) + 1
            config_text = config_text[:start_index] + value + config_text[end_index:]
            config_file = open(conf_file_path, "bw")
            config_file.write(config_text)
            config_file.close()
            return

        def add_bytes(index, value):
            config_file = open(conf_file_path, "br")
            config_text = config_file.read()
            config_file.close()
            config_text = config_text[:index - 1] + value + config_text[index - 1:]

            config_file = open(conf_file_path, "bw")
            config_file.write(config_text)
            config_file.close()
            return

        def delete_bytes(start_index, end_index):
            config_file = open(conf_file_path, "br")
            config_text = config_file.read()
            config_file.close()

            if (start_index > len(config_text)
                    or end_index > len(config_text)
                    or end_index < start_index
                    or end_index <= 0
                    or start_index <= 0):
                print('\nIncorrect args for deleting bytes')
                return

            config_text = config_text[:start_index - 1] + config_text[end_index:]
            config_file = open(conf_file_path, "bw")
            config_file.write(config_text)
            config_file.close()
            return
