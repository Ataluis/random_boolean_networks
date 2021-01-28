/*
   This header contains the classes which we will use in order to analyse the structure 
   of the phase space. We decided to separate it from the random boolean network part,
   since it can principally be used for other models with a finitely large discrete
   phase space.
*/
#ifndef ALTNET_HPP
#define ALTNET_HPP

#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <iostream>
#include "DEFINITIONS.hpp"

// The node structure is similar to that of a tree leaf (graph)
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

// A space object uses the Node class in order to generate the structure of the phase space
struct Space
{
  std::vector<Node> node;
  void create(const std::vector<int>&);
  void destroy();
};

#endif //ALTNET_HPP
