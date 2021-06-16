#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void EnableXmodMap(void)
{
	char *homedir = getenv("HOME");
	if (homedir != NULL) {
		char *binaryPath = "/bin/bash";
		char *arg1 = "/Scriptutils/xmodmaps";
		/* concatene homedir (/home/user) + arg1 */
		char *stcat = strcat(homedir, arg1);
		/* printf("%s\n", stcat); */
		execl(binaryPath, binaryPath, stcat, NULL);
	}

}
