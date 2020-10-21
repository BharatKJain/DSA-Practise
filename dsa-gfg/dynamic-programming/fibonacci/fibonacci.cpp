#include<iostream>
using namespace std;
//Using recursion
int fibonacci(int n)
{
    if(n==0 || n==1)
        return 1;
    return(fibonacci(n-1)+fibonacci(n-2));
}
//Using top-down DP with recursion and memorization
int topdowndp(int n, int *dp)
{
    if (n==0||n==1)
    {
        dp[n]=1;
        return 1;
    }
    if (dp[n]!=-1)
    {
        return dp[n];
    }
    else{
        dp[n]=topdowndp(n-1,dp)+topdowndp(n-2,dp);
        return dp[n];
    }
}
//Using Bottom-Up approach 
/* 
Basically in bottom up approach we use iterative method i.e. using loop from 0 1 1 2 3 4 5 8 ..... from left to right storing 
the previous data in an array
 */
int btupfibo(int n)
{
    int *dp=new int[n+1];
    dp[0]=1;
    dp[1]=1;
    for (int i =2;i<=n;i++)
    {
        dp[i]=dp[i-1]+dp[i-2];
    }   
    return dp[n];
}
int main()
{
    int dp[100];
    for(int i=0;i<100;i++)
    {
        dp[i]=-1;
    }
    cout<<topdowndp(10,dp)<<endl;
    cout<<btupfibo(10)<<endl;
    cout<<fibonacci(10);
    return 0;
}