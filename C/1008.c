#include<stdio.h>

int main(){
	int a, b;
	scanf("%d%d",&a, &b);
	printf("%.9f\n", (double)a / b);
	/*A�� B�� ����ϵ� ����/��� ������ E-9 ���� �ȴٰ� �����Ƿ� %f�տ� �Ҽ��� .9�� �پ��־�� �Ѵ�. */
	return 0;
}

