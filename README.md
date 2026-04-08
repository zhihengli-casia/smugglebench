<div align="center">

<h1>Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation</h1>

**ACL 2026**

Zhiheng Li, Zongyang Ma, Yuntong Pan, Ziqi Zhang, Xiaolei Lv, Bo Li, Jun Gao, Jianing Zhang, Chunfeng Yuan, Bing Li, Weiming Hu

<p>
  <a href="https://huggingface.co/datasets/zhihengli-casia/smugglebench">
    <img src="https://img.shields.io/badge/Hugging%20Face-Dataset-F59E0B?logo=huggingface&logoColor=white" alt="Hugging Face dataset" />
  </a>
  <a href="https://github.com/zhihengli-casia/smugglebench">
    <img src="https://img.shields.io/badge/GitHub-Code%20%26%20README-111827?logo=github&logoColor=white" alt="GitHub repository" />
  </a>
</p>

<p>
  Official code and benchmark release for our ACL 2026 paper on adversarial smuggling attacks against multimodal content moderation.
</p>

<p>
  <a href="README_CN.md">简体中文</a> |
  <a href="https://huggingface.co/datasets/zhihengli-casia/smugglebench">Hugging Face</a> |
  <a href="#overview">Overview</a> |
  <a href="#release-contents">Code</a> |
  <a href="#license">License</a>
</p>

</div>

<p align="center">
  <img src="assets/teaser_asa_example.png" alt="A typical example of adversarial smuggling attacks" width="94%" />
</p>

## Overview

We introduce **Adversarial Smuggling Attacks (ASA)**, a new threat model for multimodal content moderation. Instead of relying on imperceptible perturbations or prompt-based jailbreaks, ASA hides harmful content in visual forms that remain readable to humans but are difficult for MLLMs to correctly perceive or interpret.

To study this problem, we build **SMUGGLEBENCH**, a benchmark specifically designed for evaluating multimodal content moderation under adversarial smuggling attacks. The public release contains **1,700 benchmark instances**, spanning **2 attack pathways** and **9 paper-level smuggling techniques**.

## SMUGGLEBENCH At A Glance

| Property | Value |
| --- | --- |
| Benchmark name | `SMUGGLEBENCH` |
| Release scope | Public benchmark release |
| Total samples | `1700` |
| Attack pathways | `2` |
| Smuggling techniques | `9` |
| Family-level storage layout | `Perception` / `AIGC` / `Reasoning` |
| Evaluation focus | Adversarial smuggling robustness |

## Attack Pathways

<p align="center">
  <img src="assets/attack_pathways.png" alt="Two attack pathways in adversarial smuggling attacks" width="96%" />
</p>

ASA can break multimodal moderation in two different ways:

- **Perceptual Blindness**: the model fails at the perception stage and cannot reliably extract the harmful text from the image.
- **Reasoning Blockade**: the model can read the text, but fails to recognize its harmful intent during semantic interpretation.

## Benchmark Taxonomy

<p align="center">
  <img src="assets/taxonomy_and_stats.png" alt="Taxonomy discovery, data curation, and benchmark statistics" width="92%" />
</p>

The benchmark covers the following paper-level techniques:

| Pathway | Technique | Count |
| --- | --- | ---: |
| Perceptual Blindness | Tiny Text | 200 |
| Perceptual Blindness | Occluded Text | 200 |
| Perceptual Blindness | Low Contrast | 200 |
| Perceptual Blindness | Handwritten Style | 200 |
| Perceptual Blindness | Artistic/Distorted | 200 |
| Perceptual Blindness | AI Illusions | 400 |
| Reasoning Blockade | Dense Text Masking | 100 |
| Reasoning Blockade | Semantic Camouflage | 100 |
| Reasoning Blockade | Visual Puzzles | 100 |
| Total | - | 1700 |

> **Note**
> The paper taxonomy contains **9 techniques**, while the public release is organized into **10 storage subfolders**. This is expected: the paper-level technique **AI Illusions** is stored as two release subsets, `AIGC/01_Blended_Background` and `AIGC/02_Multi-Picture Camouflage`.

## Representative Cases

<p align="center">
  <img src="assets/cases/tiny_text_cases.png" alt="Tiny text examples" width="92%" />
</p>

<p align="center">
  <img src="assets/cases/occlusion_text_cases.png" alt="Occluded text examples" width="92%" />
</p>

<p align="center">
  <img src="assets/cases/artistic_distorted_cases.png" alt="Artistic and distorted examples" width="92%" />
</p>

## Release Contents

This repository is organized as the project homepage and code release for the paper.

- `annotations/`: JSONL annotations for the public release.
- `inference.py`: inference entrypoint for OpenAI-compatible multimodal APIs.
- `evaluation.py`: evaluation script for metrics such as `ASR` and `TER`.
- `scripts/build_hf_dataset.py`: utility for exporting the Hugging Face dataset package.
- `scripts/rewrite_annotations.py`: utility for rewriting annotation paths into public-release format.

The full image release is available on Hugging Face:

- [SMUGGLEBENCH on Hugging Face](https://huggingface.co/datasets/zhihengli-casia/smugglebench)

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you have access to the released images, place them under `images/` using the relative paths referenced in the annotations.

## License

This project is released under **CC BY 4.0**. See [LICENSE](LICENSE) for details.
