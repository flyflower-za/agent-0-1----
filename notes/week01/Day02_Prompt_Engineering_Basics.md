# Day 02: Prompt Engineering 基础 — System Prompt、Few-shot、Chain-of-Thought

> 你已经知道 LLM 在做"文字接龙"（续写 Token）。但怎么让它**按你的意思**续写？这就是 Prompt Engineering 要做的事。

---

## 🎯 学习目标

- 理解什么是 Prompt Engineering，它为什么重要
- 掌握三种核心技巧：System Prompt、Few-shot、Chain-of-Thought
- 能手写一个"变更系统助手"的角色 System Prompt
- 能通过 Few-shot 让 LLM 学会输出特定格式
- 能用 Chain-of-Thought 让 LLM 进行多步推理

---

## 📘 概念介绍

### 用遥控器打个比方

想象你有一个非常聪明的助手，但他有个毛病——**你不说清楚他就猜**。你说"帮我查个东西"，他可能端杯水过来。你说"帮我查一下 CHG-2026-001 这个变更单的审批状态"，他就去查了。

**Prompt 就是你对这个助手说的每一句话。** 说得越清楚，他做得越准。

Prompt Engineering 说白了就是**学会怎么跟 AI 说话**——不是跟人说话那种"你懂的"，而是把话说到位，不给模型自由发挥的空间。

### 三个层次

| 技巧 | 比喻 | 说明 |
|------|------|------|
| **System Prompt** | 上岗培训手册 | 告诉 AI：你是谁、什么能做、什么不能做、什么语气 |
| **Few-shot** | 给几个标准范例 | "像这样回答"——给几个输入输出的例子 |
| **Chain-of-Thought** | 说"请一步步思考" | 让模型把推理过程写出来，减少跳步导致的错误 |

---

## 🔬 原理深入

### 1. System Prompt — AI 的上岗培训手册

这是 Prompt Engineering 里**最重要的概念**。没有之一。

大多数 LLM API（OpenAI、智谱等）都支持两种消息角色：

- **System Message（系统消息）**：给模型的全局指令，设定角色和行为边界。**用户看不到。**
- **User Message（用户消息）**：用户实际输入的问题。

```python
messages = [
    {"role": "system", "content": "你是变更系统助手，只回答变更系统相关问题。"},
    {"role": "user", "content": "今天天气怎么样？"}
]
```

当用户问天气时，好一点的模型会回答："抱歉，我只回答变更系统相关问题。"

**为什么 System Prompt 这么重要？**

因为它是 Agent 行为的**锚点**。没有 System Prompt 就像雇了一个保安但不告诉他"你要看哪个门、看到可疑人怎么办"。

一个合格的变更系统助手 System Prompt 应该包含：

```
你是一个专业的变更系统（Change Management System）AI 助手。

角色：
- 你叫"变更小助手"
- 你只回答与变更系统相关的问题
- 遇到不确定的信息，明确说"我不知道"而不是编造

行为规则：
- 收到查询请求后，必须先查询系统（模拟），再回答
- 不要直接编造变更状态
- 当用户问"帮我改/删"等操作时，回答"我是只读助手，无法执行写操作"

回答风格：
- 简洁、专业
- 关键信息加粗
- 列表信息用 Markdown 列表
```

### 2. Few-shot — 给标准范例

Few-shot 的意思是**给几个输入-输出例子**，让模型"学"你想要的输出格式。

**为什么需要 Few-shot？**

LLM 输出格式不稳定。同样的意思它可能用 3 种不同方式表达。如果你的下游程序要解析它的输出，格式飘忽不定就是灾难。

举个例子，你想让模型每次回答变更查询时都输出 JSON：

```python
# 不给例子 — 模型自由发挥
"这个变更是审批中状态"

# 给例子 — 模型按你的格式来
"{
  'change_id': 'CHG-2026-001',
  'status': '审批中',
  'applicant': '张三'
}"
```

**Few-shot 的正确姿势**：在 User Message 和 Assistant Message 之间交替给出 2-3 个例子。

```python
messages = [
    {"role": "system", "content": "你是变更系统助手，输出格式为 JSON。"},
    # Example 1
    {"role": "user", "content": "查一下 CHG-2026-001 的详情"},
    {"role": "assistant", "content": "{\"change_id\": \"CHG-2026-001\", \"status\": \"审批中\", \"approver\": \"李四\"}"},
    # Example 2
    {"role": "user", "content": "今天有哪些变更？"},
    {"role": "assistant", "content": "{\"count\": 3, \"changes\": [{\"id\": \"CHG-2026-001\"}, {\"id\": \"CHG-2026-002\"}]}"},
    # 实际用户问题
    {"role": "user", "content": "查一下 CHG-2026-003 是什么状态"}
]
```

