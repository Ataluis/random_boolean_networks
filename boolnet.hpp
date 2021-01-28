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

//--Topological Random Boolean Network------------------------------------------------------------//
//--                                                                                              //
//--Almost the same as RBN, but the structure of the Network has to be given to it as an argument.//
//--Since the degree is not any longer constant, we also store the information about them for each//
//--vertex in the field m_k.                                                                      //
//------------------------------------------------------------------------------------------------//
//~ class TRBN : public RBN
//~ {
//~ public:
  //~ TRBN(std::vector<std::vector<int> > t_network={}, double t_p=0.5, double t_bias=0.5);
  //~ ~TRBN();
  //~ double k_mean() const;
  //~ void create_coupling_functions();
  //~ void create_coupling_functions(const double&);
  //~ void initialize_all();
//~ private:
  //~ double m_k_mean;
  //~ std::vector<int> m_k;
//~ };

//--Attractor-------------------------------------------------------------------------------------//
//--                                                                                              //
//------------------------------------------------------------------------------------------------//
//~ class Attractor
//~ {
//~ protected:
  //~ std::vector<std::bitset<NODES> > m_path;
  //~ std::set<std::bitset<NODES> > m_elements;
  //~ std::set<std::bitset<NODES> > m_attractor;
  //~ bool m_found_attractor = false;
  //~ std::bitset<NODES> m_label;
//~ public:
  //~ Attractor();
  //~ ~Attractor();
  //~ void insert_path(const std::bitset<NODES>&);
  //~ void insert_element(const std::bitset<NODES>&);
  //~ bool has_attractor() const;
  //~ std::vector<std::bitset<NODES> > path() const;
  //~ std::set<std::bitset<NODES> > elements() const;
  //~ std::set<std::bitset<NODES> > attractor() const;
  //~ std::bitset<NODES> random_attractor_element() const;
  //~ std::bitset<NODES> label() const;
  //~ friend bool operator<(const Attractor&, const Attractor&);
  //~ friend bool operator==(const Attractor&, const Attractor&);
  //~ friend Attractor operator+(const Attractor&, const Attractor&);
//~ };

//~ std::ostream& operator<<(std::ostream&, Attractor&);

//~ inline bool operator<(const Attractor& left, const Attractor& right)
//~ {
  //~ if((left.attractor()).size() != (right.attractor()).size())
  //~ {
    //~ if((left.attractor()).size() < (right.attractor()).size())
    //~ {
      //~ return true;
    //~ }
    //~ return false;
  //~ }
  //~ else
  //~ {
    //~ return left.label().to_ullong() < right.label().to_ullong();
  //~ }
//~ }

//~ inline bool operator==(const Attractor& left, const Attractor& right)
//~ {
  //~ return *((left.attractor()).begin()) == *((right.attractor()).begin());
//~ }

//~ inline Attractor operator+(const Attractor& left, const Attractor& right)
//~ {
  //~ Attractor sum = left;
  //~ for(unsigned int i = 0; i < (right.path()).size() - (right.attractor()).size(); i++)
  //~ {
    //~ sum.insert_element((right.path())[i]);
  //~ }
  //~ return sum;
//~ }

//~ class BasinSortedAttractor : public Attractor
//~ {
//~ public: 
  //~ BasinSortedAttractor(){};
  //~ BasinSortedAttractor(Attractor& attractor) : Attractor(attractor) {};
//~ };

//~ inline bool operator<(const BasinSortedAttractor& left, const BasinSortedAttractor& right)
//~ {
  //~ if((left.elements()).size() != (right.elements()).size())
  //~ {
    //~ if((left.elements()).size() < (right.elements()).size())
    //~ {
      //~ return true;
    //~ }
    //~ return false;
  //~ }
  //~ else
  //~ {
    //~ return left.label().to_ullong() < right.label().to_ullong();
  //~ }
//~ }

//--Distribution----------------------------------------------------------------------------------//
//--                                                                                              //
//------------------------------------------------------------------------------------------------//
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

//Creating all possible bitset<NODES> in a set
//~ std::set<std::bitset<NODES> > all_initial_values(const int&);

//Some measurement functions
int hamming_distance(const std::bitset<NODES>&, const std::bitset<NODES>&);
double normalized_distance(const std::bitset<NODES>&, const std::bitset<NODES>&);
double normalized_overlap(const std::bitset<NODES>&, const std::bitset<NODES>&);

//Function to identify the frozen nodes in an attractor cycle
//~ std::bitset<NODES> identify_frozen_vertices(Attractor); 

//Network creating functions
void make_lattice_dim2(const int&, const int&,
                       std::vector<std::vector<int> > &, const bool& periodic=true);

void make_random_network(const int&, const double&, std::vector<std::vector<int> > &);

#endif //BOOLNET_HPP
