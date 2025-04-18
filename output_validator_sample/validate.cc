#include <utility>
#include <string>
#include <sstream>
#include <cassert>
#include <cstring>
#include <cmath>
#include <unistd.h>
#include <vector>
#include "validate.h"

using namespace std;

int main(int argc, char **argv) {
	init_io(argc, argv);

	int nruns;
	assert(judge_in >> nruns);
	
	string line;
	for (int i = 0; i < nruns; i++) {
		assert(judge_in >> line);
	}

	string guess;
	if (!(author_out >> guess)) {
		wrong_answer("testcase: Cannot parse team guess.\n");
	}
	string answer;
	if (!(judge_ans >> answer)) {
		wrong_answer("testcase: Cannot parse judge answer.\n");
	}

	if (guess != answer) {
		wrong_answer("testcase: Team guess: '%s' does not match judge answer: '%s'.\n", guess.c_str(), answer.c_str());
	}

	// Check for trailing output.
	string trash;
	if (author_out >> trash) {
		wrong_answer("Trailing output: '%s'\n", trash.c_str());
	}
	
	// Yay!
	accept();
}
