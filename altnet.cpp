#include "altnet.hpp"
int Node::counter = 0;
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
void Space::create(const std::vector<int>& timestep)
{
  node.clear();
  node.reserve(timestep.size());
  //First we give every State its unique value
  for(unsigned int i = 0; i < timestep.size(); i++)
  {
    Node n;
    n.id = i;
    node.push_back(n);
  }
  //Introducing the used variables
  int current_node;
  int previous_node = -1;
  int next_node;
  int end_node = 0;
  unsigned int current_lowest = 0;
  bool found_cycle;
  std::vector<int> this_loop;
  
  while(current_lowest < timestep.size())
  {
    this_loop.clear();
    found_cycle = false;
    current_node = current_lowest;
    node[current_node].visited = true;
    previous_node = -1;
    next_node = timestep[current_node];
    node[current_node].next = next_node;
    this_loop.push_back(current_node);
    while(!found_cycle)
    {
      if(node[next_node].next != -1)
      {
        found_cycle = true;
        if(node[next_node].previous[0] == -1)
        {
          node[next_node].previous[0] = current_node;
        }
        else
        {
          node[next_node].previous.push_back(current_node);
        }
      }
      else
      {
        previous_node = current_node;
        if(next_node != -1)
          current_node = next_node;
      }
      
      next_node = timestep[current_node];
      node[current_node].next = next_node;
      if(node[current_node].previous[0] == -1)
      {
        node[current_node].previous[0] = previous_node;
      }
      else
      {
        node[current_node].previous.push_back(previous_node);
      }
      node[current_node].visited = true;
      this_loop.push_back(current_node);
    }
    if(node[next_node].end == -1)
    {
      end_node = current_node;
      for(auto val : this_loop) node[val].end = end_node;
    }
    else
    {
      end_node = node[next_node].end;
      for(auto val : this_loop) node[val].end = end_node;
    }
    while(node[current_lowest].visited) current_lowest++;
  }
}

void Space::destroy()
{
  node.clear();
  Node::counter = 0;
}

inline bool operator<(const Node& left, const Node& right)
{
  return left.id < right.id;
}

inline bool operator==(const Node& left, const Node& right)
{
  return left.id == right.id;
}

//~ inline bool operator<(const Meta& left, const Meta& right)
//~ {
  //~ return left.end.to_ullong() < right.end.to_ullong();
//~ }

//~ inline bool operator==(const Meta& left, const Meta& right)
//~ {
  //~ if(left.end.size() == 0) return false;
  //~ return left.end == right.end;
//~ }
