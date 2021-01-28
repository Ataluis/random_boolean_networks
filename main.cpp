/*
  This is the main file of our simulation program. We do not have to make any changes here
  and should instead use the DEFINITIONS.hpp file for the options we want to use.
*/
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <string>
#include <bits/stdc++.h>
#include "boolnet.hpp"
#include "altnet.hpp"
#include "DEFINITIONS.hpp"
#include <algorithm>
#include <bitset>
#include <cstdlib>
#include <ctime>

using namespace std;

int main()
{
  //Just some variables that we need later in order to collect the data
  vector<int> timestep(PHASE_SPACE);
  vector<int> to_test;
  int length;
  int end;
  int current;
  int number_attractors;
  
  int num_frozen;
  int num_nonfrozen;
  int frozen_stable;
  int nonfrozen_stable;
  int frozen_unstable;
  int nonfrozen_unstable;
  map<int, vector<int> > in_degree;
  RBN KBN;
  
  bitset<NODES> frozen;
  bitset<NODES> state_before;
  
  vector<vector<int> > info;
  
  set<int> attractor_nodes;
  vector<int> nodes;
  vector<vector<int> > network;
  for(int i = 0; i < NODES; i++) nodes.push_back(i);
  for(int i = 0; i < NODES; i++) network.push_back(nodes);
  int basin_of_attraction;
  int garden_of_eden;
  
  Space space;
  
  //This is the loop in which we run the realizations
  for(int realizations = 0; realizations < REALIZATIONS; realizations++)
  {
    //We first initialize a random netork
    cout << realizations << endl;
    if(DEGREE_EQUALS_NODES)
    {
		//for K=N networks
	    KBN = RBN(network,DEGREE,p);
	    KBN.create_coupling_functions();
    }
    else if(DEGREE_IS_INTEGER)
    {
	    //for K is natural number:
	    KBN = RBN(DEGREE,p);    
	    KBN.create_network();
	    KBN.create_coupling_functions();
    }
    else
    {
        //for networks with float degree
	    network.clear();
	    make_random_network(NODES,DEGREE,network);
	    KBN = RBN(network,DEGREE,p);
	    KBN.create_coupling_functions();
	}

    //Now we simulate through the network phase space
    //and store for each state its upcoming state in 
    //the vector timestep
    for(int i = 0; i < PHASE_SPACE; i++)
    {
      KBN.initialize_state(bitset<NODES>(i));
      KBN.evolve_state();
      timestep[i] = (int)((KBN.state()).to_ulong());
      //~ timestep[i] = rand() % PHASE_SPACE;
    }
    
    //Creating the structure of the phase space which we then analyze
    space.create(timestep);
	  
    //We store the name of every attractor
    attractor_nodes.clear();
    for(auto node : space.node)
    {
      attractor_nodes.insert(node.end);
    }
    number_attractors = attractor_nodes.size();
    
    //The following loop cylces over all the found attractors
    for(auto node : attractor_nodes)
    {
      basin_of_attraction = 0;
      garden_of_eden = 0;
	    
      //Counting the basin of attraction and garden of eden states
      for(int omega = 0; omega < PHASE_SPACE; omega++)
      {
        if(node == space.node[omega].end)
        {
          basin_of_attraction++;
          if(space.node[omega].previous[0] == -1) garden_of_eden++;
        }
      }
      length = 1;
      current = node;
      end = node;
      state_before = bitset<NODES>(current);
      to_test.push_back(current);
	    
      //In this timestep we store which of the nodes of the cycle are frozen
      frozen.set();
      while(space.node[current].next != end)
      {
        current = space.node[current].next;
        length++;
        frozen &= (~(state_before^bitset<NODES>(current)));
        state_before = bitset<NODES>(current);
        to_test.push_back(current);
      }
      num_frozen = 0;
      num_nonfrozen = 0;
      for(int n = 0; n < NODES; n++)
      {
        if(frozen[n])
        {
          num_frozen++;
        }
        else
        {
          num_nonfrozen++;
        }
      }
	    
      //Now we look if a node flip leads to a change of attractors
      frozen_stable = 0;
      nonfrozen_stable = 0;
      frozen_unstable = 0;
      nonfrozen_unstable = 0;
      current = node;
      end = node;
      for(int s = 0; s < length; s++)
      {
        for(int n = 0; n < NODES; n++)
        {
          if(space.node[(unsigned int)(bitset<NODES>(to_test[s]).flip(n)).to_ulong()].end == space.node[to_test[s]].end)
          {
            if(frozen[n])
            {
              frozen_stable++;
            }
            else
            {
              nonfrozen_stable++;
            }
          }
          else
          {
            if(frozen[n])
            {
              frozen_unstable++;
            }
            else
            {
              nonfrozen_unstable++;
            }
          }
        }
      }
      //Finally we store the just collected information
      info.push_back(vector<int>{NODES, (int)round(DEGREE), number_attractors, length, num_frozen, frozen_stable, frozen_unstable, num_nonfrozen, nonfrozen_stable, nonfrozen_unstable, basin_of_attraction, garden_of_eden});
      to_test.clear();
    }
    space.destroy();
  }
  
  //In the end we store the collected data in a file
  ofstream data;
  data.open(FILE_NAME, ios::out);
  for(auto vec : info)
  {
    for(auto val : vec) data << val << " ";
    data << endl;
  }
  data.close();
  
  return 0;
}