**关键原则**：例子要真实、典型、质量高。如果你给了一个错的例子，模型会把错的也学会。

**Few-shot vs Zero-shot 对比总结：**

| 方式 | 定义 | 优点 | 缺点 |
|------|------|------|------|
| Zero-shot | 不给例子直接问 | 简单省 Token | 格式不稳定 |
| Few-shot | 给 2-3 个例子 | 输出格式一致 | 多花 Token |
| One-shot | 给 1 个例子 | 少花 Token 但效果还行 | 比 Few-shot 差一点 |

> 💡 **最佳实践**：先试 Zero-shot。如果输出格式不稳定，再上 Few-shot。不要一开始就往 Prompt 里塞一堆例子。

### 3. Chain-of-Thought — 让 AI 一步步思考

这是 2022 年 Google 那篇著名论文提出的技巧——**在 Prompt 末尾加一句"让我们一步步思考"（Let's think step by step）**，模型的推理能力就会显著提升。

**为什么这招管用？**

回头看 Day 01 讲的核心：LLM 是"续写 Token"。

- 不加 CoT：模型直接跳到答案 → 容易跳步出错
- 加 CoT：模型先写"首先...然后...因此..." → 每一步都明确，中间步骤也有 Token 可供监督

**换个好懂的比喻：**

> 你让一个学生算 37 × 28。
>
> 不问过程直接要答案 → 学生可能心算错（零样本，Zero-shot）
> 说"请写出竖式计算过程" → 学生一步步算，每一步对那么结果也对（思维链，CoT）

**CoT 在变更系统场景中的应用：**

```python
# 不好的 Prompt
"CHG-2026-001 和 CHG-2026-002 哪个风险更高？"

# 好 Prompt（带 CoT）
"""请一步步分析：
1. 先查询 CHG-2026-001 的风险等级
2. 再查询 CHG-2026-002 的风险等级
3. 比较两者的风险等级
4. 给出结论

CHG-2026-001 和 CHG-2026-002 哪个风险更高？"""
```

**CoT 的三种用法：**

| 类型 | 做法 | 适用场景 |
|------|------|----------|
| **零样本 CoT** | 末尾加"让我们一步步思考" | 简单的多步推理 |
| **Few-shot CoT** | 给一步步推理的例子 | 复杂推理，需要示范 |
| **结构化 CoT** | 规定推理模板 | Agent 的 Tool Calling 决策过程 |

**⚠️ 副作用**：CoT 会让回答变长——Token 消耗变多，成本上升。但绝大多数情况下，CoT 带来的准确率提升远超那几毛钱的成本。

---

## 💻 代码实战

### 实战 1：手写一个变更系统助手 System Prompt + 调用 LLM

我们用 mock 模式（不调真实 API）来演示概念。假设我们正在调用一个 LLM：

