

## Workshop 8

## Workshop Name: Use an LLM to generate diverse graph inputs for fuzzing

## Description 

Understand how incorrect or unexpected inputs can reveal bugs even in a correct algorithm.

Use an LLM to generate diverse graph inputs for testing.

Identify different types of input-related failures, including crashes, infinite loops, and logic errors.

Use an LLM to generate fuzzing inputs for a graph traversal algorithm and analyze the resulting failures.

## Targeted Courses 

Software Quality Assurance 

## Activities 

### Pre-lab Content Dissemination 

We first need to know what is fuzzing.


#### Fuzzing

- Negative software testing
- Uses random, malformed, or systematically varied data to stress the system.
- Helps uncover edge cases that normal testing may miss
- Used for security and reliability testing of software


#### LLM-based input generation for fuzzing

- Can be prompted to create malformed, adversarial, or boundary-case inputs.
- Enables task-aware fuzzing, where inputs are tailored to a specific program (e.g., BFS)
- Improves coverage beyond random or rule-based fuzzers. 

## Prerequisites

Make sure you have the following installed:

- Python 3.8 or higher
- [Ollama](https://ollama.com/download) (MacOS, Linux, or Windows)
- Jupyter Notebook or JupyterLab


### Step 1: Download and install Ollama

Visit: [https://ollama.com/download](https://ollama.com/download) and install it for your OS.

### Step 2: Start the Ollama service

Once installed, open your terminal and run:

```bash
ollama run model-name

```

### In-class Hands-on Experience 


- Learn about generating inputs with LLM for BFS 

- Code will be saved and uploaded in this repo. 

- Demo will be recorded and uploaded on CANVAS. 


### Post Lab Experience
- Extend the 1-shot graph generator to create at least 10 crashees or failures

- Among these, at least 5 must represent unique failure types.

- Extend the extraction_prompt method to include all different types of graph inputs.
  
- Classify each generated graph by the type of potential failure types described below.

- ![BFS Failure](BFS_graph_types.png)




### Rubric 

- Code and screenshot: 80%
- Comments: 20%
- Deadline: April 19, 2026
