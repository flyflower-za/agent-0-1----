# 📋 Agent 从 0 到 1 学习路径 — 每日内容生成任务

> 本文件是自动内容生成的进度追踪文件。
> Cron 任务每天读取此文件，找到下一个未完成章节，生成内容并提交 GitHub。
> 大纲来源：`大纲.md`

---

## 第 1 周：理解 LLM 与 Agent 的本质

- [x] Day 01: LLM 的基本原理 — Token、Context Window、Temperature
- [ ] Day 02: Prompt Engineering 基础 — System Prompt、Few-shot、Chain-of-Thought
- [ ] Day 03: 什么是 AI Agent？与 Chatbot 的本质区别 + Agent 核心架构
- [ ] Day 04: ReAct 模式 — Reasoning + Acting 循环
- [ ] Day 05: Token 成本意识 — 模型定价、用量估算、成本优化思路
- [ ] Day 06: 实战 — 用 OpenAI / 智谱 API 跑通第一个对话 + Token 用量打印
- [ ] Day 07: 体验现有 Agent 产品 — OpenClaw、Cursor、Claude Code

## 第 2 周：变更系统领域建模 + System Prompt 设计

- [ ] Day 08: 变更系统核心实体模型 — 变更单、变更类型、审批流、风险评估
- [ ] Day 09: 用户高频问题场景梳理 Top 10 + 预期回答路径设计
- [ ] Day 10: Agent System Prompt 设计 V1 — 角色、语气、边界规则
- [ ] Day 11: Prompt 即代码 — 管理规范、版本控制、迭代流程
- [ ] Day 12: 安全边界设计 — 敏感数据识别、拒答策略、最小权限原则
- [ ] Day 13: 变更系统 API 清单梳理 + Agent 工具集初版定义
- [ ] Day 14: 实战 — 完成 W2 所有产出文档

## 第 3 周：Function Calling + 可观测性内建

- [ ] Day 15: Function Calling 机制原理 — 模型如何决定调用哪个函数
- [ ] Day 16: Tool / Function 定义规范 — JSON Schema + 单工具 vs 并行多工具
- [ ] Day 17: 工具设计原则 — 描述即 Prompt、参数约束、返回值结构化
- [ ] Day 18: 自研 ReAct 循环实现 — 核心约 50-80 行代码
- [ ] Day 19: Agent 可观测性 — Step Trace 设计与实现
- [ ] Day 20: 常见调试场景 + 测试用例集初始 10 条
- [ ] Day 21: 实战 — 命令行 Agent（mock 数据 + ReAct + Step Trace）

## 第 4 周：RAG — 变更文档智能问答

- [ ] Day 22: RAG 基础 — Embedding、向量数据库、相似度检索
- [ ] Day 23: 文档分块策略 — 固定大小 vs 语义分块
- [ ] Day 24: 变更系统特有场景 — 混合查询（API + RAG 协同）
- [ ] Day 25: 中文 Embedding 模型选型对比
- [ ] Day 26: 用 LlamaIndex 搭建最简 RAG + 结构化过滤
- [ ] Day 27: 混合查询原型实现 — 一个问题同时触发 API 和 RAG
- [ ] Day 28: RAG 评估 + 测试集扩充至 20 条

## 第 5 周：记忆、流式输出与对话体验

- [ ] Day 29: 对话上下文管理 — 滑动窗口、Context Window 处理
- [ ] Day 30: 指代消解 + 多轮对话理解
- [ ] Day 31: 对话历史持久化 — SQLite 存储与恢复
- [ ] Day 32: Token 预算管理 — 对话摘要压缩策略
- [ ] Day 33: 流式输出原理 — SSE、stream=True
- [ ] Day 34: 实现流式输出 — 思考阶段 + 执行阶段的不同策略
- [ ] Day 35: 实战 — 多轮对话 + 流式 + Token 管理完整实现

## 第 6 周：对接真实变更系统 API + 安全落地

- [ ] Day 36: 封装变更系统 API 为 Agent 工具
- [ ] Day 37: API 认证、分页、超时、限流处理
- [ ] Day 38: Prompt Injection 防御实现
- [ ] Day 39: 敏感信息过滤 + 输入输出校验层
- [ ] Day 40: Agent 权限设计 — 只读模式 + 审计日志
- [ ] Day 41: 联调测试 — 真实变更数据验证
- [ ] Day 42: 安全测试 + 测试集扩充至 40 条

## 第 7 周：Agent 工程化与流程编排

- [ ] Day 43: 意图识别与路由 — 判断走 API / RAG / 混合
- [ ] Day 44: 多步推理 — 复杂问题拆解为子查询
- [ ] Day 45: Plan-then-Execute 模式 + 结果聚合
- [ ] Day 46: 幻觉控制 + Structured Output
- [ ] Day 47: 架构整理 — 画出完整架构图、识别薄弱点
- [ ] Day 48: 评估体系建设 — 50+ 条回归测试集
- [ ] Day 49: 错误分析与质量报告

## 第 8 周：实战开发、部署与复盘

- [ ] Day 50: 核心引擎整合 — 统一入口
- [ ] Day 51: 前端界面 — Streamlit 聊天 UI
- [ ] Day 52: 联调测试 + Prompt 迭代 V2
- [ ] Day 53: 缓存策略 + 性能优化 + Token 成本统计
- [ ] Day 54: Docker 容器化部署
- [ ] Day 55: 基础监控 + 日志收集
- [ ] Day 56: 复盘总结 + V2 规划 + 知识体系脑图 🎉

---

## 📝 进度追踪

- **开始日期:** 2026-07-09
- **当前进度:** Day 1 / 56
- **最后更新:** 2026-07-08
- **下次生成:** Day 02

---

## 📋 内容生成规范

每个 Day 的 MD 文件应包含：

1. **标题与学习目标** (🎯)
2. **概念介绍** (📘) — 清晰易懂，适合入门
3. **原理深入** (🔬) — 核心机制讲解
4. **代码实战** (💻) — 可运行的 Python 代码示例
5. **实践练习** (📝) — 动手小任务
6. **小结与下节预告** (✅)

文件命名：`DayXX_主题关键词.md`（如 `Day01_LLM_Basic_Principles.md`）
