#include <iostream>
#include <boost/filesystem.hpp>

int main() {
	boost::filesystem::path p(".");
	for (const auto &entry : boost::filesystem::directory_iterator(p))
	{
		std::cout << entry.path() << std::endl;
	}
	return 0;
}
