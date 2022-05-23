#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

map<int, pair<int, int>> tree;

void dfs_pre(int start) {
    if (start != -1) {
        char ans = 'A' + start;
        cout << ans;
        dfs_pre(tree.find(start)->second.first);
        dfs_pre(tree.find(start)->second.second);
    }
}

void dfs_in(int start) {
    if (start != -1) {
        dfs_in(tree.find(start)->second.first);
        char ans = 'A' + start;
        cout << ans;
        dfs_in(tree.find(start)->second.second);
    }
}

void dfs_post(int start) {
    if (start != -1) {
        dfs_post(tree.find(start)->second.first);
        dfs_post(tree.find(start)->second.second);
        char ans = 'A' + start;
        cout << ans;
    }
}

int main() {
    int v;
    cin >> v;

    for (int i = 0; i < v; i++) {
        char root, left, right;
        int root_num, left_num, right_num;

        cin >> root >> left >> right;

        root_num = root - 'A';
        left_num = left - 'A';
        right_num = right - 'A';
        if (left == '.') left_num = -1;
        if (right == '.') right_num = -1;

        tree[root_num] = { left_num, right_num};
    }

    dfs_pre(0);
    cout << '\n';
    dfs_in(0);
    cout << '\n';
    dfs_post(0);
}#include <iostream>
 #include <vector>
 #include <map>
 #include <algorithm>

 using namespace std;

 map<int, pair<int, int>> tree;

 void dfs_pre(int start) {
     if (start != -1) {
         char ans = 'A' + start;
         cout << ans;
         dfs_pre(tree.find(start)->second.first);
         dfs_pre(tree.find(start)->second.second);
     }
 }

 void dfs_in(int start) {
     if (start != -1) {
         dfs_in(tree.find(start)->second.first);
         char ans = 'A' + start;
         cout << ans;
         dfs_in(tree.find(start)->second.second);
     }
 }

 void dfs_post(int start) {
     if (start != -1) {
         dfs_post(tree.find(start)->second.first);
         dfs_post(tree.find(start)->second.second);
         char ans = 'A' + start;
         cout << ans;
     }
 }

 int main() {
     int v;
     cin >> v;

     for (int i = 0; i < v; i++) {
         char root, left, right;
         int root_num, left_num, right_num;

         cin >> root >> left >> right;

         root_num = root - 'A';
         left_num = left - 'A';
         right_num = right - 'A';
         if (left == '.') left_num = -1;
         if (right == '.') right_num = -1;

         tree[root_num] = { left_num, right_num};
     }

     dfs_pre(0);
     cout << '\n';
     dfs_in(0);
     cout << '\n';
     dfs_post(0);
 }