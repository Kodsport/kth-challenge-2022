#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int MAXN = 1001;

int n;
bool grid[MAXN][MAXN] = {0};
int row[MAXN] = {0};
int col[MAXN] = {0};

int main() {
    cin >> n;
    int ones = 0;
    rep(c1,0,n){
        string s;
        cin >> s;
        rep(c2,0,n){
            grid[c1][c2] = (s[c2] == '1');
            ones += grid[c1][c2];
            row[c1] += grid[c1][c2];
            col[c2] += grid[c1][c2];
        }
    }
    string ans = "X";
    rep(c1,0,n){
        if(2*row[c1] >= ones)ans = "-";
    }
    rep(c1,0,n){
        if(2*col[c1] >= ones){
            if(ans == "-"){
                ans = "+";
            }
            else{
                ans = "|";
            }
            break;
        }
    }
    assert(ans != "X");
    cout << ans << "\n";


    return 0;
}
