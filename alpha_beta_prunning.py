import os
# Adjust this path if you installed Graphviz in a different location
os.environ["PATH"] += os.pathsep + r'C:\Program Files\Graphviz\bin'

import math
from graphviz import Digraph

class VisualTreeNode:
    """
    Represents a node in the game tree with tracking for visualization.
    """
    def __init__(self, name, value=None, is_max=True):
        self.name = name
        self.value = value
        self.is_max = is_max
        self.children = []
        # Tracking flags for visualization
        self.visited = False
        self.final_alpha = -math.inf
        self.final_beta = math.inf

    def add_child(self, child_node):
        """
        Connects a child node to this parent node.
        """
        self.children.append(child_node)

def alpha_beta_visual(node, alpha, beta, is_maximizing, graph, pruned_edges):
    """
    Executes Alpha-Beta pruning while logging structural data into a Graphviz object.
    Identifies and stores pruned connections.
    """
    node.visited = True
    
    # Base case: Leaf node evaluation
    if not node.children:
        node.final_alpha = alpha
        node.final_beta = beta
        return node.value

    if is_maximizing:
        best_val = -math.inf
        for i, child in enumerate(node.children):
            # Evaluate child branch
            value = alpha_beta_visual(child, alpha, beta, False, graph, pruned_edges)
            best_val = max(best_val, value)
            alpha = max(alpha, best_val)
            
            # Pruning condition triggered
            if beta <= alpha:
                # Track all subsequent unvisited siblings as pruned edges
                for sibling in node.children[i+1:]:
                    pruned_edges.append((node.name, sibling.name))
                break
        
        node.value = best_val
        node.final_alpha = alpha
        node.final_beta = beta
        return best_val

    else:
        best_val = math.inf
        for i, child in enumerate(node.children):
            # Evaluate child branch
            value = alpha_beta_visual(child, alpha, beta, True, graph, pruned_edges)
            best_val = min(best_val, value)
            beta = min(beta, best_val)
            
            # Pruning condition triggered
            if beta <= alpha:
                # Track all subsequent unvisited siblings as pruned edges
                for sibling in node.children[i+1:]:
                    pruned_edges.append((node.name, sibling.name))
                break
                
        node.value = best_val
        node.final_alpha = alpha
        node.final_beta = beta
        return best_val

def build_graphviz_tree(node, graph, pruned_edges):
    """
    Recursively traverses the tree structure to apply styling, labels,
    and directional edges to the final Graphviz layout.
    """
    # Construct descriptive label displaying metrics
    type_str = "MAX" if node.is_max else "MIN"
    val_str = str(node.value) if node.value is not None else "?"
    alpha_str = "-\u221e" if node.final_alpha == -math.inf else str(node.final_alpha)
    beta_str = "\u221e" if node.final_beta == math.inf else str(node.final_beta)
    
    label = f"{node.name}\n({type_str})\nVal: {val_str}\n\u03b1:{alpha_str} | \u03b2:{beta_str}"
    
    # Apply distinguishing node styles based on type and status
    if not node.children:
        # Leaf node design
        graph.node(node.name, label=f"{node.name}\nValue: {node.value}", shape="box")
    else:
        # Internal node design
        shape_type = "triangle" if node.is_max else "invtriangle"
        graph.node(node.name, label=label, shape=shape_type)

    for child in node.children:
        # Generate structural relationships
        build_graphviz_tree(child, graph, pruned_edges)
        
        # Determine if the connecting line falls under a pruned category
        if (node.name, child.name) in pruned_edges:
            # Render pruned paths with distinct dashed, low-visibility configurations
            graph.edge(node.name, child.name, style="dashed", color="gray", label="PRUNED")
        else:
            # Normal evaluated connection
            graph.edge(node.name, child.name, style="solid")

def main():
    """
    Main driver script setting up a multi-level tree to verify pruning logic.
    """
    # Structure definition (3-level deeper tree to create pruning opportunities)
    root = VisualTreeNode("Root", is_max=True)
    
    b1 = VisualTreeNode("B1", is_max=False)
    b2 = VisualTreeNode("B2", is_max=False)
    root.add_child(b1)
    root.add_child(b2)
    
    c1 = VisualTreeNode("C1", is_max=True)
    c2 = VisualTreeNode("C2", is_max=True)
    c3 = VisualTreeNode("C3", is_max=True)
    c4 = VisualTreeNode("C4", is_max=True)
    b1.add_child(c1)
    b1.add_child(c2)
    b2.add_child(c3)
    b2.add_child(c4)
    
    # Leaf node values assigned
    c1.add_child(VisualTreeNode("L1", value=3))
    c1.add_child(VisualTreeNode("L2", value=5))
    c2.add_child(VisualTreeNode("L3", value=6))
    c2.add_child(VisualTreeNode("L4", value=9))
    
    c3.add_child(VisualTreeNode("L5", value=1))
    c3.add_child(VisualTreeNode("L6", value=2))
    c4.add_child(VisualTreeNode("L7", value=0))
    c4.add_child(VisualTreeNode("L8", value=-2))

    # Initialize execution tracking containers
    dot = Digraph(comment='Alpha-Beta Pruning Tree')
    dot.attr(rankdir='TB')  # Top-to-bottom layout hierarchy
    
    pruned_list = []
    
    print("Executing Alpha-Beta Search...")
    optimal_value = alpha_beta_visual(root, -math.inf, math.inf, True, dot, pruned_list)
    print(f"Alpha-Beta execution completed. Optimal value: {optimal_value}")
    print(f"Pruned structural connections detected: {pruned_list}")

    # Build and generate the visualization matrix
    build_graphviz_tree(root, dot, pruned_list)
    
    # Saves file to the current project directory as 'alpha_beta_tree.gv.png'
    output_filename = 'alpha_beta_tree.gv'
    dot.render(output_filename, format='png', cleanup=True)
    print(f"Tree visual representation generated successfully as: {output_filename}.png")

if __name__ == "__main__":
    main()