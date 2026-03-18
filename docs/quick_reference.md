# Agent Skills 快速参考指南

> **快速查找常用概念和代码**

---

## 📁 技能结构速查

### 标准结构

```bash
skill-name/
├── skill/
│   └── SKILL.md          # 必需
├── examples/             # 推荐
├── resources/            # 可选
└── README.md             # 推荐
```

### SKILL.md 模板

```markdown
# [技能名称]

[一句话描述]

## 使用时机

✅ 使用当：[条件]
❌ 不使用当：[条件]

## 指令

[详细的操作步骤]

## 示例

[输入输出示例]
```

---

## 🎯 技术对比速查表

| 技术 | 本质 | 用途 | 复杂度 | 何时使用 |
|------|------|------|--------|----------|
| **Skills** | 指令文件夹 | 知识传递 | ⭐ | 工作流程标准化 |
| **Tools** | 函数调用 | 数据获取 | ⭐⭐ | 实时数据访问 |
| **MCP** | 通信协议 | 系统连接 | ⭐⭐⭐ | 外部系统集成 |
| **Subagents** | 独立Agent | 任务委派 | ⭐⭐⭐⭐ | 复杂任务处理 |

### 决策流程

```
需要扩展Agent能力
    ↓
传递工作流程？→ 是 → Skills
    ↓ 否
获取实时数据？→ 是 → 需要持久连接？
                    ├─ 是 → MCP
                    └─ 否 → Tools
    ↓ 否
需要独立上下文？→ 是 → Subagents
    ↓ 否
组合多种技术
```

---

## 💻 代码速查

### Claude API中使用技能

```python
import anthropic

# 加载技能
with open("skills/my-skill/skill/SKILL.md") as f:
    skill_content = f.read()

# 调用API
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-3-5-sonnet-20250129",
    max_tokens=4096,
    system=f"""你是一个助手。

{skill_content}

请严格按照技能指令执行。""",
    messages=[{
        "role": "user",
        "content": "你的任务"
    }]
)

print(message.content[0].text)
```

### Claude Code中使用技能

```bash
# 技能自动加载位置
~/.claude/skills/           # 全局技能
.claude/skills/             # 项目技能

# 使用
claude "使用my-skill技能处理这个任务"
```

### Agent SDK中使用技能

```python
from anthropic_agent import Agent, Skill

# 加载技能
skill = Skill.from_path("skills/my-skill")

# 创建Agent
agent = Agent(
    model="claude-3-5-sonnet",
    skills=[skill]
)

# 运行
result = agent.run("任务描述")
```

---

## 🎨 设计模式速查

### 模式1: 主从式

```bash
main-skill/
├── skill/SKILL.md         # 协调器
└── sub-skills/
    ├── task1.md
    └── task2.md
```

**SKILL.md**:
```markdown
# 主技能

本技能协调子任务。

## 指令

{{include: sub-skills/task1.md}}
{{include: sub-skills/task2.md}}
```

### 模式2: 渐进式披露

```markdown
# 主技能（简洁）

本技能提供完整分析流程。

子技能：
- cleaning: 数据清洗
- analysis: 统计分析
- visualization: 可视化

按需加载详细内容。
```

### 模式3: 工具箱式

```bash
toolbox-skill/
├── skill/SKILL.md         # 工具索引
└── tools/
    ├── tool1.md
    └── tool2.md
```

---

## 📋 编写清单

### 创建技能前

- [ ] 明确技能目标
- [ ] 识别使用场景
- [ ] 设计文件夹结构
- [ ] 规划子技能（如需要）

### 编写SKILL.md时

- [ ] 清晰的技能名称
- [ ] 一句话描述
- [ ] 明确的使用时机
- [ ] 具体的操作步骤
- [ ] 详细的示例
- [ ] 边界情况处理

### 完成技能后

- [ ] 在Claude.ai中测试
- [ ] 测试不同输入
- [ ] 优化输出格式
- [ ] 编写README
- [ ] 添加示例文件

---

## 🔧 常用命令

### 环境配置

```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install anthropic pandas numpy matplotlib

# 设置API密钥
export ANTHROPIC_API_KEY="your-key"
```

