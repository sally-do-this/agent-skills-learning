# 模块4: 技能对比 - Skills vs Tools vs MCP vs Subagents

> **学习时长**: 15分钟
> **难度**: ⭐⭐⭐

---

## 📌 本模块要点

- 四种技术的本质区别
- 各自的优势和局限
- 选择决策树
- 组合使用策略

---

## 4.1 技术对比总览

### 🔄 四种技术的关系

```
Agent能力增强生态系统
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Skills (技能)
  ↓ 传递知识
  ├─→ Tools (工具)
  │    ↓ 获取数据
  │    └─→ MCP (协议)
  │         ↓ 连接系统
  │         └─→ Subagents (子代理)
  └─→ (独立使用)
```

### 📊 快速对比表

| 维度 | Skills | Tools | MCP | Subagents |
|------|--------|-------|-----|-----------|
| **本质** | 指令文件夹 | 函数调用 | 通信协议 | 独立Agent |
| **目的** | 传递知识 | 获取数据 | 连接系统 | 委派任务 |
| **复杂度** | ⭐ 低 | ⭐⭐ 中 | ⭐⭐⭐ 高 | ⭐⭐⭐⭐ 很高 |
| **上下文** | 共享 | 隔离 | 隔离 | 完全隔离 |
| **持久性** | 持久存在 | 临时调用 | 会话级 | 会话级 |
| **状态** | 无状态 | 无状态 | 有状态 | 有状态 |
| **适用场景** | 工作流程 | 实时数据 | 外部系统 | 复杂任务 |
| **典型例子** | 代码审查技能 | 天气API | 数据库连接 | 研究子代理 |

---

## 4.2 Skills - 深度解析

### 🎯 核心特征

**定义**：包含指令的文件夹，传递知识和工作流程

```python
# Skills的本质
Skill = {
    "形式": "文件夹 + Markdown",
    "内容": "指令、示例、最佳实践",
    "加载": "按需加载到上下文",
    "作用": "指导Agent如何思考和行动"
}
```

### ✅ 优势

1. **知识传递**
   ```python
   # 传递复杂的工作流程
   skill/code-review/
   ├── SKILL.md           # 审查流程
   ├── examples/          # 示例代码
   └── checklists/        # 检查清单

   # Agent"学会"了如何审查代码
   ```

2. **高复用性**
   ```python
   # 一次创建，到处使用
   skills/python-best-practices/
   ├─→ Claude.ai
   ├─→ Claude Code
   ├─→ Claude API
   └─→ Agent SDK
   ```

3. **渐进式披露**
   ```python
   # 节省上下文
   主技能: 引用子技能
   子技能: 按需加载详细内容
   ```

4. **版本控制**
   ```bash
   # 作为代码管理
   git clone skills-repo
   git pull  # 获取更新
   ```

### ❌ 局限

1. **无执行能力**
   ```python
   # Skills只能提供指令
   # 不能直接执行操作
   ❌ skill.send_email()  # 错误！
   ✅ # 使用email-sender工具
   ```

2. **无实时数据**
   ```python
   # Skills是静态的
   ❌ 技能无法获取实时天气
   ✅ # 需要使用weather-api工具
   ```

3. **上下文共享**
   ```python
   # Skills在主上下文中运行
   # 大技能可能占用大量token
   ```

### 🎯 最佳使用场景

```python
# ✅ 适合使用Skills的场景

1. 工作流程标准化
   - 代码审查流程
   - 数据分析步骤
   - 文档编写规范

2. 最佳实践传递
   - Python代码风格
   - 安全检查清单
   - 设计模式指南

3. 领域专业知识
   - 法律文档分析
   - 医疗诊断流程
   - 金融风险评估

4. 复杂指令集
   - 多步骤任务
   - 决策树
   - 条件逻辑
```

---

## 4.3 Tools - 深度解析

### 🎯 核心特征

**定义**：可调用的函数，用于获取数据或执行操作

```python
# Tools的本质
Tool = {
    "形式": "函数/API",
    "输入": "结构化参数",
    "输出": "结构化结果",
    "作用": "扩展Agent的能力边界"
}
```

### 示例：天气工具

