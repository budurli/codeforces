#include <stdio.h>

int main()
{
    short int w;
    scanf("%hi", &w);
    if ((w % 2 == 0) && (w > 3))
        printf("YES\n");
    else
        printf("NO\n");
}