#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int n;
vector<vector<int>> adj;
vector<int> par;
vector<int> sz;
vector<ll> sdforw;
vector<ll> sdbackw;
vector<ll> sd;

inline int Sz(int u, int p = -1) {
    if (p == -1) return n;
    if (p == par[u]) return sz[u];
    return n - sz[p];
}


ll sumdist(int u, int p = -1) {
    ll &res = (p > 0 ? p == par[u] ? sdforw[u] : sdbackw[p] : sd[u]);
    if (res == 0) {
        res = Sz(u, p);
        for (int v: adj[u])
            if (v != p)
                res += sumdist(v, u);
    }
    return res - 1;
}
        
void forw(int u, int p = -1) {
    par[u] = p;
    sz[u] = 1;
    for (int &v: adj[u])
        if (v != p) {
            forw(v, u);
            sz[u] += sz[v];
        }
}

int main(void) {
    scanf("%d", &n);
    adj.resize(n+1);
    for (int i = 0; i < n-1; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    par.resize(n+1);
    sz.resize(n+1);
    sdforw.resize(n+1);
    sdbackw.resize(n+1);
    sd.resize(n+1);

    forw(1, -1);
    ll opt = -1;
    vector<int> optrooms;
    for (int i = 1; i <= n; ++i) {
        if (adj[i].size() > 1) continue;
        ll x = sumdist(i, -1);
        if (x > opt) {
            optrooms.clear();
            opt = x;
        }
        if (x == opt) {
            optrooms.push_back(i);
        }
    }
    printf("%d\n", optrooms.size());
    for (int u: optrooms)
        printf("%d\n", u);
}
