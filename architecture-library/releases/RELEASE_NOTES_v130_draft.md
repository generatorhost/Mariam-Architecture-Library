# Release Notes - Mariam Architecture Library v130 draft

**Version:** v130 draft  
**Status:** Draft  
**Document ID:** MAL-RELNOTES-V130-DRAFT

## What Was Added In v130
- Added the Modular Changeability Principle to Volume 00.
- Added provider/model runtime management to Volume 15.
- Added model manager provider uploader lifecycle to Volume 16.
- Added DNA managed runtime objects to Volume 14.
- Added runtime object governance to Volume 21.
- Established that all governed Mariam objects support add, edit, delete, disable, enable, upgrade, replace, fork, rollback, export as DNA, and import from DNA according to governance.
- Established that GGUF, ONNX, SafeTensors, PyTorch, Ollama, vLLM, llama.cpp, and KTransformers models are managed as Model Providers or Model Runtimes.
- Added PDF build target `Mariam_Modular_Runtime_Object_Model_v130_draft.pdf`.
- Added ZIP package `Mariam_Architecture_Library_v130_draft.zip`.

## Build Notes
- Built with `tools/build_docs.py`.
- PDF readability is verified with `pypdf`.
- ZIP membership is verified for v130 release notes, MANIFEST, the new documents, and the v130 PDF.

## Version History
| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| v130 draft | 2026-06-30 | Draft | Added modular runtime object and provider model management. |
