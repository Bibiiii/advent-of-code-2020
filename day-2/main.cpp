// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

// read_file reads from specified file
// Takes filename as argument
// Returns vector of each line
vector<string> read_file(const string &filename) {
    vector<string> passwords;
    string line;
    ifstream myfile ("passwords.txt");

    if (myfile.is_open()) {
        while (getline(myfile, line)) {
            passwords.push_back(line);
        }
    }
    else cout << "Unable to open file"; 
    return passwords;
}

// parse_line gets the required values from each password line
// Returns a tuple of the relevant parts
tuple<string, char, uint32_t, uint32_t> parse_line(const string &line) {
    string pwrd;
    char restriction;
    string min;
    string max;

    uint32_t delimiter = line.find('-');
    min = line.substr(0, delimiter);
    max = line.substr(delimiter + 1, line.find(" ") - 2);

    uint32_t delim = line.find(':');
    restriction = line.substr(delim - 1, delim)[0];

    pwrd = line.substr(delim + 2, line.size() - 1);

    // cout << "\nMin: " + min + ", Max: " + max + ", Restriction: " + restriction + ", Password: " + pwrd + "\n";

    return make_tuple(pwrd, restriction, stoi(min), stoi(max));
}

// find_valid_passwords returns number of valid passwords
// Takes password vector
int find_valid_passwords (const vector<string> &passwords) {
    uint32_t valid_passwords = 0;
    for (const string &line : passwords) {
        auto [password, restriction, min, max] = parse_line(line);
        uint32_t n = count(password.begin(), password.end(), restriction);
        if (n >= min && n <= max) {
            valid_passwords++;
        }
    }
    return valid_passwords;
}

int find_valid_passwords_2 (const vector<string> &passwords) {
    uint32_t valid_passwords = 0;
    for (const string &line : passwords) {
        auto [password, restriction, min, max] = parse_line(line);

        bool firstnotlast = (password[min - 1] == restriction) && (password[max - 1] != restriction);
        bool lastnotfirst = (password[min - 1] != restriction) && (password[max - 1] == restriction);

        if (firstnotlast || lastnotfirst) {
            valid_passwords++;
        }
    }
    return valid_passwords;
}

int main () {
    vector<string> passwords = read_file("passwords.txt");
    uint32_t valid = find_valid_passwords(passwords);
    uint32_t valid2 = find_valid_passwords_2(passwords);
    cout << "valid passwords: " << valid << endl;
    cout << "valid passwords 2: " << valid2 << endl;
    return 0;
}