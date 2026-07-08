# Day 01: LLM 的基本原理 — Token、Context Window、Temperature

> 🗡️ **变更系统 Agent 助手 · 学习路径**

---

## 🎯 学习目标

今天我们要搞清楚三件事——它们是理解所有大语言模型（LLM）的"地基"：

1. **Token 是什么？** — 模型怎么"看懂"你说的话
2. **Context Window 是什么？** — 模型到底能记住多少东西
3. **Temperature 是什么？** — 为什么有时候模型"很乖"，有时候又"天马行空"

学完今天的内容，你不仅能回答这三个问题，还能动手调 API 感受它们的真实效果。

---

## 📘 概念介绍

### 🧩 Token：模型读的不是字，是 Token

想象你是一个外星人来到地球。人类对你说了一句话，你的大脑不是逐字理解，而是**把整句话拆成你认识的"语义积木块"**，再用这些积木理解意思。

LLM 做的事情类似。

**Token = 模型能理解的最小语义单元**

- 一个 Token 可以是一个词、一个部分词、或者一个字符
- 中文里：一个字可能就是一个 Token（比如"变"），也可能多个字合并成一个（比如"变更"）
- 英文里：一个词通常 1-2 个 Token（"hello" = 1，"because" = 2）

举个例子，"变更系统今天有 3 个紧急变更"这句话，模型会拆成：

```
变 | 更 | 系 | 统 | 今 | 天 | 有 | 3 | 个 | 紧 | 急 | 变 | 更
```

或者更可能是（取决于模型的分词器）：

```
变更 | 系统 | 今天 | 有 | 3 | 个 | 紧急 | 变更
```

模型**不会读你的原始文本**，它只读 Token。所以 Token 的数量决定了：

- 💰 **你的账单** — 大部分 API 按 Token 计费
- ⏱️ **处理速度** — Token 越多，处理越慢
- 🧠 **记忆容量** — 模型最多能看多少 Token

### 📏 Context Window：模型的"工作台"

打开一个浏览器，你同时能打开多少个标签页？10 个？50 个？不管多牛，总有个上限。

LLM 也有这个上限，叫做 **Context Window**（上下文窗口）。

> Context Window = 模型一次对话能同时看到的 Token 总数

包括：
- 你设置的 System Prompt（角色设定）
- 当前你问的问题
- 之前对话的历史
- 工具定义（Function Calling 时）

目前主流模型的 Context Window 大小：

| 模型 | Context Window |
|------|---------------|
| GPT-4o | 128K Tokens |
| GPT-4o-mini | 128K Tokens |
| Claude 3.5 Sonnet | 200K Tokens |
| 智谱 GLM-4 | 128K Tokens |
| DeepSeek V3 | 128K Tokens |

128K 听起来很多是吧？可以写一整本《三体》了。但**别忘了**：

- System Prompt 占几百到几千
- 工具定义占几千
- 对话历史累积起来很快
- 每次 API 调用都要传完整上下文

所以 **Context 不是无限的**，实际可用空间比你想象的小得多。

### 🌡️ Temperature：控制模型的"创造力"

Temperature（温度）控制 LLM 输出的**随机性**。本质上它影响模型在预测下一个 Token 时的概率分布。

用比喻来理解：

- **低温（0.0 - 0.3）** → 模型像一位严谨的公务员：每次给最确定的答案，不爱创新，但稳定可靠
- **中温（0.5 - 0.8）** → 模型像一位有经验的顾问：通常给出标准答案，偶尔有点小创意
- **高温（0.8 - 1.5+）** → 模型像一个喝多了的艺术家：什么都敢说，天马行空，但不太靠谱

对于**变更系统 Agent** 这种业务场景，我们希望 Agent **准确、稳定、不瞎编**，所以应该用低 Temperature（0.0 - 0.3）。

---

## 🔬 原理深入

### Token 的内部机制

让我们拆解一次 API 调用的完整流程：

```
用户输入: "查一下 CHG-2026-001 的状态"
        ↓
  文本转 Token 序列
        ↓
  [3681, 756, 45, 12856, 2026, 11, 001, 532, 892]
        ↓
  模型看 Token 序列 + 上下文 → 预测下一个 Token
        ↓
  逐步生成回答 Tokens
        ↓
  把回答 Tokens 转回文本
        ↓
  "变更 CHG-2026-001 目前处于审批中状态"
```

关键是：**模型一次只看一个方向（从左到右）**，根据已经看到的 Token 预测下一个最可能是什么。

这就是所谓的**自回归（Auto-regressive）** 生成。

举个例子，当模型看到输入 "查一下 CHG-2026-001 的" 后，它会计算：

```
"状态" → 概率 0.85
"审批" → 概率 0.07
"详情" → 概率 0.05
...    → 其他 0.03
```

然后选概率最高的那个作为下一个 Token。

### Temperature 如何影响概率

刚才的例子中，"状态"的概率是 0.85，其他选项都远低于它。