```python
# 定义工具
def get_weather(location: str, date: str) -> dict:
    """
    获取指定地点和日期的天气

    Args:
        location: 城市名称
        date: 日期 (YYYY-MM-DD)

    Returns:
        {
            "temperature": 25,
            "condition": "sunny",
            "humidity": 60
        }
    """
    # 调用天气API
    return weather_api.get(location, date)

# Agent使用工具
agent = Agent(tools=[get_weather])

user: "明天北京天气怎么样？"
agent: "[调用 get_weather('北京', '2024-01-19')]"
agent: "明天北京晴朗，温度25°C，湿度60%"
```

### ✅ 优势

1. **实时数据访问**
   ```python
   tools = [
       get_stock_price,    # 实时股票
       get_weather,        # 实时天气
       get_news            # 实时新闻
   ]
   ```

2. **外部系统交互**
   ```python
   tools = [
       send_email,         # 发送邮件
       query_database,     # 查询数据库
       call_api           # 调用API
   ]
   ```

3. **精确控制**
   ```python
   # 确定的输入输出
   result = tool.execute(parameters)
   # 不会产生幻觉或误解
   ```

4. **安全性**
   ```python
   # 工具权限可控
   tools = [
       safe_tool_1,       # 只读
       safe_tool_2        # 受限操作
   ]
   # 不给危险工具
   ```

### ❌ 局限

1. **需要预定义**
   ```python
   # 必须预先实现
   def custom_tool(param):
       # 需要编写代码
       pass
   ```

2. **有限的灵活性**
   ```python
   # 工具行为固定
   def calculate_tax(income):
       # 固定的计算逻辑
       return income * 0.2
   # 无法根据情况调整
   ```

3. **无上下文理解**
   ```python
   # 工具不"理解"任务
   # 只是机械执行
   ```

### 🎯 最佳使用场景

```python
# ✅ 适合使用Tools的场景

1. 实时数据获取
   - 天气查询
   - 股票价格
   - 汇率转换

2. 外部系统集成
   - 数据库查询
   - API调用
   - 文件操作

3. 确定性操作
   - 数学计算
   - 数据格式转换
   - 加密/解密

4. 安全执行
   - 受限的文件访问
   - 控制的网络请求
   - 审计的操作
```

---

## 4.4 MCP - Model Context Protocol

### 🎯 核心特征

**定义**：标准化协议，连接AI模型与外部数据源

```python
# MCP的本质
MCP = {
    "形式": "通信协议",
    "目的": "统一数据访问",
    "组件": ["Client", "Server", "Host"],
    "作用": "建立AI与系统的桥梁"
}
```

### 架构示例

```
┌─────────────────────────────────────────┐
│         MCP生态系统                      │
├─────────────────────────────────────────┤
│                                         │
│  ┌──────────┐      ┌──────────┐        │
│  │   AI     │◄────┤  MCP     │        │
│  │  Agent   │      │ Client  │        │
│  └──────────┘      └────┬─────┘        │
│                          │              │
│                   ┌──────┴──────┐       │
│                   │   MCP       │       │
│                   │  Protocol   │       │
│                   └──────┬──────┘       │
│                          │              │
│      ┌────────────────────┼────────┐   │
│      │                    │        │   │
│  ┌───┴────┐         ┌─────┴───┐ ┌─┴────┐
│  │   DB   │         │   API   │ │ File │
│  │ Server │         │ Server  │ │ Server│
│  └────────┘         └─────────┘ └──────┘
│                                         │
└─────────────────────────────────────────┘
```

### 代码示例

```python
# MCP客户端使用
from mcp import Client

# 连接到MCP服务器
client = Client(
    server_url="mcp://database-server"
)

# Agent通过MCP访问数据
agent = Agent(
    mcp_clients=[
        client.connect("postgres-db"),
        client.connect("redis-cache"),
        client.connect("api-gateway")
    ]
)

# 查询变得简单
user: "查询用户张三的订单历史"
agent: "[通过MCP查询postgres-db]"
agent: "找到12个订单，总金额￥5,680..."
```

### ✅ 优势

1. **标准化接口**
   ```python
   # 统一的访问方式
   for data_source in mcp_clients:
       data = data_source.query(query)
   # 无论底层是什么
   ```

2. **丰富的生态**
   ```python
   # 预构建的MCP服务器
   mcp_servers = [
       "postgres",
       "mysql",
       "mongodb",
       "redis",
       "slack",
       "github",
       "google-drive"
   ]
   ```

