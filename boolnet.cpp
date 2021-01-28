#include "boolnet.hpp"

//Initializing the Mersenne Twister for the creation of random numbers
#define MT_RAND_MAX (std::mt19937_64().max() - std::mt19937_64().min())
std::mt19937_64 mt_random(std::chrono::duration_cast< std::chrono::milliseconds >(
    std::chrono::system_clock::now().time_since_epoch()).count());

//RBN-----------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
RBN::RBN(unsigned int t_K, double t_p, double t_bias)
  : m_N(NODES), m_K(t_K), m_p(t_p), m_bias(t_bias)
{
  this->m_network.resize(this->m_N);
  std::stringstream tmp_name;
  tmp_name << "N" << this->m_N << "_"
           << "K" << this->m_K << "_"
           << std::fixed << std::setprecision(4)
           << "p" << this->m_p;           
  this->m_name = tmp_name.str();
}

RBN::RBN(std::vector<std::vector<int> > t_network, double t_K, double t_p, double t_bias)
  : m_network(t_network), m_N(NODES), m_K(t_K), m_p(t_p), m_bias(t_bias)
{
  std::stringstream tmp_name;
  tmp_name << "N" << this->m_N << "_"
           << "K" << this->m_K << "_"
           << std::fixed << std::setprecision(4)
           << "p" << this->m_p;           
  this->m_name = tmp_name.str();
}

RBN::~RBN()
{
  (this->m_network).clear();
  (this->m_coupling_functions).clear();
}

unsigned int RBN::size() const
{
  return this->m_N;
}

std::bitset<NODES> RBN::state() const
{
  return this->m_sigma;
}

bool RBN::sigma(const int& t_n) const
{
  return this->m_sigma[t_n];
}

std::vector<int> RBN::pointing_at_sigma(const int& t_n) const
{
  return this->m_network[t_n];
}

void RBN::initialize_state()
{
  this->initialize_state(this->m_bias);
}

void RBN::initialize_state(const double& t_bias)
{
  m_bias = t_bias;
  for(unsigned int it = 0; it < this->m_N; it++)
  {
    this->m_sigma[it] = ((this->m_bias > (mt_random()/(double)MT_RAND_MAX)) ? true : false);
  }
}

void RBN::initialize_state(const std::bitset<NODES>& t_sigma)
{
  this->m_sigma = t_sigma;
  this->m_N = (this->m_sigma).size();
}

void RBN::create_network()
{
  for(unsigned int it = 0; it < this->m_N; it++)
  {
    do
    {
      (this->m_network[it]).push_back((int)round((this->m_N-1)*(mt_random()/(double)MT_RAND_MAX)));
      std::sort((this->m_network[it]).begin(), (this->m_network[it]).end());
      (this->m_network[it]).erase(std::unique((this->m_network[it]).begin(), 
      (this->m_network[it]).end() ), (this->m_network[it]).end());
    }
    while((this->m_network[it]).size() < this->m_K);
  }
}

void RBN::create_network(const int& t_K)
{
  this->m_K = t_K;
  for(unsigned int it = 0; it < this->m_N; it++)
  {
    do
    {
      (this->m_network[it]).push_back((int)round((this->m_N-1)*(mt_random()/(double)MT_RAND_MAX)));
      (this->m_network[it]).erase(std::unique((this->m_network[it]).begin(), 
      (this->m_network[it]).end() ), (this->m_network[it]).end());
    }
    while((this->m_network[it]).size() < this->m_K);
  }
}

void RBN::create_coupling_functions()
{
  this->create_coupling_functions(this->m_p);
}

void RBN::create_coupling_functions(const double& t_p)
{
  unsigned int func_total = pow(2,this->m_K);
  (this->m_coupling_functions).resize(this->m_N);
  this->m_p = t_p;
  for(unsigned int it = 0; it < this->m_N; it++)
  {
    for(unsigned int is = 0; is < func_total; is++)
    {
      this->m_coupling_functions[it][is] = 
      (this->m_p < (mt_random()/(double)MT_RAND_MAX)) ? 1 : 0;
    }
  }
}

