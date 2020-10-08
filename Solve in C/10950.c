#include<stdio.h>

int main()
{
	int a,b = 1,c,d;
	scanf_s("%d",&a);
	while(b<=a)
	{
		scanf("%d%2d",&c,&d);
		printf("%d",c+d);
		b++;
	}
	return 0;
 } 
