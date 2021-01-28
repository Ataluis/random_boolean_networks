#ifndef ALTNET_HPP
#define ALTNET_HPP

#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <iostream>
#include "DEFINITIONS.hpp"

struct Node
{
  static int counter;
  bool visited;
  int id;
  const int dummy = -1;
  int next, end;
  std::vector<int> previous;
  Node() : visited(false), id(counter), next(dummy), end(dummy) {previous.push_back(dummy);counter++;};
  friend bool operator<(const Node&, const Node&);
  friend bool operator==(const Node&, const Node&);
};

//~ struct Meta
//~ {
  //~ std::bitset<NODES> end;
  //~ int length, basin, garden_of_eden_states;
  //~ Meta() : end({}), length(0), basin(0), garden_of_eden_states(0) {}
  //~ friend bool operator<(const Meta&, const Meta&);
  //~ friend bool operator==(const Meta&, const Meta&);
//~ };

struct Space
{
  std::vector<Node> node;//[PHASE_SPACE];
  //~ std::set<Meta> attractors;
  void create(const std::vector<int>&);
  void destroy();
};

#endif //ALTNET_HPP
