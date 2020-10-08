#include<stdio.h>

int main()
{
	int count = 0, max = 0,location = 0;
	int qw[9];
	while(count < 9)
	{
		scanf("%d",&qw[count]);
		if(qw[count] > max)
		{
			max = qw[count];
			location = count + 1; //예제에서는 85가 인덱스 넘버 7인데도 위치 8이라 출력 
		}
		count ++;
	}
	printf("%d\n",max);
	printf("%d\n", location);
	return 0;
}
