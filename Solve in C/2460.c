#include<stdio.h>

int main()
{
	int count = 1,passenger = 0,all = 0,a = 0, b = 0; //a -> 나가는사람 b -> 타는사람 
	while(count <= 10)
	{
		scanf("%d %d",&a,&b);
		passenger = passenger + b -a;
		if(passenger > all)
		{
			all = passenger;
		}
		count ++;
	}
	printf("%d",all);
	return 0;
}
