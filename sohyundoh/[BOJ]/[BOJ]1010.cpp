﻿
#include <stdio.h>

long long rs_nCr(int n, int r)
{
    int i, j, t = n - r;
    long long res = 1.;

    if (t < r) t = n - (r = n - r);
    for (i = t + 1; i <= n; ++i) res *= i;
    for (i = 2; i <= r; ++i) res /= i;
    return res;
}

int main()
{
    int T, N, R;

    scanf("%d", &T);
    for (int i = 0; i < T; i++)
    {
        scanf("%d %d", &R, &N);
        printf("%lld\n", rs_nCr(N, R));
    }
    return 0;
}
﻿