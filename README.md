# LLM Agent Hands-on

**Author: Jiaxin Zhu, algorithm engineer in AMEC, Shanghai, China.**

**Contact Email: jiaxinzhu@amecnsh.com or C200073@ntu.edu.sg**

This repository provides hands-on exercises for learning how to build LLM agents from fundamental components to complete agent systems. It follows a progressive learning path, starting with basic LLM interfaces and gradually introducing tool use, agent execution patterns, context engineering, skills, agent runtime, evaluation, and optimization. The repository contains two main components:

- **labs** decompose LLM agent systems into small building blocks.
- **projects** integrate these building blocks for applications.

## Hands-on Labs

### Lab 01: LLM Interface and Tool Use

Set up the basic interface between an application and an LLM and enable the model to produce structured outputs and interact with external tools. Topics include:

- LLM API client
- Instruction prompts using system and user instructions
- Structured output with schemas
- Function calling
- MCP (model context protocol)

### Lab 02: Agent Workflow and Agent Loop

Build minimal agents using two fundamental execution patterns, i.e., chain-like agents with predefined workflows and loop-like agents based on ReAct. Topics include:

- Workflow
- ReAct

### Lab 03: Context Engineering with Prompt Management

Construct and manage the context observed by an LLM at each step so that relevant information is provided while controlling context size and maintaining output quality. Topics include:

- Prompt template
- Context organization
- Context selection
- Context optimization
- Memory

### Lab 04: Context Engineering with Skills

Package reusable specific knowledge, instructions, and procedures into skills that can be selected and executed when needed. Topics include:

- Skill definition
- Skill selection
- Skill composition
- Skill execution

### Lab 05: Harness Engineering for Agent Runtime

Build an agent harness from the perspective of RL policy-environment interaction. The harness sets up and maintains the runtime environment in which an agent receives observations, takes actions, and produces long-horizon trajectories reliably. Topics include:

- Environment setup and reset
- State and observation
- Action space and tool execution
- Environment transition
- Episode and trajectory management
- Termination and truncation
- State checkpointing and rollout resumption

### Lab 06: Agent Evaluation

Evaluate whether an agent successfully completes a task and analyze how its execution trajectory leads to success or failure. Topics include:

- Evaluation tasks and datasets
- Task outcome evaluation
- Trajectory evaluation
- Efficiency and reliability
- Failure analysis

### Lab 07: Agent Optimization using Agentic Reinforcement Learning

## Projects