void RBN::initialize_all()
{
  this->create_network();
  this->create_coupling_functions();
  this->initialize_state();
}

void RBN::change_sigma()
{
  int rnd = (int)round((this->m_N-1)*(mt_random()/(double)MT_RAND_MAX));
  this->change_sigma(rnd);
}

void RBN::change_sigma(const int& t_n)
{
  this->m_sigma[t_n] = (!(this->m_sigma[t_n]));
}

void RBN::change_until_distance_above(const double& min_distance)
{
  std::bitset<NODES> temp_net = this->m_sigma;
  int rnd;
  do{
    rnd = (int)round((this->m_N-1)*(mt_random()/(double)MT_RAND_MAX));
    this->change_sigma(rnd);
  }while(normalized_distance(temp_net,this->m_sigma) < min_distance);
}

int RBN::function_table_index(const int& t_n)
{
  int k_temp = (this->m_network)[t_n].size();
  int index = 0;
  for(int it = 0; it < k_temp; it++)
  {
    index += pow(2,it)*(this->m_sigma[(this->m_network)[t_n][it]]);
  }
  return index;
}

void RBN::evolve_state()
{
  std::bitset<NODES> sigma = this->m_sigma;
  for(unsigned int it = 0; it < this->m_N; it++)
  {
    sigma[it] = (this->m_coupling_functions[it][this->function_table_index(it)]);
  }
  this->m_sigma = sigma;
}

//~ void RBN::save_configuration(std::string key)
//~ {
  //~ std::ofstream network;
  //~ std::string net = "data/configurations/" + this->m_name + key + ".network";
  //~ network.open(net.c_str());
  //~ for(unsigned int i = 0; i < (this->m_network).size(); i++)
  //~ {
    //~ for(unsigned int j = 0; j < (this->m_network)[i].size(); j++)
    //~ {
      //~ network << (this->m_network)[i][j] << " ";
    //~ }
    //~ network << std::endl;
  //~ }
  //~ network.close();
  //~ std::ofstream functions;
  //~ std::string func = "data/configurations/" + this->m_name + key + ".functions";
  //~ functions.open(func.c_str());
  //~ for(unsigned int i = 0; i < (this->m_coupling_functions).size(); i++)
  //~ {
    //~ for(unsigned int j = 0; j < (this->m_coupling_functions)[i].size(); j++)
    //~ {
      //~ functions << (this->m_coupling_functions)[i][j] << " ";
    //~ }
    //~ functions << std::endl;
  //~ }
  //~ functions.close();
//~ }

//~ void RBN::load_configuration(std::string key)
//~ {
  //~ (this->m_network).clear();
  //~ std::ifstream network;
  //~ std::string net = "data/configurations/" + this->m_name + key + ".network";
  //~ network.open(net.c_str());
  //~ std::string line;
  //~ while(std::getline(network, line))
  //~ {
    //~ std::vector<int>   net_lineData;
    //~ std::stringstream  net_lineStream(line);
    //~ int net_value;
    //~ while(net_lineStream >> net_value)
    //~ {
      //~ net_lineData.push_back(net_value);
    //~ }
    //~ (this->m_network).push_back(net_lineData);
  //~ }
  //~ network.close();
  //~ (this->m_coupling_functions).clear();
  //~ std::ifstream functions;
  //~ std::string func = "data/configurations/" + this->m_name + key + ".functions";
  //~ functions.open(func.c_str());
  //~ while(std::getline(functions, line))
  //~ {
    //~ std::bitset<NODES>   func_lineData;
    //~ std::stringstream  func_lineStream(line);
    //~ int func_value;
    //~ while(func_lineStream >> func_value)
    //~ {
      //~ func_lineData.push_back(func_value);
    //~ }
    //~ (this->m_coupling_functions).push_back(func_lineData);
  //~ }
//~ }

