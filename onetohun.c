#include <stdio.h>


int main(int argc,char **argv)
{
	char *seq_args[] = {"seq", "100", NULL};
  	execvp("seq", seq_args);
	return 0;
}
