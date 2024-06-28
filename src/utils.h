//
// Created by Thiago Sposito on 28/06/24.
//

#ifndef UTILS_H
#define UTILS_H

inline unsigned long hash(unsigned char *str)
{
    unsigned long hash = 5381;
    int c;

    while (c = *str++)
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

    return hash;
}




#endif //UTILS_H