现在来看看 Temperature 对概率分布做了什么操作：

```
Temperature = 0.0
  模型永远选概率最高的 Token → "状态"
  → 每次都一样 → 确定性输出

Temperature = 0.7 (默认)
  稍微平滑概率 → "状态" 有 85% 概率被选中
  → 大多数时候一样，偶尔不同

Temperature = 1.5
  大幅平滑概率 → "状态" ~40%，"审批" ~20%，"详情" ~15%
  → 每次都可能不同 → 创造性输出
```

背后的数学原理其实不复杂：

```
原始概率: [0.85, 0.07, 0.05, 0.03]
除以 Temperature: T=0.7 → [1.21, 0.10, 0.07, 0.04]  → Softmax → [0.74, 0.13, 0.08, 0.05]
                   T=1.5 → [0.57, 0.05, 0.03, 0.02]  → Softmax → [0.40, 0.23, 0.18, 0.09]
```

温度越低，高概率 Token 的优势越明显；温度越高，所有 Token 的概率越接近。

### Context Window 的超载问题

当对话变长，Context Window 超了怎么办？

```
Context Window: 128K Tokens
已使用: 100K Tokens (历史对话 + 文档)
新消息: 5K Tokens
剩余:  23K Tokens  ✅ 没问题

已使用: 126K Tokens
新消息: 5K Tokens
超出:  3K Tokens  ❌ 出问题了！
```

超出后的行为因模型而异：
1. **直接错误** — API 返回错误，告诉你超了
2. **截断** — 默默忘掉最早的内容（你的 System Prompt 可能就被忘了！）
3. **滑动窗口** — 智能地丢弃最不重要的内容

对于变更系统 Agent 来说，**Context Window 超载是大忌**。想象一下用户问了 20 个问题后，Agent 突然不记得系统提示了——这是灾难。

所以后面 W5 我们会专门学**对话历史管理**来避免这个问题。

---

## 💻 代码实战

让我们用 OpenAI 兼容的 API 来体验 Token、Context Window 和 Temperature 的真实效果。

### ✅ 准备工作

确保你已安装 OpenAI SDK：

```bash
pip install openai
```

### 📝 代码：第一个 LLM 调用 + Token 用量打印

```python
"""
hello-llm.py — 第一个 LLM 对话 + Token 用量打印
场景：让模型扮演"变更系统助手"
"""

from openai import OpenAI

# 初始化客户端
# 假设你用智谱 API（兼容 OpenAI SDK）
client = OpenAI(
    api_key="your-api-key-here",       # ← 换成你的 API Key
    base_url="https://open.bigmodel.cn/api/paas/v4"  # 智谱的 API 端点
)

# System Prompt：定义 Agent 的角色
system_prompt = """你是"变更系统助手"，一个专业的变更管理咨询助手。

你的职责：
- 帮助用户查询变更信息
- 解释变更流程和规则
- 提供变更管理建议

你的性格：
- 专业可靠，语言简洁
- 只用事实说话，不编造信息
- 不知道的就说不知道

变更系统背景：公司变更管理系统，管理从开发到上线的所有变更请求。
"""

# 用户的问题
user_query = "查一下 CHG-2026-001 这个变更的状态"

# 调用 API
response = client.chat.completions.create(
    model="glm-4-plus",              # 智谱的模型名
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_query}
    ],
    temperature=0.1,                  # 低温 → 稳定的回答
    stream=False                      # 先不流式输出
)

# 打印模型回答
print("🤖 Agent 回答:")
print(response.choices[0].message.content)

# ⭐ 重点：查看 Token 用量！
print("\n" + "="*50)
print("💰 Token 用量详情")
print("="*50)
usage = response.usage
print(f"  Prompt Tokens:  {usage.prompt_tokens:>6}  ← 你输入的（System + 问题）")
print(f"  Completion Tokens: {usage.completion_tokens:>6}  ← 模型生成的（回答）")
print(f"  总计:             {usage.total_tokens:>6}")
```

### 📝 代码：对比不同 Temperature 的效果

```python
"""
temperature-test.py — 同样的输入，不同的 Temperature
看看回答会有什么不同
"""

from openai import OpenAI

client = OpenAI(
    api_key="your-api-key-here",
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

system_prompt = "你是一个变更系统助手，请用简洁的语言回答。"
user_query = "变更申请应该包含哪些内容？"

temperatures = [0.0, 0.5, 1.0, 1.5]

for temp in temperatures:
    # 每个 Temperature 调 2 次，看稳定性
    for i in range(2):
        response = client.chat.completions.create(
            model="glm-4-plus",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            temperature=temp,
        )

        answer = response.choices[0].message.content
        print(f"\n🌡️ Temperature = {temp} (第 {i+1} 次)")
        print(f"   回答: {answer[:80]}...")
        print(f"   Tokens: {response.usage.total_tokens}")
```

