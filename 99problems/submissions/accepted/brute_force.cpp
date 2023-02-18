#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int MAXN = 10000;

int main() {
    int n;
    cin >> n;
    int diff = 101*MAXN;
    int ans = 0;
    for(int c1 = 1; c1 <= MAXN; c1++){
        if(c1 > 0 && c1%100 == 99){
            int d = abs(c1-n);
            if(d <= diff){
                diff = d;
                ans = c1;
            }
        }
    }
    cout << ans << "\n";

    return 0;
}
