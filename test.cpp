#include<bits/stdc++.h>

using namespace std;

int main() {
    int dem = 0;
    int st = 0;
    for (int i = 1; i <= 4024; i++){
        st++;
        if(st == 3 && i % 3 == 0) dem++;
        if(st == 4) st = 0;
    }
    cout << dem;
}