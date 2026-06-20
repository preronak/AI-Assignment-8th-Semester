import numpy as np
import matplotlib.pyplot as plt

def viterbi(obs_seq, states, start_p, trans_p, emit_p):
    """
    Executes the Viterbi algorithm to find the most likely sequence of hidden states.
    
    Parameters:
    obs_seq (list): Sequence of integer indices representing observations.
    states (list): List of hidden state names.
    start_p (numpy.ndarray): Initial state probabilities.
    trans_p (numpy.ndarray): State transition probabilities.
    emit_p (numpy.ndarray): Observation emission probabilities.
    
    Returns:
    tuple: (Optimal hidden state sequence, Probability matrix for visualization)
    """
    num_states = len(states)
    num_obs = len(obs_seq)
    
    # Initialize the probability matrix (V) and the path tracker (P)
    # V tracks the maximum probability of reaching state i at time t
    viterbi_matrix = np.zeros((num_states, num_obs))
    # P tracks the state transition that resulted in the maximum probability
    path_tracker = np.zeros((num_states, num_obs), dtype=int)
    
    # Base Case: Initialize the first column for time t=0
    first_obs = obs_seq[0]
    viterbi_matrix[:, 0] = start_p * emit_p[:, first_obs]
    
    # Recursive Step: Compute probabilities for time t > 0
    for t in range(1, num_obs):
        current_obs = obs_seq[t]
        for current_state in range(num_states):
            # Calculate probabilities of transitioning from all previous states to the current state
            transition_probs = viterbi_matrix[:, t-1] * trans_p[:, current_state] * emit_p[current_state, current_obs]
            
            # Store the maximum probability and the state index that provided it
            viterbi_matrix[current_state, t] = np.max(transition_probs)
            path_tracker[current_state, t] = np.argmax(transition_probs)
            
    # Backtracking: Find the optimal path starting from the last time step
    best_path = np.zeros(num_obs, dtype=int)
    best_path[-1] = np.argmax(viterbi_matrix[:, -1])
    
    for t in range(num_obs - 2, -1, -1):
        best_path[t] = path_tracker[best_path[t+1], t+1]
        
    # Convert state indices back to string labels
    optimal_state_sequence = [states[i] for i in best_path]
    
    return optimal_state_sequence, viterbi_matrix

def visualize_probabilities(viterbi_matrix, states, observations, obs_labels):
    """
    Generates a line plot showing the probability of each hidden state at each time step.
    """
    time_steps = range(len(observations))
    
    plt.figure(figsize=(10, 6))
    
    # Plot a line for each hidden state
    for i, state in enumerate(states):
        plt.plot(time_steps, viterbi_matrix[i, :], marker='o', label=state)
        
    plt.title('HMM State Probabilities Over Time (Viterbi Algorithm)')
    plt.xlabel('Time Step (Observation)')
    plt.ylabel('Probability')
    plt.xticks(time_steps, [f"T{t}\n({obs_labels[obs]})" for t, obs in enumerate(observations)])
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Save the plot to the local directory
    output_filename = 'hmm_probability_plot.png'
    plt.savefig(output_filename)
    print(f"\nGraphical visualization saved as: {output_filename}")
    plt.close()

def main():
    # 1. Define the parameters of the model
    hidden_states = ['Sunny', 'Rainy']
    observable_events = ['Walk', 'Shop', 'Clean']
    
    # Initial probabilities: 60% chance it starts Sunny, 40% Rainy
    start_probabilities = np.array([0.6, 0.4])
    
    # Transition probabilities: 
    # [Sunny->Sunny, Sunny->Rainy]
    # [Rainy->Sunny, Rainy->Rainy]
    transition_matrix = np.array([
        [0.7, 0.3],
        [0.4, 0.6]
    ])
    
    # Emission probabilities:
    # [Sunny emits Walk, Sunny emits Shop, Sunny emits Clean]
    # [Rainy emits Walk, Rainy emits Shop, Rainy emits Clean]
    emission_matrix = np.array([
        [0.6, 0.3, 0.1],
        [0.1, 0.4, 0.5]
    ])
    
    # 2. Define the observation sequence to test
    # Sequence: Walk (0), Walk (0), Shop (1), Clean (2)
    obs_sequence = [0, 0, 1, 2]
    
    # 3. Execute Viterbi
    predicted_states, prob_matrix = viterbi(
        obs_sequence, 
        hidden_states, 
        start_probabilities, 
        transition_matrix, 
        emission_matrix
    )
    
    # 4. Terminal Output Display
    print("Hidden Markov Model - Viterbi Algorithm Execution\n")
    print("-" * 50)
    print(f"{'Time Step':<15} | {'Observation':<15} | {'Predicted State':<15}")
    print("-" * 50)
    
    for t in range(len(obs_sequence)):
        obs_name = observable_events[obs_sequence[t]]
        state_name = predicted_states[t]
        print(f"T = {t:<11} | {obs_name:<15} | {state_name:<15}")
        
    print("-" * 50)
    
    # 5. Graphical Output Generation
    visualize_probabilities(prob_matrix, hidden_states, obs_sequence, observable_events)

if __name__ == "__main__":
    main()