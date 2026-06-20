# AI Algorithms Implementation - Prerona Kashyap

This project contains implementations of fundamental AI algorithms and games, including Alpha-Beta Pruning visualization, Hidden Markov Model (Viterbi algorithm), and an interactive Tic-Tac-Toe game with AI.

## Project Overview

The project consists of three main Python modules demonstrating key concepts in artificial intelligence:

### 1. **Alpha-Beta Pruning** (`alpha_beta_prunning.py`)
An implementation of the Alpha-Beta pruning algorithm with game tree visualization. This algorithm optimizes the minimax algorithm by eliminating branches that don't need to be evaluated.

**Features:**
- Builds game tree structures
- Visualizes the pruning process using Graphviz
- Generates visual output showing which branches were pruned
- Tracks alpha and beta values during execution

### 2. **Hidden Markov Model - Viterbi Algorithm** (`hmm_viterbi.py`)
Implementation of the Viterbi algorithm for finding the most likely sequence of hidden states in a Hidden Markov Model.

**Features:**
- Solves the decoding problem in HMMs
- Computes optimal hidden state sequences
- Visualizes probability matrices using matplotlib
- Supports custom transition and emission probabilities

### 3. **Tic-Tac-Toe with AI** (`tic_tac_toe.py`)
An interactive Tic-Tac-Toe game where you can play against an AI opponent powered by the Minimax algorithm.

**Features:**
- Human vs AI gameplay
- AI uses minimax with alpha-beta pruning
- Interactive command-line interface
- Tracks game state and win conditions

## Requirements

Before running the project, ensure you have Python 3.6+ installed.

### Dependencies

All required Python packages are listed in `requirements.txt`:
- **contourpy** (1.3.3) - Required for matplotlib
- **cycler** - Required for matplotlib
- **graphviz** - For generating game tree visualizations
- **kiwisolver** - Required for matplotlib
- **matplotlib** - For plotting and visualization
- **numpy** - For numerical computations in Viterbi algorithm
- **packaging** - Dependency management
- **Pillow** - Image processing library
- **pyparsing** - Parsing utilities

## Installation Instructions

### Step 1: Install Python Packages

Navigate to the project directory and install all required Python dependencies:

```bash
pip install -r requirements.txt
```

### Step 2: Install Graphviz (Important for Windows!)

**⚠️ IMPORTANT FOR WINDOWS USERS:**

For the Alpha-Beta pruning visualization to work properly on Windows, you must install Graphviz separately (it's not included in pip).

#### Windows Installation:

1. Download the Graphviz installer from: https://graphviz.org/download/
2. Choose the **Windows** version (msi installer)
3. Run the installer and follow the installation wizard
4. **Important:** During installation, check the option to add Graphviz to your system PATH
5. Alternatively, if you didn't add it to PATH during installation, you can add it manually:
   - Default installation path: `C:\Program Files\Graphviz\bin`
   - Add this path to your system environment variables

#### Verify Installation:

After installation, verify that Graphviz is properly installed by running:

```bash
dot -V
```

You should see the version number of Graphviz.

#### Uncomment Graphviz Path (if needed):

If you installed Graphviz in a non-standard location, edit `alpha_beta_prunning.py` and uncomment/adjust these lines:

```python
# import os
# os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'
```

### Step 3: Verify Installation

Run a simple test to ensure everything is working:

```bash
python alpha_beta_prunning.py
```

If a `.pdf` or `.svg` file is generated, your setup is successful!

## How to Run Each Module

### Alpha-Beta Pruning

Run the Alpha-Beta pruning algorithm with game tree visualization:

```bash
python alpha_beta_prunning.py
```

**Output:**
- Generates a visual representation of the game tree
- Shows which branches were pruned
- Creates output file (PDF, SVG, or PNG format) based on Graphviz rendering
- Displays final evaluation values and pruning statistics

### Hidden Markov Model - Viterbi Algorithm

Execute the Viterbi algorithm for HMM:

```bash
python hmm_viterbi.py
```

**Output:**
- Displays the most likely hidden state sequence
- Shows the Viterbi probability matrix
- Generates visualization plots using matplotlib
- Outputs transition path tracking information

### Tic-Tac-Toe Game

Play Tic-Tac-Toe against the AI:

```bash
python tic_tac_toe.py
```

**How to Play:**
- The board is represented as a 3x3 grid
- Enter your move as a position (0-8) when prompted
- Board positions:
  ```
  0 | 1 | 2
  ---------
  3 | 4 | 5
  ---------
  6 | 7 | 8
  ```
- You play as 'O', the AI plays as 'X'
- The AI uses the minimax algorithm to determine optimal moves
- The game ends when someone wins or the board is full

## Troubleshooting

### "graphviz" module not found
**Solution:** Run `pip install graphviz`

### "Graphviz executable not found"
**Solution:** This means Graphviz is not installed on your system. Follow the installation steps above for your operating system.

### Visualization files not generated
**Solution:** Ensure Graphviz is properly installed and added to your system PATH. Restart your terminal/IDE after installing Graphviz.

### Import errors for numpy, matplotlib, or contourpy
**Solution:** Reinstall all dependencies: `pip install -r requirements.txt`

## Project Structure

```
AI Assignment/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── alpha_beta_prunning.py   # Alpha-Beta pruning with visualization
├── hmm_viterbi.py           # Viterbi algorithm implementation
├── tic_tac_toe.py           # Tic-Tac-Toe game with AI
└── .gitignore              # Git ignore rules
```

## Technical Details

### Alpha-Beta Pruning Algorithm
- **Time Complexity:** O(b^(d/2)) in best case, O(b^d) in worst case
- **Space Complexity:** O(d) where d is tree depth
- **Use Case:** Game tree searching, AI decision-making

### Viterbi Algorithm
- **Time Complexity:** O(N² × T) where N is number of states, T is sequence length
- **Space Complexity:** O(N × T)
- **Use Case:** Speech recognition, DNA sequencing, hidden state inference

### Minimax Algorithm (Tic-Tac-Toe)
- **Implementation:** Recursive search with game state evaluation
- **Optimization:** Alpha-Beta pruning for efficiency
- **Strategy:** AI plays optimally to never lose

## Notes

- Windows users must follow the Graphviz installation steps for full functionality