运行后你会看到：Temperature = 0 时两次回答几乎一样；Temperature = 1.5 时两次回答可能完全不一样，甚至模型会开始编造内容——这就是所谓的**幻觉**。

### 📝 代码：感受 Context Window 的影响

```python
"""
context-test.py — 测试模型能记住多少对话
"""

from openai import OpenAI

client = OpenAI(
    api_key="your-api-key-here",
    base_url="https://open.bigmodel.cn/api/paas/v4"
)

messages = [
    {"role": "system", "content": "你是变更系统助手，请简洁回答。"},
]

# 模拟多轮对话
queries = [
    "查一下 CHG-2026-001 的状态",
    "它的审批人是谁？",
    "审批到第几步了？",
    "之前问到的是哪个变更单号？"
]

for q in queries:
    messages.append({"role": "user", "content": q})

    response = client.chat.completions.create(
        model="glm-4-plus",
        messages=messages,
        temperature=0.1,
    )

    answer = response.choices[0].message.content
    print(f"\n🧑 用户: {q}")
    print(f"🤖 Agent: {answer}")

    # 把回答加入历史，继续下一轮对话
    messages.append({"role": "assistant", "content": answer})

print("\n" + "="*50)
print(f"📊 本轮对话总 Token 数: {response.usage.total_tokens}")
```

注意观察：
- 第二问"它的审批人是谁？"— 模型还能记住"它"指 CHG-2026-001 吗？
- 第四问"之前问到的是哪个变更单号？"— 模型还记得吗？

如果模型答不上来，说明 Context Window 里的关键信息被挤走了（或者模型本身的多轮对话能力不够强）。

---

## 📝 实践练习

### 练习 1：理解 Token — 手算 Token 数

把下面这段话用 Python 估算 Token 数（中文通常 1 字 ≈ 1-2 Tokens）：

> "变更系统 Agent 助手需要能够根据用户的问题，查询变更状态、审批流程、影响范围等信息，并基于公司 SOP 文档提供专业建议。"

你的任务：
1. 数一下这段话有多少个字
2. 估算它大概有多少 Tokens（中文 1 字 ≈ 1.3 Tokens）

### 练习 2：搭建你的第一个 System Prompt

写一个 System Prompt，让模型扮演"公司变更管理助理"：

要求：
- 约 100-200 字
- 包含：角色定义、核心职责、行为边界
- 保存到 `prompts/system-v0.md`

```markdown
# prompts/system-v0.md — 变更系统助理 System Prompt V0

你是[你定义的角色]...
```

### 练习 3：Temperature 对比

用上面给的 `temperature-test.py` 代码：

1. 运行 Temperature = 0.0 各两次，观察输出是否一致
2. 运行 Temperature = 1.5 各两次，观察输出差异
3. 思考：对于"查询变更状态"这种任务，应该用低温还是高温？

### 练习 4：Context Window 极限测试

修改 `context-test.py`，把用户查询循环增加到 20 轮：

```python
queries = [
    f"这是第 {i} 个问题：CHG-2026-{i:03d} 的状态是什么？"
    for i in range(1, 21)
]
```

观察：
- 第几轮之后模型开始"失忆"？
- 它还能记得 System Prompt 中的角色设定吗？

---

## ✅ 小结与下节预告

### 今天你学到了什么

| 概念 | 一句话总结 | 对 Agent 的意义 |
|------|-----------|----------------|
| **Token** | 模型的最小语义单元，也是计费单位 | Token 数 = 你的成本，写 Prompt 要精简 |
| **Context Window** | 模型一次能看到的 Token 上限 | 对话不能无限长，需要管理历史 |
| **Temperature** | 控制输出的随机性/创造力 | 变更系统 Agent 建议用 0.0-0.3 |

### 底层心法

今天这三件事有一个共同主题：**LLM 不是魔法，它有物理限制**。

- Token 让你知道"说人话"是有成本的
- Context Window 让你知道模型的记忆是有限的
- Temperature 让你知道模型的"思考"是概率性的

**理解这些限制，是成为一个合格的 Agent 工程师的第一步。**

### 下节预告：Day 02 — Prompt Engineering 基础

> 知道了模型怎么读 Token、怎么记住东西，明天我们来学**怎么写 Prompt 能让模型更好地理解你的意图**。
>
> 你会学到 System Prompt、Few-shot 示例、Chain-of-Thought 等核心技巧，并把这些技巧应用到变更系统场景中。

---

> 💡 **小贴士**：今天的内容可能有点"理论"，但别急。从明天开始我们会越来越多地把理论变成代码。第 1 周就是在打地基，地基稳了，后面的 Agent 才不会歪。
>
> 🗡️ **大侠说**：理解 Token 和 Context Window 不是说你要精通 NLP，而是让你在做 Agent 时能预判问题——"这个查询会不会超 Context？""这个 System Prompt 是不是太长了？"有了预判能力，你就比 90% 的人强了。
