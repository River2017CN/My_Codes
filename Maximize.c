/*
教材中的求最大值程序之课后习题，
由示例的两数取大者变更为了三数求最大者。
这显然不是最优解，希望我日后可以改进它。
ToDo：改为可以传入任意个参数的比较程序
*/
#include <stdio.h>
int max(int x,int y,int z)
{
    int ans;
    int cache;
    if(x>y)cache=x;  //判断
    else cache=y;
    if (cache>z)ans=cache;
    else ans=z;
    return(ans);
}
int main()
{
    int a,b,c,final;
    scanf("%d,%d,%d",&a,&b,&c);
    final = max(a,b,c);
    printf("The max is %d\n",final);
    return 0;
}


/*
运行程序后，输入两个整数变量以比较大小。
C语言治好了我的空格癌（大嘘
*/