//TRBN----------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
//~ TRBN::TRBN(std::vector<std::vector<int> > t_network, double t_p, double t_bias)
//~ {
  //~ this->m_N = t_network.size();
  //~ (this->m_network).resize(this->m_N);
  //~ this->m_p = t_p;
  //~ this->m_bias = t_bias;
  //~ this->m_sigma.resize(this->m_N);
  //~ this->m_k_mean = 0.0;
  //~ (this->m_k).resize(this->m_N);
  //~ for(unsigned int it = 0; it < this->m_N; it++)
  //~ {
    //~ this->m_k[it] = t_network[it].size();
    //~ (this->m_network)[it].resize(this->m_k[it]);
    //~ (this->m_network)[it] = t_network[it];
    //~ this->m_k_mean += this->m_k[it];
  //~ }
  //~ this->m_k_mean /= (double)(this->m_N);
//~ }

//~ TRBN::~TRBN()
//~ {
  //~ (this->m_k).clear();
//~ }

//~ double TRBN::k_mean() const
//~ {
  //~ return this->m_k_mean;
//~ }

//~ void TRBN::create_coupling_functions()
//~ {
  //~ this->create_coupling_functions(this->m_p);
//~ }

//~ void TRBN::create_coupling_functions(const double& t_p)
//~ {
  
  //~ unsigned int func_total;
  //~ (this->m_coupling_functions).resize(this->m_N);
  //~ this->m_p = t_p;
  //~ for(unsigned int it = 0; it < this->m_N; it++)
  //~ {
    //~ func_total = pow(2,this->m_k[it]);
    //~ (this->m_coupling_functions)[it].resize(func_total);
    //~ for(unsigned int is = 0; is < func_total; is++)
    //~ {
      //~ this->m_coupling_functions[it][is] = 
      //~ (this->m_p < (mt_random()/(double)MT_RAND_MAX)) ? true : false;
    //~ }
  //~ }
//~ }

//~ void TRBN::initialize_all()
//~ {
  //~ this->create_network();
  //~ this->create_coupling_functions();
  //~ this->initialize_state();
//~ }

//Attractor-----------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
//~ Attractor::Attractor()
//~ {
  //~ m_found_attractor = false;
//~ }

//~ Attractor::~Attractor()
//~ {
  //~ this->m_found_attractor = false;
  //~ (this->m_path).resize(0);
  //~ (this->m_elements).clear();
  //~ (this->m_attractor).clear();
  //~ (this->m_label).clear();
//~ }

//~ void Attractor::insert_path(const std::bitset<NODES>& t_element)
//~ {
  //~ auto found_attractor = (this->m_elements).insert(t_element);
  //~ if(found_attractor.second)
  //~ {
    //~ (this->m_path).push_back(t_element);
  //~ }
  //~ else
  //~ {
    //~ std::vector<std::bitset<NODES> >::iterator it = std::find((this->m_path).begin(), 
    //~ (this->m_path).end(), t_element);
    //~ unsigned int index = std::distance((this->m_path).begin(), it);
    //~ for(unsigned int i = index; i < (this->m_path).size(); i++)
    //~ {
      //~ (this->m_attractor).emplace((this->m_path)[i]);
    //~ }
    //~ this->m_label = *((this->m_attractor).begin());
    //~ this->m_found_attractor = true;
  //~ }
//~ }

//~ void Attractor::insert_element(const std::bitset<NODES>& t_element)
//~ {
  //~ (this->m_elements).insert(t_element);
//~ }

//~ bool Attractor::has_attractor() const
//~ {
  //~ return this->m_found_attractor;
//~ }

//~ std::vector<std::bitset<NODES> > Attractor::path() const
//~ {
  //~ return this->m_path;
//~ }

//~ std::set<std::bitset<NODES> > Attractor::elements() const
//~ {
  //~ return this->m_elements;
//~ }

//~ std::set<std::bitset<NODES> > Attractor::attractor() const
//~ {
  //~ return this->m_attractor;
//~ }

