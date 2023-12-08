#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
struct line {
  long dst;
  long src;
  long range;
};

long seeds[] = {4188359137, 37519573,   3736161691, 172346126,  2590035450,
                66446591,   209124047,  106578880,  1404892542, 30069991,
                3014689843, 117426545,  2169439765, 226325492,  1511958436,
                177344330,  1822605035, 51025110,   382778843,  823998526};

std::vector<std::string> split_string_by_newline(std::string &str) {
  auto result = std::vector<std::string>{};
  auto ss = std::stringstream{str};

  for (std::string line; std::getline(ss, line, '\n');)
    result.push_back(line);

  return result;
}
vector<long> splitLine(string l) {
  vector<long> ret;
  std::istringstream ss(l);
  string token;
  while (std::getline(ss, token, ',')) {
    ret.push_back(stol(token));
  }
  return ret;
}

int main(int argc, char *argv[]) {

  ifstream f("output.txt"); // taking file as inputstream
  // string str((istreambuf_iterator<char>(f)), istreambuf_iterator<char>());

  vector<vector<vector<long>>> dataString;
	dataString.reserve(7);
	string str;

  if (f) {
    ostringstream ss;
    ss << f.rdbuf(); // reading data
    str = ss.str();
  }

  vector<string> data = split_string_by_newline(str);
	vector<string>::iterator it = data.begin();

	for (int i = 0; i < 6; i++){
		for (;*it!="\n"; it++){
			dataString[i].push_back(splitLine(*it));
		}
	}
	cout<<dataString[0][0][1];
}
