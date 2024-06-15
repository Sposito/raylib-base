#!/usr/bin/env python3
import os
from dataclasses import dataclass, field
from subprocess import Popen, PIPE
import sys

bin_path: str = '../cmake-build-release/raylib-base-test'
tests = dict()


def add_test(test):
    name:str = test.__name__
    name = name.replace('test_', '')
    tests[name] = test


def test_open_close() -> int:
    proc = Popen(bin_path, stdout=PIPE, stderr=PIPE)
    termination_status = proc.wait()
    std_out, std_err = proc.communicate()
    with open('test-output.log', 'w+') as file:
        file.write(std_out.decode('utf-8'))

    if termination_status != 0:
        print(f"Test failed with termination status {termination_status}")
        return 1
    return 0


add_test(test_open_close)


def main(test_name):
    import os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print("[PATH]: ", dir_path)

    if test_name in tests.keys():
        tests[test_name]()

    else:
        print(f"Unknown test: {test_name}")
        print("For more information use run_test --help ")
        return 1

def display_help():
    print_rgb(f"Availalble tests: {', '.join(key for key, _ in tests.items())}", 0, 255, 10)

def print_rgb(text, r, g, b):
    color_code = f"\033[38;2;{r};{g};{b}m"
    print(f"{color_code}{text}\033[0m")

def print_warning(text):
    print(f"[WARNING]: {text}", 255, 255, 0)


def flag_in_argv(flags: list[str]) -> bool:
    for flag in flags:
        if flag in sys.argv:
            return True
    return False


def get_payload(flags:list[str]) -> list[str]:
    indexes: list[int] = []
    argv_size = len(sys.argv)

    for element in flags:
        if element not in sys.argv:
            continue
        index = sys.argv.index(element)
        indexes.append(index)

    results: list[str] = []
    for index in indexes:
        if index >= argv_size:
            print_warning(f'The element {index} of flags tried to get an inexistant payload.')
            continue
        results.append(sys.argv[index + 1])

    return results


@dataclass()
class Flag:
    # flag_list: list[str]
    # present: bool
    # index: bool
    # payload: str = field(default_factory=lambda: "any" )
    # expect_payload: bool = False
    def __init__(self, flag_list, expect_payload=False):
        self.flag_list = flag_list
        self.expect_payload = expect_payload
        self.present = flag_in_argv(self.flag_list)
        self.payload = get_payload(flag_list) if expect_payload else None

    def __bool__(self):
        return self.present


class Flags:
    def __init__(self):
        self.help: Flag = Flag(['--help', '-h'])
        self.gdoc: Flag = Flag(['--generate-test-doc', '-d'])
        self.tbin: Flag = Flag(['--bin', '-b'], True)
        self.test: Flag = Flag(['--test', '-t'], True)

def gen_doc():
    with open('doc.md', 'w') as doc, open('../README.md','r') as readme:
        doc.writelines(readme.readlines())


if __name__ == '__main__':
    flags = Flags()

    if flags.help:
        display_help()
        print("Usage: run_test <test_name>")
        exit()

    if flags.gdoc:  # generate documentation
        gen_doc()
        exit()

    if not flags.test:
        print("Usage: python3 run_test.py --test{-t} <test_name> --tbin{-b}[optional] <path/to/binary>")
        print("For more information use run_test --help ")
        sys.exit(1)
    test_name: str = ''

    if len(flags.test.payload) >= 1:
        test_name = flags.test.payload[0]

    if not test_name:
        print_warning('You must provided a valid test name \n See python3 run_test.py --help')
        exit()

    if flags.tbin:
        if len(flags.tbin.payload) > 1:
            print_warning('You are supposed to use only short OR long form of a flag.')
            exit(1)
        if bool(flags.tbin.payload[0]):
            bin_path = flags.tbin.payload[0]

    exit_code = main(test_name)
    sys.exit(exit_code)