# Provider Model Runtime Management

**Title:** Provider Model Runtime Management  
**Version:** v130 draft  
**Status:** Draft  
**Document ID:** MAL-V15-PROVIDER-MODEL-RUNTIME-001

## Purpose
Define how model formats and model-serving engines are managed as Model Providers or Model Runtimes inside Mariam.

## Scope
- Covers GGUF, ONNX, SafeTensors, PyTorch, Ollama models, vLLM models, llama.cpp models, and KTransformers models.
- Defines upload, registration, activation, disablement, compatibility, benchmarking, governance, rollback, and DNA export.
- Excludes direct storage of secrets, private filesystem paths, unapproved model weights, and unverified runtime execution.

## Managed Model Types
- GGUF models are managed as local or hosted model runtime assets, commonly through llama.cpp-compatible runtimes or provider adapters.
- ONNX models are managed as portable runtime artifacts with compatibility checks for execution providers and acceleration targets.
- SafeTensors models are managed as model assets with metadata, architecture, quantization, and adapter compatibility.
- PyTorch models are managed as runtime-capable assets requiring dependency, device, safety, and resource checks.
- Ollama models are managed through an Ollama Model Provider with model registry, health, context, and activation state.
- vLLM models are managed through a vLLM Model Runtime with batching, serving, memory, and throughput metadata.
- llama.cpp models are managed through a llama.cpp runtime adapter with quantization and context window metadata.
- KTransformers models are managed through a KTransformers runtime adapter for compatible architectures and execution plans.

## Lifecycle Operations
- Upload model artifact or provider reference.
- Extract model metadata.
- Register provider/runtime entry.
- Run compatibility checks.
- Benchmark model behavior.
- Approve or reject activation.
- Enable or disable model provider.
- Replace model version behind a stable provider contract.
- Roll back to a prior approved model or runtime configuration.
- Export model provider metadata as DNA.
- Import model provider metadata from DNA.

## Governance and Safety
- Model activation requires permission, versioning, audit, compatibility, testing, and rollback.
- High-risk models require governance approval before production routing.
- Local model paths, credentials, tokens, and private weights must never be exposed in documentation or logs.
- Model providers must declare tool calling, embedding, vision, context window, quantization, license, and safety constraints.

## Acceptance Criteria
- GGUF, ONNX, SafeTensors, PyTorch, Ollama, vLLM, llama.cpp, and KTransformers are documented as Providers/Runtimes.
- Providers can be uploaded, registered, enabled, disabled, replaced, rolled back, and exported as DNA.
- Compatibility and governance gates exist before model activation.

## Traceability
| Source | Relationship |
| --- | --- |
| MAL-V15-PROVIDER-MODEL-RUNTIME-001 | Runtime/provider management for model formats and runtimes. |
| Volume 16 Model Ecosystem | Model manager and provider uploader reference. |
| Volume 14 DNA Operating System | DNA export/import reference. |

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v130 draft | 2026-06-30 | Draft | Added provider/model runtime management doctrine. |
