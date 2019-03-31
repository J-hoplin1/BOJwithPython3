#include<stdio.h>

int main(){
	int a, b;
	scanf("%d%d",&a, &b);
	printf("%.9f\n", (double)a / b);
	/*A와 B를 출력하되 절대/상대 오차는 E-9 까지 된다고 했으므로 %f앞에 소수점 .9를 붙어주어야 한다. */
	return 0;
}

