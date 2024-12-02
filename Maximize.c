//教材中的求最大值程序
#include <stdio.h>
int main()
{
    int max(int x,int y);
    int a,b,c;
    scanf("%d,%d",&a,&b);
    c = max(a,b);
    printf("The max is %d\n",c);
    return 0;
}

int max(int x,int y)
{
    int z;
    if(x>y)z=x;  //判断
    else z=y;
    return(z);
}
/*
运行程序后，输入两个整数变量以比较大小。
C语言治好了我的空格癌（大嘘
*/
