#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void EnableXmodMap(void)
{
	char *binaryPath = "/bin/bash";
	char *arg1 = "/home/kos/Scriptutils/xmodmaps";
	execl(binaryPath, binaryPath, arg1, NULL);
}
