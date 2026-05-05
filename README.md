<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=wave&color=gradient&customColorList=0,2,2,5,30&height=200&section=header&text=Logistics%20Route%20Optimizer&fontSize=42&fontColor=white&fontAlignY=42&fontAlign=50&desc=A*%20Search%20Engine%20for%20Last-Mile%20Logistics&descAlignY=62&descAlign=50&descSize=18&animation=fadeIn" alt="Header" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-2563EB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Algorithm-A*_Search-FF6F00?style=for-the-badge&logo=thealgorithms&logoColor=white" alt="A* Search" />
  <img src="https://img.shields.io/badge/Status-Production_Ready-059669?style=for-the-badge&logo=checkmarx&logoColor=white" alt="Production Ready" />
  <img src="https://img.shields.io/badge/License-MIT-8B5CF6?style=for-the-badge&logo=bookstack&logoColor=white" alt="MIT License" />
</p>

<p align="center">
  <h2>Intelligent route optimization for truck logistics — finding optimal delivery paths through complex transportation networks</h2>
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Inter&weight=600&size=24&duration=3000&pause=500&color=2563EB&center=true&vCenter=true&width=700&lines=A*+Search+Algorithm+Implementation;Traffic-Aware+Heuristic+Function;Graph-Based+Network+Topology;13+Distribution+Hubs+%7C+17+Routes;Optimal+Path+Guaranteed+Every+Time" alt="Typing animation" />
</p>

<br/>

<p align="center">
  <a href="https://github.com/MALULEKE-KS"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  <a href="https://za.linkedin.com/in/kurhula-success-maluleke-32153231a"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
  <a href="mailto:kurhula04s@gmail.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>
  <img src="https://komarev.com/ghpvc/?username=MALULEKE-KS&style=for-the-badge&color=2563EB&label=Views" alt="Profile views" />
</p>

---

<br/>

## About This Project

> *"Building practical digital systems that solve real-world challenges"*

This is an **AI-powered logistics route optimization system** built as part of my BSc Computer Science & Mathematics Artificial Intelligence module. The system implements the **A\* Search Algorithm** to find optimal delivery routes through the Mahikeng Local Municipality distribution network, reducing travel costs and improving delivery efficiency.

Where most route planners use basic shortest-path algorithms, this system reasons through informed search — using traffic-based heuristics to guide exploration toward the most promising routes first.

### System Architecture

| Phase | Focus |
| :--- | :--- |
| **1. Network Modeling** | Graph-based representation of 13 distribution hubs |
| **2. Heuristic Design** | Traffic-factor estimation for cost prediction |
| **3. Search Execution** | A* algorithm with priority queue optimization |
| **4. Route Delivery** | Optimal path reconstruction and simulation |

---

## Currently

