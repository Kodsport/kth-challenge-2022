#include <bits/stdc++.h>
using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const int MAXN = 201;

int DX[5] = {1,0,-1,0,0};
int DY[5] = {0,1,0,-1,0};
string dir = "DRUL.";
bool grid[MAXN][MAXN] = {0};
int nex[MAXN][MAXN] = {0};
int doorx, doory;
int n,m,k;
vector<pii> person;
int dist[MAXN][MAXN] = {0};
vi ind;

bool inbounds(int i, int j){
    return i >= 0 && j >= 0 && i < n && j < m;
}

bool comp(int i, int j){
    return dist[person[i].first][person[i].second] < dist[person[j].first][person[j].second];
}

void bfs(){
    rep(c1,0,n){
        rep(c2,0,m){
            dist[c1][c2] = -1;
        }
    }
    queue<pii> Q;
    Q.push({doorx, doory});
    dist[doorx][doory] = 1;
    rep(c1,0,4){
        int x = doorx+DX[c1];
        int y = doory+DY[c1];
        if(!inbounds(x,y))nex[doorx][doory] = c1;
    }
    while(!Q.empty()){
        pii p = Q.front();
        Q.pop();
        int x = p.first;
        int y = p.second;
        rep(c1,0,4){
            int x2 = x+DX[c1];
            int y2 = y+DY[c1];
            if(inbounds(x2,y2) && dist[x2][y2] == -1 && !grid[x2][y2]){
                nex[x2][y2] = (c1+2)%4;
                dist[x2][y2] = dist[x][y]+1;
                Q.push({x2,y2});
            }
        }
    }
}

int main() {
    int a,b;
    cin >> n >> m;
    k = 0;

    rep(c1,0,n){
        string row;
        cin >> row;
        rep(c2,0,m){
            if(row[c2] == '#'){
                grid[c1][c2] = 1;
            }
            if(row[c2] == 'P'){
                ind.push_back(k);
                k++;
                person.push_back({c1,c2});
            }
            if((c1 == 0 || c2 == 0 || c1 == n-1 || c2 == m-1) && !grid[c1][c2]){
                doorx = c1;
                doory = c2;
            }
        }
    }

    bfs();
    sort(all(ind), comp);
    vi D(k, 0);
    bool fail = 0;
    vector<set<int> > VS(n*m, set<int>());

    rep(c1,0,k){
        if(dist[person[c1].first][person[c1].second] == -1){
            fail = 1;
            break;
        }
        VS[dist[person[c1].first][person[c1].second]].insert(c1);
        D[c1] = dist[person[c1].first][person[c1].second];
    }

    if(fail){
        cout << "-1\n";
        return 0;
    }
    int tot = 0;
    rep(c1,0,n*m){
        while(sz(VS[c1]) > 1){
            int i = *(VS[c1].begin());
            VS[c1].erase(i);
            D[i]++;
            VS[c1+1].insert(i);
        }
    }
    rep(c1,0,k){
        tot = max(tot, D[c1]);
    }

    vector<string> ANS(k, "");

    rep(c1,0,k){
        int i = c1;
        int d = D[c1];
        int x = person[i].first;
        int y = person[i].second;
        rep(c2,0,d-dist[x][y]){
            ANS[i] += dir[4];
        }
        while(inbounds(x,y)){
            int j = nex[x][y];
            ANS[i] += dir[j];
            x += DX[j];
            y += DY[j];
        }
        while(sz(ANS[i]) < tot){
            ANS[i] += dir[4];
        }
    }
    cout << tot << "\n";
    rep(c1,0,k){
        cout << ANS[c1] << "\n";
    }

    return 0;
}
