# EgoRoBo-EgoData

中文名：伊格具身数据（EgoRoBo）  
定位：面向具身智能 / 人形机器人训练的**第一视角行为数据（Egocentric Data）**项目

> EgoRoBo-EgoData is an open, scalable, and production-oriented repository for egocentric human behavior data, focused on data collection, annotation, quality control, and dataset organization for embodied AI.

---

## 1. 项目简介

EgoRoBo-EgoData 聚焦于**第一视角行为数据**，用于支持：

- 人形机器人模仿学习（Imitation Learning）
- Manipulation / Pick-and-Place / Tool Use 等操作任务建模
- 行为分解、动作识别与任务规划
- 多任务、多主体、多环境的数据训练与评测

与偏重仿真或强化学习的项目不同，本仓库主要覆盖：

- **数据采集规范**
- **标注体系设计**
- **数据组织格式**
- **质量控制流程**
- **样例数据与元数据模板**

---

## 2. 核心特色

### 2.1 第一视角（Egocentric）
- 以头戴 / 胸戴 / 近眼相机为主
- 视角更接近机器人真实执行时的观测输入
- 更适合学习“看见-决策-操作”的完整链路

### 2.2 可控采集
- 支持统一场景、统一光照、统一工位、统一拍摄参数
- 支持**同一任务由不同人执行**
- 支持**同一人执行不同任务**
- 支持任务变量与环境变量的交叉验证

### 2.3 面向生产的数据组织
- 统一命名规范
- 明确目录结构
- 兼容视频、轨迹、动作段、文本标签、质检结果
- 便于后续扩展到大规模训练集

### 2.4 可扩展标注体系
支持多层级标注：
- 任务级（Task-level）
- 步骤级（Step-level）
- 动作级（Action-level）
- 物体级（Object-level）
- 质量级（Quality-level）

---

## 3. 适用场景

本项目适用于以下第一视角行为数据：

- 日常整理：收纳、摆放、清洁、开关门
- 工具使用：拧螺丝、组装、拆卸、搬运
- 精细操作：抓取、对齐、插入、旋转、按压
- 服务机器人：取物、递交、整理台面
- 工业辅助：标准工序复现、装配流程记录

---

## 4. 数据结构设计

```text
EgoRoBo-EgoData/
├── README.md
├── LICENSE
├── .gitignore
├── docs/
│   ├── data_collection_protocol.md
│   ├── annotation_guideline.md
│   ├── quality_control.md
│   └── benchmark_tasks.md
├── dataset_card/
│   └── dataset_card_zh.md
├── metadata/
│   ├── tasks.csv
│   ├── subjects.csv
│   └── environments.csv
├── annotations/
│   ├── task_schema.json
│   └── sample_annotation.json
├── samples/
│   ├── video/
│   │   └── README.md
│   └── trajectory/
│       └── README.md
├── examples/
│   ├── task_list_example.csv
│   ├── session_metadata_example.json
│   └── annotation_example.json
├── scripts/
│   ├── validate_metadata.py
│   └── build_dataset_index.py
└── assets/
    └── logo_placeholder.txt
```

---

## 5. 推荐数据字段

### 5.1 Session 元数据
每条采集 session 建议包含：

| 字段 | 说明 |
|------|------|
| session_id | 采集会话唯一ID |
| task_id | 任务ID |
| subject_id | 执行者ID（匿名化） |
| env_id | 场景ID |
| camera_type | 相机类型 |
| camera_position | 头戴 / 胸戴 / 眼镜式 |
| fps | 帧率 |
| resolution | 分辨率 |
| lighting | 光照条件 |
| hand_dominance | 左/右利手 |
| start_time | 采集开始时间 |
| duration_sec | 时长 |
| qc_status | 质检状态 |

### 5.2 标注字段

| 字段 | 说明 |
|------|------|
| task_name | 任务名称 |
| step_id | 步骤编号 |
| step_name | 步骤名称 |
| action_label | 动作标签 |
| object_label | 目标物体标签 |
| start_frame | 起始帧 |
| end_frame | 结束帧 |
| success_flag | 是否成功完成 |
| occlusion_flag | 是否存在遮挡 |
| anomaly_flag | 是否有异常 |

---

## 6. 标注体系建议

### 一级：任务级标签
- pick_up_object
- place_object
- open_drawer
- close_drawer
- wipe_surface
- assemble_component
- use_tool

### 二级：步骤级标签
例如任务 `assemble_component` 可拆为：
1. pick_part
2. align_part
3. insert_part
4. fasten_part
5. verify_result

### 三级：动作级标签
- reach
- grasp
- lift
- move
- align
- rotate
- insert
- push
- release

---

## 7. 质量控制（QC）建议

建议建立最少 4 层质检：

1. **采集前检查**：相机角度、清晰度、工位完整性
2. **采集中检查**：遮挡、抖动、丢帧、任务偏离
3. **采集后初审**：命名规范、元数据完整性、任务覆盖度
4. **标注后复审**：标签一致性、边界帧准确性、异常片段处理

### 推荐质检指标
- 视频可用率
- 标注一致率
- 任务完成率
- 重采率
- 帧级清晰度通过率
- 片段切分准确率

---

## 8. 与企业自采的区别

| 维度 | 企业自采 | EgoRoBo-EgoData 模式 |
|------|----------|----------------------|
| 采集搭建成本 | 高 | 标准化复用，成本更低 |
| 数据一致性 | 团队差异大 | 流程统一，数据更稳 |
| 任务扩展速度 | 慢 | 可快速复制新任务 |
| 质检体系 | 往往临时搭建 | 可沉淀为标准流程 |
| 标注规范 | 易不统一 | 支持统一 schema |

---

## 9. 快速开始

### 9.1 克隆仓库
```bash
git clone https://github.com/your-org/EgoRoBo-EgoData.git
cd EgoRoBo-EgoData
```

### 9.2 校验元数据
```bash
python scripts/validate_metadata.py --input examples/session_metadata_example.json
```

### 9.3 构建数据索引
```bash
python scripts/build_dataset_index.py --root . --output dataset_index.json
```

---

## 10. Roadmap

- [x] 第一视角数据仓库基础结构
- [x] 中文数据卡模板
- [x] 采集规范文档
- [x] 标注规范文档
- [x] 元数据校验脚本
- [ ] 增加公开视频样例
- [ ] 增加基准任务 Benchmark 列表
- [ ] 增加 Hugging Face / OpenX 风格导出格式
- [ ] 增加训练数据转换工具

---

## 11. 贡献方式

欢迎贡献：

- 新的任务 schema
- 标注规范建议
- 数据清洗脚本
- 可公开的样例数据
- 面向 embodied AI 的 benchmark 设计

请先阅读：`docs/annotation_guideline.md` 和 `docs/data_collection_protocol.md`

---

## 12. License

建议根据你是否开放数据选择：

- 文档与代码：MIT / Apache-2.0
- 数据样例：CC BY-NC 4.0 或自定义数据许可

> 若项目主要用于商业合作，可将公开仓库仅作为项目介绍与样例展示，真实数据通过私有交付。

---

## 13. 联系方式

- Project Name: EgoRoBo-EgoData
- 中文名：伊格具身数据
- Focus: Egocentric Human Behavior Data for Embodied AI

