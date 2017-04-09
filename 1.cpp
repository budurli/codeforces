#include <stdio.h>

int main()
{
    long long int n, m, a;
    scanf("%lld %lld %lld",&n,&m,&a);
    n = (n+(a-1))/a;
    m = (m+(a-1))/a;
    printf("%lld\n",n*m);
    return 0;
}