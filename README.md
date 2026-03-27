# Python-course-project

Project description: 
The project will take an existing piece of power systems analysis code and will attempt to implement the following.
    1.Transform existing code into Python library with proper tests  
    2.NumPy optimization for speed (vectorization, no loops)
    3.Improve documentation and performance benchmarks





# Library usage and installation
## Install
```bash
pip install -r requirements.txt
```

## Usage Example
```python
from pslib.network import *

net = create_test_network()
create_loads(net, 1, -0.006, -0.0029)
run_powerflow(net)
fig = plot_results(net)
```

## Tests
```bash
pytest tests/ -v  # 4/4 PASS
```