3. **类型安全**
   ```python
   # 强类型定义
   @mcp.resource("get-user")
   def get_user(id: int) -> User:
       # IDE支持
       # 类型检查
       pass
   ```

4. **状态管理**
   ```python
   # MCP服务器维护状态
   session.start()
   data = session.query("...")
   more_data = session.query("...")  # 保持连接
   session.close()
   ```

### ❌ 局限

1. **学习曲线**
   ```python
   # 需要理解MCP概念
   # Client-Host-Server架构
   # 协议规范
   ```

2. **基础设施要求**
   ```python
   # 需要运行MCP服务器
   # 需要网络连接
   # 需要配置管理
   ```

3. **延迟**
   ```python
   # 网络往返
   result = mcp_call()  # 可能慢
   # 本地工具可能更快
   ```

### 🎯 最佳使用场景

```python
# ✅ 适合使用MCP的场景

1. 数据库集成
   - PostgreSQL
   - MySQL
   - MongoDB

2. 云服务连接
   - AWS S3
   - Google Drive
   - Slack

3. 企业系统
   - 内部API
   - CRM系统
   - ERP系统

4. 复杂状态管理
   - 长连接会话
   - 事务管理
   - 流式处理
```

---

## 4.5 Subagents - 子代理

### 🎯 核心特征

**定义**：具有独立上下文的独立Agent实例

```python
# Subagents的本质
Subagent = {
    "形式": "独立Agent实例",
    "上下文": "完全隔离",
    "能力": "独立思考和行动",
    "作用": "处理复杂子任务"
}
```

### 架构示例

```python
# 主Agent创建子代理
class MainAgent:
    def __init__(self):
        self.skills = Skills()
        self.tools = Tools()

    def process_complex_task(self, task):
        # 分配给子代理
        if task.type == "research":
            subagent = self.create_subagent(
                name="researcher",
                skills=["literature-search", "analysis"],
                isolated_context=True
            )
            return subagent.execute(task)

# 子代理独立工作
researcher = Subagent(
    skills=["paper-analyzer", "citation-manager"],
    memory=IsolatedMemory(),  # 独立记忆
    tools=[arxiv_api, google_scholar]
)

# 子代理有独立的思考过程
result = researcher.think_and_act(research_task)
```

### ✅ 优势

1. **上下文隔离**
   ```python
   # 子代理不污染主上下文
   main_agent_context = "主要任务..."
   subagent_context = "子任务..."  # 完全独立

   # 主Agent只看到最终结果
   result = subagent.execute()
   # 不受子代理思考过程影响
   ```

2. **并行处理**
   ```python
   # 多个子代理并行工作
   subagents = [
       create_subagent("data-analyst"),
       create_subagent("visualization"),
       create_subagent("report-writer")
   ]

   results = Parallel.run([
       s.analyze(data),
       s.visualize(data),
       s.write_report(data)
   ])
   ```

3. **专业化**
   ```python
   # 每个子代理是专家
   code_expert = Subagent(
       skills=["python", "javascript", "code-review"]
   )

   security_expert = Subagent(
       skills=["security-audit", "penetration-testing"]
   )

   ml_expert = Subagent(
       skills=["ml-models", "data-preprocessing"]
   )
   ```

4. **复杂决策**
   ```python
   # 子代理可以自主决策
   planner = Subagent(
       role="planner",
       autonomy=HIGH  # 高自主性
   )

   # planner会自己规划、执行、调整
   plan = planner.create_plan(goal)
   ```

### ❌ 局限

1. **资源消耗**
   ```python
   # 每个子代理消耗token
   # 多个子代理 = 多倍消耗
   ```

2. **协调复杂**
   ```python
   # 需要管理子代理间通信
   # 避免冲突
   # 合并结果
   ```

3. **调试困难**
   ```python
   # 黑盒决策过程
   # 难以追踪错误
   ```

### 🎯 最佳使用场景

```python
# ✅ 适合使用Subagents的场景

1. 复杂研究任务
   - 文献综述
   - 多源信息整合
   - 深度分析

2. 并行处理
   - 同时处理多个文件
   - 分布式任务
   - 批量分析

3. 隔离需求
   - 敏感数据处理
   - 独立实验
   - 沙箱环境

4. 长链任务
   - 多步骤工作流
   - 需要中间状态
   - 迭代优化
```

