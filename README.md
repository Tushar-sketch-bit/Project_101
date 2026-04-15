# Project_101
**📊 Local-ML Insight Engine**
Hybrid Data Analysis & AI Strategy Pipeline
A high-performance Data Analysis + AI/ML project designed to maximize hardware efficiency. This project integrates a robust Python-based ETL/EDA pipeline with a local Large Language Model (LLM) to perform Augmented Analytics—transforming massive datasets into actionable business intelligence without cloud dependency.

**🛠️ The ML Pipeline Architecture**
The project is divided into three distinct phases to ensure optimal resource allocation between the CPU (Preprocessing) and GPU (Inference).

**Phase 1**: Automated EDA & Feature Engineering (Python/Pandas)
Role: The "Data Scientist" layer.
Process: Automated cleaning, outlier detection, and statistical profiling of raw datasets.
Output: Dimensionality reduction from thousands of raw records into a structured Feature Summary (means, variance, correlations, and trend coefficients).


**Phase 2**: The Contextual Bridge (Prompt Engineering)
Role: The "ML Engineer" layer.
Process: Mapping statistical findings into a high-density structured prompt.
Logic: By feeding the AI "Pre-Calculated Features" rather than "Raw Data," we eliminate calculation errors and focus the model on Analytical Reasoning and Strategic Prediction.


**Phase 3**: The Interaction Layer (Ollama / Llama 3.2)
Role: The "Business Intelligence" layer.
Process: Deploying a quantized LLM to act as an on-demand consultant for the processed data.
Outcome: 100% private, latency-free Q&A regarding data trends and business logic.


**💻 Hardware & Model Optimization**
This project is specifically tuned for Mid-Tier GPU environments (GTX 1650 / 8GB RAM) to prove that ML workflows can be run efficiently on consumer hardware.
Model Architecture: Llama 3.2 3B (Quantized to Q4_K_M).
Compute Strategy: 100% GPU Offloading. We prioritize running a lighter model entirely on VRAM (2.8 GB) rather than a larger model that spills into System RAM, preventing "Bus Bottlenecks."
Memory Safeguard: num_ctx is strictly limited to 2048–4096 to prevent Memory Inflation—ensuring the 8GB System RAM remains stable for Python tasks while the 4GB VRAM handles the AI.


**🚀 Key ML Takeaways**
Efficiency over Scale: Demonstrates that a Q4 Quantized model running at 100% GPU utilization provides higher throughput and more concise analysis than a Q8 model that causes system lag.
Zero-Cost Infrastructure: A fully local stack using Ollama & GGUF—eliminating API overhead, token costs, and data privacy risks.
Augmented Context: For external data (e.g., industry benchmarks), the project utilizes a Python-based Scraper (BeautifulSoup) to inject real-time context into the offline model manually.


Component,Tools
Data processing:  EDA, NumPy, Pandas, Matplotlib,
Data Science:  Python, Pandas, NumPy, Scikit-Learn,
Inference Engine:  Ollama, GGUF,
Web Scraping:  BeautifulSoup4,
Model:  Llama 3.2 3B (Q4_K_M),
Hardware Target:  NVIDIA GTX 1650 (4GB VRAM) / 8GB RAM
