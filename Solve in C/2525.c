#include<stdio.h>

int main()
{
	int total, hr, min, ti;
	scanf("%d %d",&hr,&min);
	scanf("%d",&ti);
	
	total = min + ti;
	
	if(total > 59)
	{
		min = total % 60;
		hr += total / 60;
		if(hr > 23)
		{
			hr = hr % 24;
		 } 
	}
	else
	{
		min = total;
	}
	printf("%d %d",hr,min);
	return 0;
}