### 技能管理

```bash
# 查看全局技能
ls ~/.claude/skills/

# 查看项目技能
ls .claude/skills/

# 复制技能到全局
cp -r my-skill ~/.claude/skills/

# 测试技能
claude "使用my-skill技能"
```

### 运行示例

```bash
# 基础示例
python code/examples/basic_skill_usage.py

# 练习题生成器
python code/examples/practice_generator.py

# 交互模式
python code/examples/practice_generator.py --interactive
```

---

## 📊 技能评估标准

### 质量检查

| 维度 | 标准 | 评分 |
|------|------|------|
| **清晰度** | 使用时机明确 | ⭐⭐⭐⭐⭐ |
| **完整性** | 包含所有部分 | ⭐⭐⭐⭐⭐ |
| **具体性** | 步骤可操作 | ⭐⭐⭐⭐⭐ |
| **示例** | 有输入输出 | ⭐⭐⭐⭐⭐ |
| **测试** | 经过测试 | ⭐⭐⭐⭐⭐ |

### 性能指标

- ✅ Token效率: <2000 tokens（主技能）
- ✅ 响应时间: <5秒
- ✅ 准确率: >90%
- ✅ 一致性: >95%

---

## 🐛 常见问题

### Q1: 技能没有被加载？

```bash
# 检查技能位置
ls ~/.claude/skills/your-skill/

# 检查文件名
ls ~/.claude/skills/your-skill/skill/SKILL.md

# 重启Claude Code
```

### Q2: 技能输出质量不稳定？

- ✅ 检查指令是否清晰
- ✅ 添加更多示例
- ✅ 明确输出格式
- ✅ 处理边界情况

### Q3: Token使用过多？

- ✅ 使用渐进式披露
- ✅ 拆分为子技能
- ✅ 移除冗余内容
- ✅ 精简示例

### Q4: API调用失败？

```python
# 检查API密钥
import os
print(os.getenv("ANTHROPIC_API_KEY"))

# 检查网络连接
ping api.anthropic.com

# 检查权限
# 确保密钥有足够权限
```

---

## 📚 资源链接

### 官方文档
- [Claude Documentation](https://docs.anthropic.com/)
- [Skills Open Standard](https://docs.anthropic.com/docs/skills)
- [API Reference](https://docs.anthropic.com/api/getting-started)

### 学习资源
- [DeepLearning.AI Course](https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/)
- [DataWhale中文翻译](https://github.com/datawhalechina/agent-skills-with-anthropic)
- [Anthropic Cookbook](https://github.com/anthropics/cookbook)

### 工具和库
- [Claude Agent SDK](https://github.com/anthropics/agent-sdk)
- [MCP Protocol](https://modelcontextprotocol.io/)
- [Python anthropic包](https://github.com/anthropics/anthropic-sdk-python)

---

## 💡 最佳实践

### 技能设计

1. **单一职责**: 一个技能做一件事
2. **渐进式披露**: 主技能简洁，子技能详细
3. **明确时机**: 清楚说明何时使用
4. **包含示例**: 提供输入输出示例
5. **版本控制**: 使用Git管理技能

### 性能优化

1. **控制大小**: 主技能<2000 tokens
2. **按需加载**: 子技能按需引用
3. **缓存结果**: 避免重复计算
4. **并行处理**: 多个子代理并行

### 错误处理

1. **验证输入**: 检查输入格式
2. **友好提示**: 清晰的错误信息
3. **降级处理**: 提供备选方案
4. **日志记录**: 记录错误日志

---

## 🎯 学习检查点

### 初级 (完成✅)
- [ ] 理解什么是Skills
- [ ] 能使用预设技能
- [ ] 创建了第一个技能
- [ ] 理解技能结构

### 中级 (完成✅)
- [ ] 创建了多个技能
- [ ] 使用子技能
- [ ] 在API中集成技能
- [ ] 理解渐进式披露

### 高级 (完成✅)
- [ ] 构建完整应用
- [ ] 组合多种技术
- [ ] 优化性能
- [ ] 生产部署

---

**保持实践，持续进步！** 🚀
