#include <vector>
#include <algorithm>
#include <map>
#include <set>
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

void TOLOWER(string &s){
    for (char& c : s) c = (char)tolower(c);
}

bool is_vowel(char c){
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

void check_case(){
    int n;
    judge_in >> n;

    set<string> names;

    for(int c1 = 0; c1 < n; c1++){
        string name;
        if(!(author_out >> name)){
            wrong_answer("Could not read %d:th line of output", c1+1);
        }

        // Just to be nice, letters should actually be lowercase
        TOLOWER(name);

        if(sz(name) < 3 || sz(name) > 20){
            wrong_answer("Name on line %d had invalid length %d", c1+1, sz(name));
        }
        trav(y, name){
            if(y-'a' < 0 || y-'a' >= 26){
                wrong_answer("Name on line %d contained invalid character", c1+1);
            }
        }
        for(int c1 = 0; c1 < sz(name)-2; c1++){
            if(is_vowel(name[c1]) && is_vowel(name[c1+1]) && is_vowel(name[c1+2])){
                wrong_answer("Name on line %d contained three vowels in a row", c1+1);
            }
            if(!is_vowel(name[c1]) && !is_vowel(name[c1+1]) && !is_vowel(name[c1+2])){
                wrong_answer("Name on line %d contained three consonants in a row", c1+1);
            }
        }
        names.insert(name);
    }
    if(sz(names) != n){
        wrong_answer("Duplicate names");
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