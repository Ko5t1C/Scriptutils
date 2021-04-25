#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void Keyled(void)
{
	char *binaryPath = "/bin/bash";
	char *arg1 = "/home/kos/Scriptutils/clavier";
	execl(binaryPath, binaryPath, arg1, NULL);
}