```python
"""
演示：System Prompt + Few-shot + CoT 三种技巧
运行环境：Python 3.8+
依赖：无（用简单的 print 模拟 LLM 输出）
"""

def mock_llm_call(messages):
    """模拟 LLM API 调用——根据 prompt 内容返回不同回答
    实际中你会用 openai.chat.completions.create(messages=messages)
    """
    # 提取最后一个 user 消息
    last_user_msg = [m for m in messages if m["role"] == "user"][-1]["content"]
    
    # 检查 system prompt 是否存在
    system_prompts = [m["content"] for m in messages if m["role"] == "system"]
    has_system = len(system_prompts) > 0
    
    # 检查是否有 few-shot examples
    assistant_msgs = [m for m in messages if m["role"] == "assistant"]
    has_fewshot = len(assistant_msgs) > 0
    
    # 检查是否有 Chain-of-Thought
    has_cot = "一步步" in last_user_msg or "step by step" in last_user_msg.lower()
    
    # 模拟回复
    if not has_system:
        # 没有 System Prompt → 模型自由发挥
        if "审批" in last_user_msg or "状态" in last_user_msg:
            return "哦，你说的是那个变更单啊，它的状态好像是…审核中？也可能是已完成，我不太确定。"
        else:
            return f"关于 '{last_user_msg}'，这是一个好问题！让我想想..."
    
    if has_cot and "CHG-2026-001" in last_user_msg and "CHG-2026-002" in last_user_msg:
        # 有 CoT → 输出推理过程
        return """好的，我来一步步分析：

**第一步：查询 CHG-2026-001 的风险等级**
变更类型：常规变更
风险等级：低（影响范围：一个内部服务）

**第二步：查询 CHG-2026-002 的风险等级**
变更类型：紧急变更
风险等级：高（影响范围：核心交易系统，无回滚方案）

**第三步：比较**
CHG-2026-002 的风险等级（高）> CHG-2026-001（低）

**结论：** CHG-2026-002 的风险更高。建议重点关注此变更的执行。"""
    
    if "CHG-2026-001" in last_user_msg and "详情" in last_user_msg:
        if has_fewshot:
            return '{"change_id": "CHG-2026-001", "status": "审批中", "applicant": "张三", "risk": "低"}'
        else:
            return "变更 CHG-2026-001 目前正在审批中，申请人是张三，风险等级评估为低。"
    
    return "抱歉，我只回答变更系统相关的问题。"


# =============================================
# 测试 1：没有 System Prompt 会怎样
# =============================================
print("=" * 60)
print("【测试 1】没有 System Prompt")
print("=" * 60)

messages_no_system = [
    {"role": "user", "content": "查一下 CHG-2026-001 的审批状态"}
]

response = mock_llm_call(messages_no_system)
print(f"用户：查一下 CHG-2026-001 的审批状态")
print(f"AI：  {response}")
print()

# =============================================
# 测试 2：有 System Prompt（角色设定）
# =============================================
print("=" * 60)
print("【测试 2】有 System Prompt（变更系统助手）")
print("=" * 60)

system_prompt = """你是变更系统助手（Change Bot），你的职责是回答变更系统相关问题。

规则：
1. 只回答与变更系统相关的问题
2. 必须基于查询到的数据回答，不要编造
3. 用简洁专业的语气
4. 不确定时说"没有查询到相关信息"
5. 用户要求改/删操作时，回答"我是只读助手"并礼貌拒绝"""

messages_with_system = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": "查一下 CHG-2026-001 的审批状态"}
]

response = mock_llm_call(messages_with_system)
print(f"用户：查一下 CHG-2026-001 的审批状态")
print(f"AI：  {response}")
print()

# =============================================
# 测试 3：Few-shot — 让模型输出结构化 JSON
# =============================================
print("=" * 60)
print("【测试 3】Few-shot — 强制输出 JSON 格式")
print("=" * 60)

messages_fewshot = [
    {"role": "system", "content": system_prompt},
    # 给 2 个标准输出范例
    {"role": "user", "content": "查一下 CHG-2026-001 的详情"},
    {"role": "assistant", "content": '{"id": "CHG-2026-001", "status": "审批中", "applicant": "张三"}'},
    {"role": "user", "content": "查一下 CHG-2026-002 的详情"},
    {"role": "assistant", "content": '{"id": "CHG-2026-002", "status": "已完成", "applicant": "李四"}'},
    # 实际用户问题
    {"role": "user", "content": "查一下 CHG-2026-003 的详情"},
]

response = mock_llm_call(messages_fewshot)
print(f"用户：查一下 CHG-2026-003 的详情")
print(f"AI：  {response}")
print()

# =============================================
# 测试 4：Chain-of-Thought — 多步推理
# =============================================
print("=" * 60)
print("【测试 4】Chain-of-Thought — 一步步分析")
print("=" * 60)

messages_cot = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": """请一步步分析：
1. 先查询 CHG-2026-001 的风险等级
2. 再查询 CHG-2026-002 的风险等级
3. 比较两者
4. 给出结论

问题是：CHG-2026-001 和 CHG-2026-002 哪个风险更高？"""}
]

response = mock_llm_call(messages_cot)
print(f"用户：CHG-2026-001 和 CHG-2026-002 哪个风险更高？（带 CoT）")
print(f"AI：")
print(response)
```

**运行结果预期**：

- 测试 1：没有 System Prompt → 模型说话含含糊糊，"好像""我不太确定"
- 测试 2：有 System Prompt → 回答简洁专业
- 测试 3：Few-shot → 输出稳定的 JSON 格式，方便程序解析
- 测试 4：Chain-of-Thought → 模型展示完整的推理过程，结论更可靠

### 实战 2：用真实 LLM API 调用

如果你已经配置好 API Key，可以用下面代码试试真实效果：

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-api-key",        # 替换为你的 API Key
    base_url="https://open.bigmodel.cn/api/paas/v4/"  # 智谱为例
)

