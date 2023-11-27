#define BOOST_TEST_MODULE static library test // Defines the name of the program which is used in the messages
#include <common.hpp>
#include <boost/test/unit_test.hpp>


using namespace std;

BOOST_AUTO_TEST_SUITE(MainSuite)

BOOST_AUTO_TEST_CASE(SampleTest)
{
    BOOST_TEST(true);
}


BOOST_AUTO_TEST_SUITE_END()