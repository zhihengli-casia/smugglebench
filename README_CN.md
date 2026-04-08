<div align="center">

<h1>Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation</h1>

**ACL 2026**

Zhiheng Li, Zongyang Ma, Yuntong Pan, Ziqi Zhang, Xiaolei Lv, Bo Li, Jun Gao, Jianing Zhang, Chunfeng Yuan, Bing Li, Weiming Hu

<p>
  <img src="https://img.shields.io/badge/Benchmark-SMUGGLEBENCH-0F766E" alt="Benchmark badge" />
  <img src="https://img.shields.io/badge/Samples-1.7K-2563EB" alt="Sample count badge" />
  <img src="https://img.shields.io/badge/Pathways-2-D97706" alt="Pathway badge" />
  <img src="https://img.shields.io/badge/Techniques-9-475569" alt="Technique badge" />
</p>

<p>
  本仓库是 ACL 2026 论文 <strong>Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation</strong> 的官方代码与基准发布页。
</p>

<p>
  <a href="README.md">English</a> |
  <a href="#概述">概述</a> |
  <a href="#仓库内容">代码</a> |
  <a href="#引用">引用</a> |
  <a href="#许可证">许可证</a>
</p>

</div>

<p align="center">
  <img src="assets/teaser_asa_example.png" alt="Adversarial Smuggling Attacks 示例图" width="94%" />
</p>

## 概述

我们提出了一个新的多模态内容审核威胁模型：**Adversarial Smuggling Attacks (ASA)**。这类攻击不同于传统的不可感知扰动，也不同于依赖提示词的 jailbreak，而是将违规内容隐藏在“人类可读、模型难读”或“模型虽可读但难以正确理解”的视觉表达中，从而绕过 MLLM 内容审核。

围绕这一问题，我们构建了 **SMUGGLEBENCH**，用于系统评测多模态内容审核模型在 adversarial smuggling attacks 下的鲁棒性。当前公开版本包含 **1700 个 benchmark 实例**，覆盖 **2 条攻击路径** 和 **9 种论文口径的 smuggling techniques**。

## SMUGGLEBENCH 一览

| 属性 | 内容 |
| --- | --- |
| Benchmark 名称 | `SMUGGLEBENCH` |
| 发布范围 | 公开 benchmark 发布版 |
| 样本总数 | `1700` |
| 攻击路径 | `2` |
| 技术类型 | `9` |
| 发布目录组织 | `Perception` / `AIGC` / `Reasoning` |
| 评测重点 | Adversarial smuggling robustness |

## 攻击路径

<p align="center">
  <img src="assets/attack_pathways.png" alt="ASA 的两条攻击路径" width="96%" />
</p>

ASA 主要通过两种方式破坏多模态内容审核：

- **Perceptual Blindness**：模型在感知阶段就无法可靠地读出图像中的关键违规文本。
- **Reasoning Blockade**：模型能够读出文本，但在语义理解阶段未能正确识别其违规意图。

## Benchmark Taxonomy

<p align="center">
  <img src="assets/taxonomy_and_stats.png" alt="SMUGGLEBENCH 的 taxonomy、构建流程与统计信息" width="92%" />
</p>

论文口径下，SMUGGLEBENCH 覆盖以下 9 类 techniques：

| 攻击路径 | Technique | 数量 |
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

> **说明**
> 论文中的 taxonomy 是 **9 种 techniques**，而当前公开整理版的数据目录对应 **10 个存储子目录**。这是正常的，因为论文层面的 **AI Illusions** 在发布目录中被拆分为两个子集：`AIGC/01_Blended_Background` 和 `AIGC/02_Multi-Picture Camouflage`。

## Representative Cases

<p align="center">
  <img src="assets/cases/tiny_text_cases.png" alt="Tiny Text 示例" width="92%" />
</p>

<p align="center">
  <img src="assets/cases/occlusion_text_cases.png" alt="Occluded Text 示例" width="92%" />
</p>

<p align="center">
  <img src="assets/cases/artistic_distorted_cases.png" alt="Artistic/Distorted 示例" width="92%" />
</p>

## 仓库内容

本仓库以论文项目主页与代码发布页的形式组织，当前主要包含：

- `annotations/`：公开版 JSONL 标注文件。
- `inference.py`：面向 OpenAI 兼容接口的推理入口。
- `evaluation.py`：用于计算 `ASR`、`TER` 等指标的评测脚本。
- `scripts/build_hf_dataset.py`：导出 Hugging Face 数据集包的脚本。
- `scripts/rewrite_annotations.py`：将标注路径整理为公开发布格式的脚本。

完整图片数据已经整理为单独的 Hugging Face 数据集包，后续可在这里补充公开链接。

## 快速开始

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

如果你拥有公开发布的图片数据，请按照标注文件中的相对路径，将图片放置到 `images/` 目录下。

## 引用

如果这个项目对你的研究有帮助，欢迎引用我们的论文：

```bibtex
@inproceedings{li2026making,
  title={Making MLLMs Blind: Adversarial Smuggling Attacks in MLLM Content Moderation},
  author={Li, Zhiheng and Ma, Zongyang and Pan, Yuntong and Zhang, Ziqi and Lv, Xiaolei and Li, Bo and Gao, Jun and Zhang, Jianing and Yuan, Chunfeng and Li, Bing and Hu, Weiming},
  booktitle={Proceedings of ACL 2026},
  year={2026}
}
```

更规范的引用元数据也可以直接参考 [CITATION.cff](CITATION.cff)。

## 许可证

本项目采用 **CC BY 4.0** 许可证发布，详情见 [LICENSE](LICENSE)。
