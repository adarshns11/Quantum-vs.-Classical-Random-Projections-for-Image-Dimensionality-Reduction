Quantum vs. Classical Random Projections for Image Dimensionality Reduction 
This project investigates the effectiveness of Quantum Random Projections (QRP) 
compared to Classical Random Projections (CRP) for reducing the dimensionality of MNIST digit images.
 Project Components
 
quantum_random_projections.ipynb: Research notebook containing the experimental setup, benchmarking, and accuracy comparisons.
dashboard.py: An interactive Streamlit application for real-time digit classification and embedding visualization.
requirements.txt:

Methodology

1. PreprocessingIn modern machine learning, high-dimensional data (like 784-pixel images) leads to the "Curse of Dimensionality."
2.  We reduce these images to 8x8 (64 pixels) to benchmark how different mathematical projections preserve information. 
3. Quantum Feature Mapping (QRP)We implement a 6-qubit quantum circuit using the following architecture:

Layers :b Encoding Layer: Random Mixing Layer:  Entanglement Layer: Extraction: 

Classical Baseline (CRP)Uses a Gaussian random matrix to project the 64D data into a lower-dimensional space, serving as a benchmark for the quantum model's performance. 
Key Insight

While Classical RP yields slightly higher accuracy, Quantum RP generates more compact clusters in the projected feature space. 
As shown in our PCA visualization, the Quantum model groups digit classes more tightly, suggesting a higher potential for non-linear classification tasks.
