#include<stdio.h>

int main()
{
	int input;
	scanf("%d", &input);
	
	int out5 = input / 5;
	int count = 0;
	int out5_n = 0;
	int min_num = 0;
	for(;count <= out5;count ++)
	{
		out5_n = input - (count * 5);
		if((out5_n % 3) != 0)
		{
			continue;
		}
		else
		{
			min_num = count + (out5_n / 3);	
		}
	}
	if(min_num == 0)
	{
		min_num = -1;
	}
	printf("%d", min_num);
	return 0;
}
