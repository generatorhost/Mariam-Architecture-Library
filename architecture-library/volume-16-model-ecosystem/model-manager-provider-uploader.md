# Model Manager Provider Uploader

**Title:** Model Manager Provider Uploader  
**Version:** v130 draft  
**Status:** Draft  
**Document ID:** MAL-V16-MODEL-UPLOADER-001

## Purpose
Define the interface and lifecycle for uploading, registering, testing, approving, activating, rolling back, and exporting models and providers in Mariam.

## Scope
- Covers Model Upload, Provider Registration, Runtime Compatibility Check, Model Metadata Extraction, Quantization Metadata, Context Window Metadata, Embedding Capability Detection, Vision Capability Detection, Tool Calling Capability Detection, Model Benchmarking, Model Approval, Model Activation, Model Rollback, and Model DNA Export.
- Applies to GGUF, ONNX, SafeTensors, PyTorch, Ollama, vLLM, llama.cpp, KTransformers, and future provider/runtime adapters.

## Required Workflow
- Model Upload: accept file, reference, package, local provider handle, or remote registry reference through governed upload paths.
- Provider Registration: create a provider/runtime record with name, type, owner, version, adapter, supported operations, and permissions.
- Runtime Compatibility Check: validate architecture, hardware, runtime adapter, dependencies, memory, context window, and serving mode.
- Model Metadata Extraction: extract architecture, tokenizer, license, size, format, checksum, source, tags, and provenance.
- Quantization Metadata: record quantization family, bit depth, method, expected accuracy tradeoff, and supported runtimes.
- Context Window Metadata: record supported context length, tested context length, KV cache assumptions, and memory impact.
- Embedding Capability Detection: identify whether the model supports embeddings and under which provider interface.
- Vision Capability Detection: identify image or multimodal support and required companion files.
- Tool Calling Capability Detection: identify native, prompted, adapter-based, or unsupported tool calling behavior.
- Model Benchmarking: run latency, throughput, quality, memory, safety, and task-specific benchmarks.
- Model Approval: route results to governance, security, and technical reviewers.
- Model Activation: enable only approved provider/runtime configurations.
- Model Rollback: restore previous approved model version or disable failed activation.
- Model DNA Export: export model metadata, compatibility, benchmark evidence, approval state, and provider configuration as DNA.

## Interface Expectations
- Upload UI must show progress, validation, errors, metadata preview, and next required approval.
- Provider registry must show enabled/disabled state, runtime status, compatibility state, benchmark summary, and rollback target.
- Activation must require explicit permission and audit logging.

## Acceptance Criteria
- Models are not just files; they become governed Model Providers or Model Runtimes.
- Upload, registration, compatibility, metadata, benchmarking, approval, activation, rollback, and DNA export are documented as required lifecycle steps.
- GGUF, ONNX, SafeTensors, PyTorch, Ollama, vLLM, llama.cpp, and KTransformers can be represented without changing core architecture.

## Traceability
| Source | Relationship |
| --- | --- |
| MAL-V16-MODEL-UPLOADER-001 | Model manager provider uploader definition. |
| Volume 15 Runtime Ecosystem | Provider/runtime lifecycle reference. |
| Volume 14 DNA Operating System | DNA export/import reference. |

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v130 draft | 2026-06-30 | Draft | Added model manager provider uploader lifecycle. |
