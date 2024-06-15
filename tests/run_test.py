#!/usr/bin/env python3
import os

from subprocess import Popen, PIPE
import sys
from collections.abc import Callable
bin_path: str = 'cmake-build-debug/raylib-base'


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
    if test_name in tests.keys():
        tests[test_name]()

    else:
        print(f"Unknown test: {test_name}")
        print("For more information use run_test --help ")
        return 1

def display_help():
    print(f"Availalble tests: {', '.join(key for key, _ in tests.items())}")


if __name__ == '__main__':
    if sys.argv[1] == '--help':
        display_help()
        print("Usage: run_test <test_name>")
    elif sys.argv[1] == '--generate-test-doc':
        pass
    else:

        if len(sys.argv) != 2:
            print("Usage: run_test <test_name>")
            print("For more information use run_test --help ")
            sys.exit(1)

        test_name = sys.argv[1]
        exit_code = main(test_name)
        sys.exit(exit_code)