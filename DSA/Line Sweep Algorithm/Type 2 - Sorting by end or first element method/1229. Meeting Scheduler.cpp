// https://algo.monster/liteproblems/1229#editor
// we can use 1d differential but man , that was not great in this case, 


#include <algorithm>
#include <iostream>
#include <iterator>
#include <limits>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
std::vector<int> meeting_scheduler(std::vector<std::vector<int>>& slots1, std::vector<std::vector<int>>& slots2, int duration) {
    // WRITE YOUR BRILLIANT CODE HERE
    int i=0,j=0;
    // sort the emlemnts by first elemnts
    sort(slots1.begin(),slots1.end());
    sort(slots2.begin(),slots2.end());
    
    int m=slots1.size(),n=slots2.size();
    vector<int>result;
    while(i<m && j<n){
        // checking overlap of intervals
        int L = max(slots1[i][0],slots2[j][0]);
        int R = min(slots1[i][1],slots2[j][1]);
        if(duration <= R-L){
            result.push_back(L);
            result.push_back(L+duration);
            return result;
        }
        if(slots1[i][1] < slots2[j][1]){
            i++;
        }else{
            j++;
        }
    }
    return {};
}

template<typename T>
std::vector<T> get_words() {
    std::string line;
    std::getline(std::cin, line);
    std::istringstream ss{line};
    ss >> std::boolalpha;
    std::vector<T> v;
    std::copy(std::istream_iterator<T>{ss}, std::istream_iterator<T>{}, std::back_inserter(v));
    return v;
}

void ignore_line() {
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
}

template<typename T>
void put_words(const std::vector<T>& v) {
    if (!v.empty()) {
        std::copy(v.begin(), std::prev(v.end()), std::ostream_iterator<T>{std::cout, " "});
        std::cout << v.back();
    }
    std::cout << '\n';
}

int main() {
    int slots1_length;
    std::cin >> slots1_length;
    ignore_line();
    std::vector<std::vector<int>> slots1;
    for (int i = 0; i < slots1_length; i++) {
        slots1.emplace_back(get_words<int>());
    }
    int slots2_length;
    std::cin >> slots2_length;
    ignore_line();
    std::vector<std::vector<int>> slots2;
    for (int i = 0; i < slots2_length; i++) {
        slots2.emplace_back(get_words<int>());
    }
    int duration;
    std::cin >> duration;
    ignore_line();
    std::vector<int> res = meeting_scheduler(slots1, slots2, duration);
    put_words(res);
}
