#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int ac, char *av[])
{
    int i;

    i = 0;
    if (ac == 1)
    {
        write(1, "Error\n", 6);
        exit(1);
    }
    while (i < ac)
    {
        printf("av[%i] = %s\n", i, av[i]);
        i++;
    }
}
