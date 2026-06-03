---
name: mlops-operations
description: "Umbrella skill for ML Operations: inference serving (vLLM), fine-tuning (TRL), evaluation (LM-Eval), and multimodal models (SAM, AudioCraft)."
---

# MLOps Operations

This skill provides a consolidated framework for managing the lifecycle of machine learning models, from fine-tuning and evaluation to production-grade inference.

## Core Workflows

### 1. Model Fine-Tuning (TRL)
**Trigger**: When the user needs to adapt an LLM to specific tasks using SFT, DPO, or RLHF.
- **Tools**: Use the `TRL` library for reinforcement learning from human feedback.
- **Reference**: `references/trl.md` for detailed code examples and checklists.

### 2. Model Evaluation (LM-Eval)
**Trigger**: When measuring model performance on standard benchmarks (MMLU, GSM8K).
- **Tools**: Use `lm-evaluation-harness` for zero-shot and few-shot evaluation.
- **Reference**: `references/evaluation.md` for benchmarking procedures.

### 3. High-Throughput Inference (vLLM)
**Trigger**: When deploying models for production use with high concurrency.
- **Tools**: Use `vLLM` for PagedAttention-optimized serving.
- **Reference**: `references/vllm.md` for server configuration and load testing.

### 4. Multimodal Generation (AudioCraft, SAM)
**Trigger**: When generating audio/music or performing image segmentation.
- **Audio**: Use `AudioCraft` (MusicGen/AudioGen) for text-to-audio.
- **Vision**: Use `Segment Anything Model (SAM)` for zero-shot segmentation.
- **References**: `references/audiocraft.md`, `references/segment-anything.md`.

### 5. Efficient Training & Optimization (Axolotl, Unsloth)
**Trigger**: When training models with limited VRAM or needing 2-5x speedups.
- **Axolotl**: Use for YAML-based configuration of LoRA/QLoRA training.
- **Unsloth**: Use for optimized kernels that reduce VRAM usage and increase speed.
- **Related Skills**: `mlops/training/axolotl`, `mlops/training/unsloth`.

### 6. Declarative LLM Programming (DSPy)
**Trigger**: When building complex RAG pipelines or needing automated prompt optimization.
- **Action**: Use DSPy to define modules and optimize them against a metric.
- **Related Skill**: `mlops/research/dspy`.

### 7. Structured Output & Safety (Outlines, Obliteratus)
- **Outlines**: Use for JSON schema enforcement and regex-guided generation.
- **Obliteratus**: Use for debiasing and abliterating refusals.
- **Related Skills**: `mlops/inference/outlines`, `mlops/inference/obliteratus`.

## Sub-Workflows (References)

Detailed implementation guides:
- `references/vllm.md`: vLLM server setup, quantization (AWQ/GPTQ), and metrics.
- `references/trl.md`: Supervised Fine-Tuning (SFT) and Reward Modeling.
- `references/evaluation.md`: Benchmark selection and few-shot prompting.
- `references/audiocraft.md`: MusicGen and AudioGen pipelines.
- `references/segment-anything.md`: Box/Point-based image segmentation.