---

## 4.6 选择决策树

### 🌳 决策流程

```
开始：需要扩展Agent能力
    ↓
    ├─ 需要传递工作流程/知识？
    │   ├─ 是 → 使用 Skills
    │   └─ 否 → 继续
    │
    ├─ 需要获取实时数据？
    │   ├─ 是 → 需要持久连接？
    │   │   ├─ 是 → 使用 MCP
    │   │   └─ 否 → 使用 Tools
    │   └─ 否 → 继续
    │
    ├─ 需要独立上下文？
    │   ├─ 是 → 使用 Subagents
    │   └─ 否 → 继续
    │
    └─ 需要组合多种能力？
        └─ 使用 组合策略
```

### 📋 快速参考

```
场景：代码审查
- 传递审查流程 → Skills ✅
- 执行代码测试 → Tools ✅
- 查询Git历史 → MCP ✅
- 隔离环境运行 → Subagents ✅

场景：数据分析
- 标准化流程 → Skills ✅
- 查询数据库 → MCP ✅
- 实时计算 → Tools ✅
- 并行处理 → Subagents ✅
```

---

## 4.7 组合使用策略

### 🔄 组合模式1: Skills + Tools

```python
# 示例：智能数据分析

agent = Agent(
    skills=[
        "data-analysis-workflow",  # 分析流程
        "statistical-tests"        # 统计方法
    ],
    tools=[
        "query_database",          # 数据获取
        "calculate_statistics"     # 统计计算
    ]
)

# 工作流
def analyze(table_name):
    # 1. Skills提供流程指导
    workflow = agent.load_skill("data-analysis-workflow")

    # 2. Tools获取数据
    data = agent.use_tool("query_database", table_name)

    # 3. Skills指导分析
    analysis = agent.apply_skill("statistical-tests", data)

    # 4. Tools执行计算
    stats = agent.use_tool("calculate_statistics", data)

    return agent.synthesize(analysis, stats)
```

### 🔄 组合模式2: Skills + MCP

```python
# 示例：企业系统集成

agent = Agent(
    skills=[
        "report-generator",      # 报告生成流程
        "data-visualization"     # 可视化最佳实践
    ],
    mcp_clients=[
        connect_postgres(),      # 数据库
        connect_slack(),         # 消息系统
        connect_google_drive()   # 文件系统
    ]
)

# 工作流
def generate_monthly_report():
    # 1. MCP获取数据
    sales_data = agent.mcp.postgres.query("SELECT * FROM sales")
    team_notes = agent.mcp.slack.get_messages()

    # 2. Skills指导报告生成
    report_structure = agent.load_skill("report-generator")

    # 3. Skills指导可视化
    charts = agent.apply_skill("data-visualization", sales_data)

    # 4. MCP保存报告
    agent.mcp.drive.save(report)

    return report
```

### 🔄 组合模式3: Skills + Subagents

```python
# 示例：研究项目

class ResearchTeam:
    def __init__(self):
        # 主Agent
        self.coordinator = Agent(
            skills=["project-management", "synthesis"]
        )

        # 子代理团队
        self.researchers = [
            Subagent(
                name="literature-reviewer",
                skills=["paper-analysis", "citation-manager"]
            ),
            Subagent(
                name="experimental-designer",
                skills=["experiment-planning", "statistics"]
            ),
            Subagent(
                name="data-analyst",
                skills=["data-processing", "visualization"]
            )
        ]

    def conduct_research(self, topic):
        # 协调器分配任务
        tasks = self.coordinator.plan_research(topic)

        # 并行执行
        results = Parallel.run([
            self.researchers[0].review_literature(topic),
            self.researchers[1].design_experiment(topic),
            self.researchers[2].prepare_analysis(topic)
        ])

        # 综合结果
        final_report = self.coordinator.synthesize(results)

        return final_report
```

### 🔄 组合模式4: 全栈组合