//~ std::bitset<NODES> Attractor::random_attractor_element() const
//~ {
  //~ int rnd = (int)round(((this->m_attractor).size()-1)*(mt_random()/(double)MT_RAND_MAX));
  //~ std::set<std::bitset<NODES> >::iterator it;
  //~ it = (this->m_attractor).begin();
  //~ for(int n = 0; n < rnd; n++)
  //~ {
    //~ it++;
  //~ }
  //~ return *it;
//~ }

//~ std::bitset<NODES> Attractor::label() const
//~ {
  //~ return m_label;
//~ }

//~ //--Distribution------------------------------------------------------------------------------------
//~ //--------------------------------------------------------------------------------------------------
//~ //--------------------------------------------------------------------------------------------------
//~ Distribution::Distribution()
//~ {
  //~ (this->m_distribution)[0] = 0;
//~ }

//~ void Distribution::add_to_distribution(int NODES)
//~ {
  //~ if((this->m_distribution).count(NODES) > 0)
  //~ {
    //~ (this->m_distribution)[NODES] += 1.;
  //~ }
  //~ else
  //~ {
    //~ (this->m_distribution)[NODES] = 1.;
  //~ }
//~ }

//~ Distribution& Distribution::operator/=(const double divisor)
//~ {
  //~ std::map<int, double> new_distribution;
  //~ for(auto it = (this->m_distribution).begin(); it != (this->m_distribution).end(); ++it)
  //~ {
    //~ new_distribution[it->first] = (it->second)/divisor;
  //~ }
  //~ this->m_distribution = new_distribution;
  //~ return *this;
//~ }

//~ std::ostream& Distribution::print(std::ostream& os)
//~ {
  //~ for(auto it=(this->m_distribution).begin(); it!=(this->m_distribution).end(); ++it)
  //~ {
    //~ os << it->first << " " << it->second << std::endl;
  //~ }
  //~ return os;
//~ }

//~ std::ostream& operator<<(std::ostream& os, Distribution& distribution)
//~ {
  //~ return distribution.print(os);
//~ }
//Initaial values function--------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
//~ std::set<std::bitset<NODES> > all_initial_values(const int& N)
//~ {
  //~ unsigned long long int num_states = pow(2,N);
  //~ std::set<std::bitset<NODES> > initial_values;
  //~ for(unsigned long long int i = 0; i < num_states; i++)
  //~ {
    //~ std::bitset<NODES> initial(N,false);
    //~ unsigned long long int temp = i;
    //~ for(int n = N-1; n >= 0; n--)
    //~ {
      //~ if(temp >= pow(2,n))
      //~ {
        //~ initial[n] = true;
        //~ temp -= pow(2,n);
      //~ }
    //~ }
    //~ initial_values.insert(initial);
    //~ initial.clear();
  //~ }
  //~ return initial_values;
//~ }

//Some measurement functions------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
int hamming_distance(const std::bitset<NODES>& net1,const std::bitset<NODES>& net2)
{
  int distance = 0;
  if(net1.size() == net2.size())
  {
    unsigned int net_size = net1.size();
    for(unsigned int it = 0; it < net_size; it++)
    {
      distance += (int)(net1[it]^net2[it]);
    }
  }else{
    std::cout << "Measurement failure: diffeerent network sizes!"
    << std::endl;
  }
  return distance;
}

double normalized_distance(const std::bitset<NODES>& net1,const std::bitset<NODES>& net2)
{
  double distance = (double)hamming_distance(net1,net2);
  return distance/net1.size();
}

double normalized_overlap(const std::bitset<NODES>& net1,const std::bitset<NODES>& net2)
{
  return 1.0 - (double)normalized_distance(net1,net2);
}

