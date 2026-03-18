# 模块7-9: 技能集成实战

> **学习时长**: 45分钟
> **难度**: ⭐⭐⭐⭐

---

## 📌 本模块要点

- 在Claude API中使用技能
- 在Claude Code中使用技能
- 在Agent SDK中使用技能
- 三个完整实战案例

---

## 7.1 Claude API中使用技能

### 🔌 API集成基础

#### 配置环境

```bash
# 安装依赖
pip install anthropic

# 设置环境变量
export ANTHROPIC_API_KEY="your-api-key"
```

#### 基础调用

```python
import anthropic
from pathlib import Path

# 初始化客户端
client = anthropic.Anthropic()

# 读取技能内容
skill_path = Path("skills/my-skill/skill/SKILL.md")
skill_content = skill_path.read_text()

# 构建消息
message = client.messages.create(
    model="claude-3-5-sonnet-20250129",
    max_tokens=4096,
    system=f"""你是一个专业的数据分析助手。
{skill_content}

请严格按照技能中的指令执行任务。""",
    messages=[
        {
            "role": "user",
            "content": "分析sales.csv数据并生成报告"
        }
    ]
)

# 获取响应
print(message.content[0].text)
```

### 🛠️ 高级集成：代码执行工具

```python
import anthropic
import json

class SkillEnabledAgent:
    """支持技能的Agent"""

    def __init__(self, skill_paths):
        self.client = anthropic.Anthropic()
        self.skills = self._load_skills(skill_paths)
        self.tools = self._setup_tools()

    def _load_skills(self, paths):
        """加载技能文件"""
        skills = {}
        for path in paths:
            skill_name = Path(path).parent.parent.name
            with open(f"{path}/skill/SKILL.md") as f:
                skills[skill_name] = f.read()
        return skills

    def _setup_tools(self):
        """配置工具"""
        return [
            {
                "name": "read_file",
                "description": "读取文件内容",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "文件路径"
                        }
                    },
                    "required": ["path"]
                }
            },
            {
                "name": "execute_python",
                "description": "执行Python代码",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "code": {
                            "type": "string",
                            "description": "Python代码"
                        }
                    },
                    "required": ["code"]
                }
            },
            {
                "name": "write_file",
                "description": "写入文件",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "path": {"type": "string"},
                        "content": {"type": "string"}
                    },
                    "required": ["path", "content"]
                }
            }
        ]

    def run(self, task, skill_name=None):
        """执行任务"""

        # 构建系统提示
        if skill_name:
            system_prompt = f"""你是一个专业的助手。

{self.skills[skill_name]}

请严格按照技能指令执行任务。你可以使用工具来：
1. 读取文件
2. 执行Python代码进行数据分析
3. 写入结果文件
"""
        else:
            system_prompt = "你是一个有帮助的助手。"

        # 初始消息
        messages = [{"role": "user", "content": task}]

        # 对话循环
        while True:
            # 调用API
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20250129",
                max_tokens=4096,
                system=system_prompt,
                messages=messages,
                tools=self.tools
            )

            # 检查是否需要使用工具
            stop_reason = response.stop_reason

            # 添加响应到历史
            assistant_message = {
                "role": "assistant",
                "content": response.content
            }
            messages.append(assistant_message)

            if stop_reason == "tool_use":
                # 执行工具
                for block in response.content:
                    if block.type == "tool_use":
                        tool_result = self._execute_tool(block)
                        messages.append({
                            "role": "user",
                            "content": [tool_result]
                        })
            else:
                # 完成
                return response.content

    def _execute_tool(self, tool_block):
        """执行工具调用"""
        tool_name = tool_block.name
        tool_input = tool_block.input

        if tool_name == "read_file":
            with open(tool_input["path"]) as f:
                result = f.read()
            return {
                "type": "tool_result",
                "tool_use_id": tool_block.id,
                "content": result
            }

        elif tool_name == "execute_python":
            exec_globals = {}
            exec(tool_input["code"], exec_globals)
            return {
                "type": "tool_result",
                "tool_use_id": tool_block.id,
                "content": "代码执行成功"
            }

        elif tool_name == "write_file":
            with open(tool_input["path"], "w") as f:
                f.write(tool_input["content"])
            return {
                "type": "tool_result",
                "tool_use_id": tool_block.id,
                "content": f"已写入{tool_input['path']}"
            }
```

#### 实战案例：自动化数据分析

```python
# 使用Agent进行数据分析
agent = SkillEnabledAgent([
    "skills/time-series-analyzer"
])

# 分析销售数据
result = agent.run(
    task="分析sales_data.csv，生成完整报告",
    skill_name="time-series-analyzer"
)

"""
Agent会自动：
1. [读取技能] 加载time-series-analyzer技能
2. [使用工具] 读取sales_data.csv
3. [执行代码] Python进行统计分析
4. [生成报告] 按技能格式输出
5. [保存结果] 写入analysis_report.md
"""
```

---

## 7.2 Claude Code中使用技能

### 💻 技能文件位置

```bash
# 用户技能目录
~/.claude/skills/
├── my-custom-skill/
│   └── skill/SKILL.md
└── another-skill/
    └── skill/SKILL.md

# 项目级技能（推荐）
my-project/
├── .claude/
│   └── skills/
│       ├── project-reviewer/
│       └── code-generator/
├── src/
└── tests/
```

### 🎯 技能自动加载

