
#ifndef CMD_HANDLER_H
#define CMD_HANDLER_H

#include<string.h>
#include<stdlib.h>
#include<stdio.h>
#include<utils.h>


const int* cmdH_arg_count;
const char** cmdH_arg_values;
int cmdH_initialized = 0;
long long* arg_hashes;
enum CMD_ARGS{TIMEOUT=2};

inline int cmdH_init(const int* argc, const char *argv[]) {
    cmdH_arg_count = argc;
    cmdH_arg_values = argv;
    cmdH_initialized = 1;
    arg_hashes = (long long *) malloc(*argc * sizeof(long long));
    for (int i = 0; i < *cmdH_arg_count; i++) {
        arg_hashes[i] = hash(argv[i]);
    }

    return 0;
}



inline int cmdH_delete() {
    cmdH_initialized = 0;
    free(arg_hashes);
    return 0;
}

inline int cmdH_getArgumentPayload(const char* argument, char** payload) {
    if (cmdH_arg_count < 1) {
        return 1;
    }
    for(int i = 0; i < *cmdH_arg_count; i++) {
        if(hash(argument) == arg_hashes[i]) {
           int size = strlen(cmdH_arg_values[i]);
            if (size > 0) {
                payload = &cmdH_arg_values[i];
            }

        }
    }
    return 0;
}

#endif //CMD_HANDLER_H