| | |
| :--- | :--- |
| **Project** | Truck Logistics Route Optimizer — A* Search |
| **Module** | CMPG 313 — Artificial Intelligence |
| **Institution** | North-West University |
| **Built by** | [Maluleke Kurhula Success](https://github.com/MALULEKE-KS) |
| **Based in** | South Africa |
| **Core Tech** | Python · A* Algorithm · Graph Theory · Heuristics |

---

## How It Works

### The A* Search Algorithm
f(n) = g(n) + h(n)

Where:
g(n) = Actual distance traveled from start to node n
h(n) = Traffic factor heuristic (estimated cost to goal)
f(n) = Estimated total cost through node n

text

### Network Topology
┌──────────┐
│ Zeerust │
└────┬─────┘
│
┌──────────┴──────────┐
│ Groot Marico │
└─────────────────────┘
│
┌──────────┐ ┌───┴────┐ ┌──────────┐
│ Mmabatho │────│ Slurry │────│Bakerville│
└────┬─────┘ └───┬────┘ └────┬─────┘
│ │ │
┌────┴─────┐ ┌────┴─────┐ ┌───┴────────┐
│ Mahikeng │───│ Disaneng │ │Lichtenburg │
└────┬─────┘ └────┬─────┘ └────┬───────┘
│ │ │
┌────┴─────┐ ┌────┴─────┐ ┌───┴──────┐
│ Madibogo │───│Sannieshof│ │ Coligny │
└──────────┘ └────┬─────┘ └──────────┘
│
┌────┴────────┐
│Delareyville │
└─────────────┘

text

### Traffic Heuristics (to Coligny)

| Hub | Traffic Factor | Hub | Traffic Factor |
| :--- | :---: | :--- | :---: |
| Disaneng | 70 | Bakerville | 30 |
| Mahikeng | 50 | Lichtenburg | 20 |
| Mmabatho | 55 | **Coligny** | **0** |
| Slurry | 45 | Ottosdal | 25 |
| Zeerust | 65 | Sannieshof | 40 |
| Groot Marico | 75 | Delareyville | 55 |
| | | Madibogo | 60 |

---

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Git (for cloning)

### Installation

# Clone the repository
git clone https://github.com/MALULEKE-KS/logistics-route-optimizer.git
cd logistics-route-optimizer

# Run the route optimizer
python A_star_search.py
Expected Output
text
==================================================
TRUCK LOGISTICS - A* SEARCH ROUTE OPTIMIZATION
==================================================
Starting Point: Disaneng
Destination:    Coligny

✅ SEARCH COMPLETE
------------------------------
Optimal Path:   Disaneng → Mahikeng → Bakerville → Lichtenburg → Coligny
Total Distance: 110 km
------------------------------

🚛 Truck Journey Simulation
==============================
  📍 Now at: Disaneng
  📍 Now at: Mahikeng
  📍 Now at: Bakerville
  📍 Now at: Lichtenburg
  📍 Now at: Coligny

🎯 Destination Reached!
==================================================
Verification
Run the verification script to manually confirm the optimal path:

bash
python verify.py
Manual Distance Calculation
Segment	Distance
Disaneng → Mahikeng	25 km
Mahikeng → Bakerville	35 km
Bakerville → Lichtenburg	20 km
Lichtenburg → Coligny	30 km
Total	110 km ✅
Project Structure
text
logistics-route-optimizer/
│
├── A_star_search.py           # Main A* search implementation
├── A_star_search_testcase.py  # Truck simulation module
├── verify.py                  # Manual verification script
├── verification_output.png    # Program output screenshot
├── verify.PNG                 # Verification screenshot
└── README.md                  # Project documentation
Technical Details
Property	Value
Algorithm	A* Search (Informed Search)
Data Structure	Priority Queue (heapq)
Graph Type	Weighted Undirected
Heuristic	Traffic-based (Admissible)
Nodes	13 Distribution Hubs
Edges	17 Routes
Time Complexity	O(b^d)
Space Complexity	O(b^d)
Optimality	Guaranteed
Engineering Philosophy
Principle	Application
Informed Search	Traffic heuristics guide exploration
Optimality	A* guarantees shortest path
Modularity	Separate graph, weights, and heuristics
Verification	Manual calculation confirms results
Real-world Application	Practical logistics route planning
What I Can Build
This project demonstrates foundational AI skills applicable to:

Industry	Applications
Logistics	Route optimization, fleet management, delivery scheduling
Transportation	Traffic navigation, public transit routing
AI & ML	Search algorithms, heuristic design, optimization problems
Supply Chain	Warehouse routing, distribution planning
Game Development	Pathfinding, NPC movement
Robotics	Navigation, obstacle avoidance
Connect With Me
Portfolio	my-nextjs-portfolio.vercel.app
Email	kurhula04s@gmail.com
WhatsApp	wa.me/27640708649
LinkedIn	linkedin.com/in/kurhula-success-maluleke
GitHub	github.com/MALULEKE-KS
<p align="center"> <em>Built with precision — KSDRILL-SA</em> </p><p align="center"> <img src="https://capsule-render.vercel.app/api?type=wave&color=gradient&customColorList=0,2,2,5,30&height=100&section=footer" alt="Footer wave" /> </p> 
