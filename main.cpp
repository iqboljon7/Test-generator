#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> a(n);
    for(int &i: a)
        cin >> i;
    int ans = 0;
    sort(a.begin(),a.end());
    int k = a[n/2];
    for(int i = 0; i < n; i++)
        ans += min(a[i], abs(a[i] - k));
    cout << ans;
}