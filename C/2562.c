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
			location = count + 1; //���������� 85�� �ε��� �ѹ� 7�ε��� ��ġ 8�̶� ��� 
		}
		count ++;
	}
	printf("%d\n",max);
	printf("%d\n", location);
	return 0;
}
