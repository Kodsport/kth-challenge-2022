#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define per(i, b, a) for(int i = b - 1; i >= a; i--)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef long double ld;
typedef unsigned long long ull;

unsigned seed = chrono::system_clock::now().time_since_epoch().count();
mt19937 eng(seed);

ll random2(){
    return (1ll << 31ll)*eng()+eng();
}

ll n,m,k,q,T;

const ll big = 1000000007;
const ll big2 = 1000000009;
const ll mod =  998244353;

const int MAXN = 200006;

vector<vi> C(MAXN, vi());

int PAR[MAXN] = {0};
int leaves[MAXN] = {0};

void dfs1(int i, int par){
    PAR[i] = par;
    leaves[i] = (sz(C[i]) == 1);
    trav(y, C[i]){
        if(y != par){
            dfs1(y,i);
            leaves[i] += leaves[y];
        }
    }
}

int centroid = 0;
vector<pii> ANS;

vi get_leaves(int i, int par){
    vi res;
    if(sz(C[i]) == 1)return {i};
    trav(y, C[i]){
        if(y != par){
            vi temp = get_leaves(y, i);
            trav(v, temp){
                res.push_back(v);
            }
        }
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);

   // freopen("fhc.txt","r",stdin);
   // freopen("autput.txt","w",stdout);

    ll a,b,c,d,e;

    cin >> n;
    rep(c1,0,n-1){
        cin >> a >> b;
        a--;
        b--;
        C[a].push_back(b);
        C[b].push_back(a);
    }
    int root = 0;
    rep(c1,0,n){
        if(sz(C[c1]) > 1)root = c1;
    }
    dfs1(root,-1);
    int tot_leaves = leaves[root];

    int best = big;
    rep(c1,0,n){
        int temp = tot_leaves - leaves[c1];
        trav(y, C[c1]){
            if(y != PAR[c1]){
                temp = max(leaves[y], temp);
            }
        }
        if(temp < best && sz(C[c1]) != 1){
            best = temp;
            centroid = c1;
        }
    }

    vector<vi> L;
    priority_queue<pii> pq;
    trav(y, C[centroid]){
        vi temp = get_leaves(y, centroid);
        pq.push({sz(temp), sz(L)});
        L.push_back(temp);
    }

    while(sz(pq) >= 2){
        int i = pq.top().second;
        pq.pop();
        int j = pq.top().second;
        pq.pop();
        ANS.push_back({L[i].back(), L[j].back()});
        L[i].pop_back();
        L[j].pop_back();
        if(sz(L[i]) > 0)pq.push({sz(L[i]), i});
        if(sz(L[j]) > 0)pq.push({sz(L[j]), j});
    }

    if(sz(pq) > 0){
        int i = pq.top().second;
        pq.pop();

        while(sz(L[i]) > 0){
            ANS.push_back({L[i].back(), centroid});
            L[i].pop_back();
        }
    }

    cout << sz(ANS) << "\n";
    trav(p, ANS){
        cout << p.first+1 << " " << p.second+1 << "\n";
    }

    return 0;
}
