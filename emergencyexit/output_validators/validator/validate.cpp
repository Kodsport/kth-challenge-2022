#include <vector>
#include <algorithm>
#include <map>
#include "validate.h"

using namespace std;

#define rep(i, a, b) for(int i = a; i < (b); ++i)
#define trav(a, x) for(auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef long double ld;

void TOUPPER(string &s){
    for (char& c : s) c = (char)toupper(c);
}

bool validate_row(string row, int len){
    if(sz(row) != len)return 0;
    for(auto c : row){
        if(c != 'U' && c != 'D' && c != 'R' && c != 'L' && c != '.')return 0;
    }
    return 1;
}

pii get_directions(char c){
    c = toupper(c);
    if(c == 'U')return {-1,0};
    if(c == 'D')return {1,0};
    if(c == 'R')return {0,1};
    if(c == 'L')return {0,-1};
    return {0,0};
}

void check_case(){
    int n,m;
    int k = 0;
    judge_in >> n >> m;
    vector<pii> person;
    vector<vector<bool> > grid(n, vector<bool>(m, 0));

    for(int c1 = 0; c1 < n; c1++){
        string s;
        judge_in >> s;
        for(int c2 = 0; c2 < m; c2++){
            grid[c1][c2] = (s[c2] == '#');
            if(s[c2] == 'P'){
                person.push_back({c1, c2});
            }
        }
    }
    k = sz(person);

    // Read length
    int judge_answer, author_answer;
    judge_ans >> judge_answer;
    if(!(author_out >> author_answer)){
        wrong_answer("Could not read first line of output");
    }
    if(author_answer == -1){
        if(judge_answer != -1){
            wrong_answer("Contestant wrote -1 but judge found a solution");
        }
        return;
    }
    if(author_answer > judge_answer){
        wrong_answer("Contestant did worse than judge (%d vs %d)", author_answer, judge_answer);
    }

    // Read instructions
    vector<string> ans;
    for(int c1 = 0; c1 < k; c1++){
        string row;
        if(!(author_out >> row)){
            wrong_answer("Could not read %d:th row", c1+1);
        }
        if(!validate_row(row, author_answer)){
            wrong_answer("Wrong format of %d:th row", c1+1);
        }
        ans.push_back(row);
    }

    // Make sure everyone gets out
    vector<bool> got_out(k, 0);
    for(int c1 = 0; c1 < author_answer; c1++){
        map<pii,int> position_to_person;
        for(int c2 = 0; c2 < k; c2++){
            if(got_out[c2]) {
                if (ans[c2][c1] != '.') {
                    wrong_answer("Person %d already exited but got %c instruction at time %d",
                                 c2+1, ans[c2][c1], c1+1);
                }
                continue;
            }
            pii dir = get_directions(ans[c2][c1]);
            person[c2].first += dir.first;
            person[c2].second += dir.second;
            if(person[c2].first < 0 || person[c2].first >= n || person[c2].second < 0 || person[c2].second >= m){
                got_out[c2] = 1;
                continue;
            }
            if(grid[person[c2].first][person[c2].second]){
                wrong_answer("Person %d walked into a wall at time %d", c2+1, c1+1);
            }
            if(position_to_person.find(person[c2]) != position_to_person.end()){
                int j = position_to_person[person[c2]];
                wrong_answer("Person %d walked into person %d at time %d", c2+1, j+1, c1+1);
            }
            position_to_person[person[c2]] = c2;
        }
    }
    for(int c1 = 0; c1 < k; c1++){
        if(!got_out[c1]){
            wrong_answer("Person %d didn't get out", c1+1);
        }
    }

    if(judge_answer == -1 || judge_answer > author_answer){
        judge_error("Contestant found answer that was better than judge");
    }
}

int main(int argc, char **argv) {
  init_io(argc, argv);
  check_case();

  /* Check for trailing output. */
  string trash;
  if (author_out >> trash) {
      wrong_answer("Trailing output\n");
  }

  accept();
  return 0;
}
