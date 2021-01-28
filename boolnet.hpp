//--Random Boolean Network (N-K model)------------------------------------------------------------//
//--                                                                                              //
//--For the members of RBN we use the most common naming conventions found in literature (Aldana- //
//--Gonzales et al. (2003)). The methods are named in a somewhat self-explanatory manner. The     //
//--easiest way to start with this class is:                                                      //
//-- 1. initialize it with the desired parameters                                                 //
//-- 2. call create_all()                                                                         //
//-- 3. call evolve_state() to move on one step in time                                           //
//--Depending on the research problem one could also create everything individually. For some     //
//--problems it might be interesting to flip the value of a vertex, which can be done with calling//
//--change_sigma(int).                                                                            //
//------------------------------------------------------------------------------------------------//
#ifndef BOOLNET_HPP
#define BOOLNET_HPP

#include <vector>
#include <bitset>
#include <set>
#include <map>
#include <bits/stdc++.h> //unique
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <random>
#include <cmath>
#include <climits>
#include <chrono>
#include <algorithm>
#include "DEFINITIONS.hpp"

class RBN
{
public:
  RBN(unsigned int t_K=DEGREE, double t_p=0.5, double t_bias=0.5);
  RBN(std::vector<std::vector<int> > t_network, double t_K, double t_p=0.5, double t_bias=0.5);
  virtual ~RBN();
  //Functions to obtain information about the network
  unsigned int size() const;
  std::bitset<NODES> state() const;
  bool sigma(const int&) const;
  std::vector<int> pointing_at_sigma(const int&) const;
  //A new state can either be initialized at random or by making a copy
  //of an already existing one
  void initialize_state();
  void initialize_state(const double&);
  void initialize_state(const std::bitset<NODES>&);
  void create_network();
  void create_network(const int&);
  //Every vertex gets its own set of coupling functions, which are randomly initialized and 
  //the magnetisation of them can be handed as an argument
  virtual void create_coupling_functions();
  virtual void create_coupling_functions(const double&);
  virtual void initialize_all();
  //Flips a single sigma
  void change_sigma(); //randomly
  void change_sigma(const int&);
  //Flips sigmas until the distance reaches the given value compared to the system
  //before the call
  void change_until_distance_above(const double&);
  //The argument tells which vertex to look at, then we lookup the values of its ingoing vertices
  //and turn them into an index for where the value of the next time step can be found in the
  //coupling functions
  int function_table_index(const int&);
  //Applies the coupling functions to all nodes
  void evolve_state();
  //~ void save_configuration(std::string);
  //~ void load_configuration(std::string);
  
protected:
  std::vector<std::vector<int> > m_network;              //Incoming links of all vertices
  
  unsigned int m_N;  //Size of the network
  double m_K;  //Vertex degree
  double m_p;        //Bias for the coupling functions (1 = all true)
  double m_bias;     //Starting bias of the boolean variables (1 = all true)
  std::bitset<NODES> m_sigma;  //Vector with all boolean variables
  std::vector<std::bitset<FUNCTION_SPACE> > m_coupling_functions;  //Coupling functions
  std::string m_name;
};

class Distribution
{
  std::map<int, double> m_distribution;
public:
  Distribution();
  void add_to_distribution(int);
  Distribution& operator/=(const double);
  std::ostream& print(std::ostream&);
  friend std::ostream& operator<<(std::ostream&, Distribution&);
};

std::ostream& operator<<(std::ostream&, Distribution&);

//Some measurement functions
int hamming_distance(const std::bitset<NODES>&, const std::bitset<NODES>&);
double normalized_distance(const std::bitset<NODES>&, const std::bitset<NODES>&);
double normalized_overlap(const std::bitset<NODES>&, const std::bitset<NODES>&);

//Network creating functions
void make_lattice_dim2(const int&, const int&,
                       std::vector<std::vector<int> > &, const bool& periodic=true);

void make_random_network(const int&, const double&, std::vector<std::vector<int> > &);

#endif //BOOLNET_HPP
