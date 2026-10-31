#include <iostream>
using namespace std;

// Create a C++ program to manage the scores of an IPL team
// 1. Create a Match class with team names, runs, wickets, and overs
// 2. Use a struct to store individual player scores
// 3. Use a 2D array to store scores of teams across matches

class Match {
    string team_name;
    int runs;
    int wickets;
    int overs;
};

struct Player {
    string name;
    int runs;
};

int main() {
    int[][] live_scores
}