```markdown
# Claude Code自动检测技能

当你在项目中运行Claude Code时：
1. 检查~/.claude/skills/（全局技能）
2. 检查.claude/skills/（项目技能）
3. 自动加载所有技能

使用时自然语言触发：
"使用python-reviewer技能审查这段代码"
```

### 🛠️ 子代理配置

```python
# .claude/subagents.json
{
  "subagents": {
    "security-reviewer": {
      "description": "专门进行安全审查",
      "skills": ["security-checklist", "vulnerability-scanner"],
      "isolation": "context"
    },
    "performance-analyst": {
      "description": "性能分析和优化",
      "skills": ["profiling-guidelines", "optimization-patterns"],
      "isolation": "context"
    },
    "test-generator": {
      "description": "生成单元测试",
      "skills": ["pytest-best-practices", "test-design-patterns"],
      "isolation": "context"
    }
  }
}
```

### 📋 完整工作流示例

```bash
# 场景：开发新功能

# 1. 需求分析
claude "分析user_stories.md，提取技术需求"
[自动加载 requirement-analyzer 技能]

# 2. 架构设计
claude "基于需求设计系统架构"
[自动加载 architecture-designer 技能]

# 3. 代码生成
claude "生成用户认证模块代码"
[自动加载 code-generator 技能]

# 4. 安全审查
claude "使用security-reviewer子代理审查代码"
[启动独立上下文的子代理]

# 5. 性能分析
claude "使用performance-analyst子代理检查性能"
[启动另一个独立子代理]

# 6. 测试生成
claude "使用test-generator子代理生成测试"
[第三个子代理并行工作]

# 7. 文档编写
claude "生成API文档"
[自动加载 api-documenter 技能]
```

---

## 7.3 Claude Agent SDK中使用技能

### 🤖 SDK基础

```python
from anthropic import AnthropicBedrock

# 初始化SDK客户端
client = AnthropicBedrock()

# 创建Agent
from anthropic_agent import Agent, Skill

# 加载技能
research_skill = Skill.from_directory("skills/research-methodology")

# 创建Agent
agent = Agent(
    model="claude-3-5-sonnet",
    skills=[research_skill],
    tools=[web_search, file_reader]
)
```

### 🎓 实战案例：研究Agent

```python
import anthropic
from anthropic_agent import Agent, Skill, Subagent
import asyncio

class ResearchTeam:
    """智能研究团队"""

    def __init__(self):
        # 主协调Agent
        self.coordinator = Agent(
            name="coordinator",
            skills=["project-management", "synthesis"]
        )

        # 子代理团队
        self.literature_reviewer = Subagent(
            name="literature_reviewer",
            skills=[
                Skill.from_path("skills/literature-search"),
                Skill.from_path("skills/citation-manager")
            ],
            tools=[arxiv_api, google_scholar],
            isolation="full"  # 完全隔离上下文
        )

        self.analyst = Subagent(
            name="analyst",
            skills=[
                Skill.from_path("skills/critical-analysis"),
                Skill.from_path("skills/statistical-methods")
            ],
            tools=["calculator", "statistical-tests"]
        )

        self.writer = Subagent(
            name="writer",
            skills=[
                Skill.from_path("skills/academic-writing"),
                Skill.from_path("skills/report-structure")
            ]
        )

    async def conduct_research(self, topic):
        """执行完整研究流程"""

        # 阶段1：文献检索
        print("🔍 阶段1：文献检索...")
        papers = await self.literature_reviewer.run(
            f"搜索关于'{topic}'的最新研究论文"
        )

        # 阶段2：并行分析
        print("📊 阶段2：分析...")
        analysis_tasks = [
            self.analyst.analyze_methods(papers),
            self.analyst.analyze_findings(papers),
            self.analyst.identify_gaps(papers)
        ]

        results = await asyncio.gather(*analysis_tasks)

        # 阶段3：综合报告
        print("✍️ 阶段3：撰写报告...")
        report = await self.writer.run(
            f"""基于以下分析撰写综述报告：

方法分析：{results[0]}
发现分析：{results[1]}
研究空白：{results[2]}

要求：
- 学术风格
- 包含引用
- 提出未来方向"""
        )

        return report

# 使用
async def main():
    team = ResearchTeam()
    report = await team.conduct_research(
        "Transformer在时间序列预测中的应用"
    )

    print(report)

# 运行
asyncio.run(main())
```

---

## 7.4 三平台对比

| 特性 | API | Claude Code | Agent SDK |
|------|-----|-------------|-----------|
| **适用场景** | 应用集成 | 开发工作流 | 复杂系统 |
| **复杂度** | 中 | 低 | 高 |
| **灵活性** | 高 | 中 | 很高 |
| **上下文隔离** | 手动 | 自动 | 完善 |
| **子代理** | 手动 | 配置文件 | 原生支持 |
| **工具集成** | 手动 | 自动 | 丰富 |

---

## 📝 模块7-9总结

### ✅ 核心要点

1. **API集成**
   - 直接调用Claude API
   - 手动管理技能加载
   - 自定义工具集成

2. **Claude Code**
   - 自动技能加载
   - 子代理配置
   - 开发工作流优化

3. **Agent SDK**
   - 完整Agent框架
   - 原生子代理支持
   - 并行处理能力

### 🎯 选择建议

```
简单任务 → Claude Code（自动、便捷）
应用集成 → Claude API（灵活、可控）
复杂系统 → Agent SDK（强大、完善）
```

---

**下一步**: 开始实践环节！🚀

