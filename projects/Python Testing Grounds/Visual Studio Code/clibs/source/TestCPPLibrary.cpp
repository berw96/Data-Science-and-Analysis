#define TestCPPLibrary _declspec(dllexport)

extern "C" {
	TestCPPLibrary int AddNumbers(int _a, int _b) {
		return _a + _b;
	}

	TestCPPLibrary int SubtractNumbers(int _a, int _b) {
		return _a - _b;
	}

	TestCPPLibrary int MultiplyNumbers(int _a, int _b) {
		return _a * _b;
	}

	TestCPPLibrary int DivideNumbers(int _numerator, int _denominator) {
		return _numerator / _denominator;
	}
}