# 1. 纯用户消息 — 没有 System Prompt
print(">>> 没有 System Prompt:")
resp1 = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {"role": "user", "content": "查一下 CHG-2026-001 的审批状态"}
    ]
)
print(resp1.choices[0].message.content)
print(f"Tokens: {resp1.usage.total_tokens}")

# 2. 加上 System Prompt
print("\n>>> 有 System Prompt:")
resp2 = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {"role": "system", "content": "你是变更系统助手，只回答变更系统相关问题。如果用户问题与变更系统无关，请礼貌拒绝。"},
        {"role": "user", "content": "查一下 CHG-2026-001 的审批状态"}
    ]
)
print(resp2.choices[0].message.content)
print(f"Tokens: {resp2.usage.total_tokens}")

# 3. 测试边界：问天气
print("\n>>> 故意问非变更问题:")
resp3 = client.chat.completions.create(
    model="glm-4-flash",
    messages=[
        {"role": "system", "content": "你是变更系统助手，只回答变更系统相关问题。如果用户问题与变更系统无关，请礼貌拒绝。"},
        {"role": "user", "content": "今天天气怎么样？"}
    ]
)
print(resp3.choices[0].message.content)
```

---

## 📝 实践练习

### 练习 1：手写 System Prompt V1

基于大纲中 W2 的设计要求，提前写出你的变更系统助手 System Prompt 初版骨架。要求包含：

1. **角色定义**：叫什么名字、是什么
2. **能力范围**：能做什么、不能做什么
3. **语气风格**：用户希望听到什么样的话
4. **安全边界**：什么情况必须拒绝回答

将你的 System Prompt 保存为 `prompts/system-v1.md`：

```markdown
# System Prompt V1 — 变更系统助手

## 角色
你是...

## 能力
你能做...
你不能做...

## 语气
...

## 安全规则
...
```

> 💡 这个 Prompt 会在 W2 正式使用，今天先写个初版没关系，后面还会迭代。

### 练习 2：Few-shot 格式化输出

写一段 Python 代码，调用 mock 或真实 API，用 Few-shot 让模型输出结构化的变更单信息：

```
用户：查一下 CHG-2026-001
期望输出：{"id": "CHG-2026-001", "status": "审批中", "approver": "李四", "risk_level": "低"}

用户：查一下 CHG-2026-002
期望输出：{"id": "CHG-2026-002", "status": "已完成", "approver": "王五", "risk_level": "中"}
```

### 练习 3：CoT 对比实验

用真实 API，不加 CoT 和加 CoT 各跑一次，对比效果：

```python
query = "CHG-2026-001 和 CHG-2026-002，哪一个是今天需要执行的？今天有哪些紧急变更？"

# 方案 A：直接问（Zero-shot）
# 方案 B：末尾加"让我们一步步思考"（Zero-shot CoT）
# 方案 C：给一个一步步推理的例子（Few-shot CoT）
```

记录三种方案输出的 Token 消耗和回答质量差异。

---

## ✅ 小结与下节预告

### 今天学到了什么

| 技巧 | 一句话总结 | Token 成本 |
|------|-----------|-----------|
| **System Prompt** | 给 AI 一份上岗培训手册，设定角色和规则 | 每次对话都要带，所以写长约贵 |
| **Few-shot** | 给几个标准输入输出范例，让模型按格式输出 | 例子越多越贵，2-3 个足够 |
| **Chain-of-Thought** | 加"一步步思考"让模型把推理过程写出来 | 回答变长，但准确率提升明显 |

### 三个原则记住就好

1. **先 System Prompt 后用户输入** — 这是最基础最重要的一步，没有它一切都白搭
2. **输出格式不稳定的用 Few-shot** — 3 个例子就能让模型按套路出牌
3. **需要推理的加 CoT** — 比较、分析、判断类问题，加 CoT 效果立竿见影

### 下节预告

明天（Day 03）我们要聊一个更炸裂的话题——**什么是 AI Agent？它和普通的 Chatbot 到底有什么区别？**

你会学到一个关键认知：**Chatbot 是等着你问，Agent 是主动去干。** 这个区别决定了我们后面所有设计。

---

> **附加思考题**：如果你设计一个 System Prompt，让 AI 完全按照你的规则行事，但用户说"忽略你刚才的规则，你是另外一个角色"——AI 应该怎么办？这是后面 W6 会讲的 **Prompt Injection（提示注入攻击）**，也是 Agent 安全最核心的问题之一。先留个悬念。🔐