```python
# 示例：完整的代码审查系统

class CodeReviewSystem:
    def __init__(self):
        self.agent = Agent(
            # Skills: 传递知识和流程
            skills=[
                "security-checklist",
                "performance-guidelines",
                "code-style-standards"
            ],

            # Tools: 执行具体操作
            tools=[
                "run_tests",
                "measure_coverage",
                "check_complexity"
            ],

            # MCP: 连接外部系统
            mcp_clients=[
                connect_github(),      # 代码仓库
                connect_jira(),        # Issue跟踪
                connect_sonarqube()    # 质量分析
            ],

            # Subagents: 处理子任务
            subagents={
                "security": Subagent(
                    skills=["vulnerability-scanner"],
                    tools=["static-analysis"]
                ),
                "performance": Subagent(
                    skills=["profiling-guidelines"],
                    tools=["benchmark"]
                )
            }
        )

    def review_pull_request(self, pr_url):
        # 1. MCP获取代码
        code = self.agent.mcp.github.get_pr_code(pr_url)

        # 2. 并行子代理审查
        security_report = self.agent.subagents["security"].audit(code)
        performance_report = self.agent.subagents["performance"].check(code)

        # 3. Tools测试代码
        test_results = self.agent.tools.run_tests(code)
        coverage = self.agent.tools.measure_coverage(code)

        # 4. Skills综合评估
        review = self.agent.apply_skills(
            code=code,
            security=security_report,
            performance=performance_report,
            tests=test_results,
            coverage=coverage
        )

        # 5. MCP发布评论
        self.agent.mcp.github.post_review_comment(pr_url, review)

        return review
```

---

## 4.8 实战对比案例

### 📊 案例：营销数据分析

#### 方案1: 仅使用Skills

```python
agent = Agent(skills=["marketing-analysis"])

# 分析Excel文件
result = agent.analyze(marketing_data.xlsx)

"""
结果：
✅ 标准化的分析流程
✅ 一致的分析方法
❌ 无法获取实时数据
❌ 手动操作复杂
"""
```

#### 方案2: Skills + Tools

```python
agent = Agent(
    skills=["marketing-analysis"],
    tools=["calculate_roi", "forecast_trends"]
)

result = agent.analyze(marketing_data.xlsx)

"""
结果：
✅ 标准化流程
✅ 自动计算ROI
✅ 趋势预测
❌ 仍需手动上传文件
"""
```

#### 方案3: Skills + MCP

```python
agent = Agent(
    skills=["marketing-analysis"],
    mcp_clients=[connect_marketing_db()]
)

# 直接查询数据库
result = agent.analyze("SELECT * FROM campaigns WHERE date > '2024-01-01'")

"""
结果：
✅ 直接访问数据库
✅ 实时数据
✅ 标准化分析
✅ 完全自动化
"""
```

#### 方案4: 全栈组合

```python
agent = Agent(
    skills=["marketing-analysis"],
    mcp_clients=[
        connect_marketing_db(),
        connect_google_analytics(),
        connect_ads_platform()
    ],
    subagents=[
        Subagent("competitor-analyst"),
        Subagent("trend-forecaster")
    ]
)

# 完整的营销智能系统
report = agent.generate_comprehensive_report()

"""
结果：
✅ 多数据源整合
✅ 并行分析
✅ 竞争对手对比
✅ 趋势预测
✅ 自动生成报告
✅ 保存到云端
"""
```

---

## 📝 模块4总结

### ✅ 核心要点

1. **四种技术各有专长**
   - Skills: 知识传递
   - Tools: 数据获取
   - MCP: 系统连接
   - Subagents: 任务委派

2. **选择标准**
   - 传递工作流 → Skills
   - 实时数据 → Tools/MCP
   - 外部系统 → MCP
   - 复杂任务 → Subagents

3. **组合策略**
   - 大多数场景需要组合使用
   - 技能提供"大脑"（知识）
   - 工具提供"手脚"（能力）
   - MCP提供"连接"（桥梁）
   - 子代理提供"团队"（协作）

### 🎯 下一步

**进入模块5**: 探索预设技能
- Anthropic官方技能库
- Excel、PowerPoint等文档技能
- 实战案例演示

---

**💡 实践思考**：
1. 你当前的工作流中哪些地方适合用Skills？
2. 是否需要集成外部系统？（考虑MCP）
3. 是否有可以并行处理的任务？（考虑Subagents）
4. 如何组合这些技术构建最佳方案？
