# include <stdio.h>
int h(int n);
int f(int n);
int main()
{
  int n;
  printf("Give n ");
  scanf("%d", &n);
  printf("f:%d\n", f(n));  
  printf("h:%d\n", h(n));
}

int h(int n)
{
  if (n == 1 || n==2)
    return 1;
  else
    return h(n-1) + h(n-2);
}

int f(int n)
{
  int i, t,a,b;
  a = b = 1;
  for (i = 1; i < n; i++)
    {
      t = a;
      a = b;
      b = t + b;
    }
  return a;
}
