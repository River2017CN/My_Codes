//这是一个输入圆半径求圆的半径与面积的程序，用于帮助检验简单学习printf与scanf的成果。
#include <stdio.h>
int main()
{
	float r,a1,a2,pae;	//我也忘了为啥要叫pae
	pae=3.1415926;
	printf("请输入圆的半径：\n");
	scanf("%f",&r);
	a1=2*pae*r;
	a2=pae*r*r;
	printf("圆的周长是%f，圆的面积是%f。",a1,a2);
	return 0;
}
