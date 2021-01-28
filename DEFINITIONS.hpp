#ifndef DEFINITIONS_HPP
#define DEFINITIONS_HPP
#include <cmath>

//Values to work with
#define NODES 4
#define DEGREE 2
#define DEGREE_EQUALS_NODES false // N = K ?
#define DEGREE_IS_INTEGER true    // 2 is not 2.0 and not integer would be 2.5
#define p 0.5
#define REALIZATIONS 1000000
#define FILE_NAME "master/basin_of_attraction_master_N4_K_2.dat"

//Do not change these values
#define PHASE_SPACE (1<<NODES)
#define FUNCTION_SPACE (1<<(int)std::ceil(DEGREE))

#endif //DEFINITIONS_HPP
