# One-Dimensional Transient Conduction
#### Video Demo:  <https://youtu.be/fLlW8CdSClo>
#### Description: It is the simulation of a conduction problem in an isolated bar, whose ends are submitted to temperatures of the user's choice, starting from an initial condition also chosen. The system is considered a one-dimensional transient conduction, whose equation is delT/delt = alpha*del2T/delx2, which must be discretized and subjected to the following conditions:
#### 
#### Initial condition: Temperature = u0 at time = 0 and 0 < x < length
#### Boundary condition 1: Temperature = ul at x = 0 and time > 0
#### Boundary condition 2: Temperature = ur at x = length and time > 0
#### 
#### They are two Dirichlet-type boundary conditions and for this project it is only possible to change their values, not the type of boundary condition.
#### The execution is direct by the IDE button or by the python project.py command.
#### The program prompts the user for the following values, but suggests default values ​​that can be selected just by clicking ENTER.
#### 
#### Simulation time [Enter for 1000]:
#### Bar length [Enter for 100]:
#### Thermal diffusivity alpha [Enter for 1]:
#### Initial temperature (°C) [Enter for 25]:
#### Left temperature (°C) [Enter for 100]:
#### Right temperature (°C) [Enter for 0]:
#### Number of nodes in the bar [Enter for 200]:
#### 
#### The number of nodes in time is not required because is automaticaly calculated by the positivity criterion.
#### 
#### Requirements:
#### pip install numpy
#### pip install matplotlib
#### 
#### CS50 codespace is not showing matplotlib plot as easy to see working locally in VS Code or PyCharm.