//function for identifying the frozen part of an attractor cycle------------------------------------
//--------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
//~ std::bitset<NODES> identify_frozen_vertices(Attractor Att)
//~ {
  //~ std::set<std::bitset<NODES> > temp = Att.attractor();
  //~ std::vector<std::bitset<NODES> > attractor(temp.size());
  //~ std::copy(temp.begin(), temp.end(), attractor.begin());
  //~ std::bitset<NODES> frozen_vertices(attractor[0].size(),true);
  //~ for(unsigned int i = 0; i < attractor.size() - 1; i++)
  //~ {
    //~ for(unsigned int j = 0; j < attractor[0].size(); j++)
    //~ {
      //~ if(attractor[i][j] != attractor[i+1][j]) frozen_vertices[j] = false;
    //~ }
  //~ }
  //~ return frozen_vertices;
//~ }

//Network creating functions------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
//--------------------------------------------------------------------------------------------------
void make_lattice_dim2(const int& Nx,const int& Ny,
                       std::vector<std::vector<int> > &lattice,const bool& periodic)
{
  lattice.resize(Nx*Ny);
  int it = 0;
  int up, right, down, left;
  if(periodic)
  {
    for(int i = 0; i < Nx; i++)
    {
      for(int j = 0; j < Ny; j++)
      {
        it = i*Ny + j;
        left = ((i  )%Nx)*Ny + (Ny+j-1)%Ny;
        lattice[it].push_back(left);
        up = ((i+1)%Nx)*Ny + (j  )%Ny;
        lattice[it].push_back(up);
        right = ((i  )%Nx)*Ny + (j+1)%Ny;
        lattice[it].push_back(right);
        down = ((Nx+i-1)%Nx)*Ny + (j  )%Ny;
        lattice[it].push_back(down);
      }
    }
  }else{
    for(int i = 0; i < Nx; i++)
    {
      for(int j = 0; j < Ny; j++)
      {
        it = i*Ny + j;
        if(it%Nx != 0)
        {
          left = ((i  )%Nx)*Ny + (j-1)%Ny;
          lattice[it].push_back(left);
        }
        if(it < Nx*(Ny-1))
        {
          up = ((i+1)%Nx)*Ny + (j  )%Ny;
          lattice[it].push_back(up);
        }
        if(it%Nx != Nx-1)
        {
          right = ((i  )%Nx)*Ny + (j+1)%Ny;
          lattice[it].push_back(right);
        }
        if(it >= Nx)
        {
          down = ((Nx+i-1)%Nx)*Ny + (j  )%Ny;
          lattice[it].push_back(down);
        }
      }
    }
  }
}

void make_random_network(const int& N, const double& K, 
                         std::vector<std::vector<int> > &lattice)
{
  lattice.resize(N);
  double NK = N*K;
  int vertex_in, vertex_out;
  int total_num_edges = std::floor(NK);
  unsigned int size_in;
  double rnd_num = mt_random()/(double)MT_RAND_MAX;
  if((total_num_edges+rnd_num) < NK) total_num_edges++;
    for(int edge = 0; edge < N; edge++)
  {
    vertex_in = edge;
    vertex_out = std::round(((double)(N-1))*mt_random()/(double)MT_RAND_MAX);
    size_in = (lattice[vertex_in]).size();
    (lattice[vertex_in]).push_back(vertex_out);
    std::sort((lattice[vertex_in]).begin(), (lattice[vertex_in]).end());
    (lattice[vertex_in]).erase(std::unique((lattice[vertex_in]).begin(), 
    (lattice[vertex_in]).end() ), (lattice[vertex_in]).end());
    if(size_in == (lattice[vertex_in]).size()) edge--;
  }
  for(int edge = N; edge < total_num_edges; edge++)
  {
    vertex_in = std::round(((double)(N-1))*mt_random()/(double)MT_RAND_MAX);
    vertex_out = std::round(((double)(N-1))*mt_random()/(double)MT_RAND_MAX);
    size_in = (lattice[vertex_in]).size();
    (lattice[vertex_in]).push_back(vertex_out);
    std::sort((lattice[vertex_in]).begin(), (lattice[vertex_in]).end());
    (lattice[vertex_in]).erase(std::unique((lattice[vertex_in]).begin(), 
    (lattice[vertex_in]).end() ), (lattice[vertex_in]).end());
    if(size_in == (lattice[vertex_in]).size()) edge--;
  }
}

