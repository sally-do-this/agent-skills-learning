# Agent Skills with Anthropic - 完整学习笔记

> **课程信息**
> - **讲师**: Elie Schoppik (Anthropic技术教育负责人)
> - **平台**: DeepLearning.AI
> - **时长**: 2小时19分钟
> - **难度**: 初级
> - **课时**: 10个视频课程
> - **发布时间**: 2026年1月

---

## 📚 课程概述

### 什么是Agent Skills?

**Skills（技能）**是包含指令的文件夹，用于扩展AI Agent的能力，为Agent提供专业的按需知识。

**核心概念**：
- 📁 **技能是文件夹** - 包含markdown格式的指令文件
- 🔄 **可重用** - 一次构建，多场景部署
- 🎯 **按需加载** - Agent在需要时自动调用
- 🌐 **开放标准** - 跨平台兼容的格式

**解决的问题**：
- ❌ **传统方式**: 每次都要重复解释相同的工作流程
- ✅ **使用Skills**: 打包一次，Agent自动知道该做什么

### 为什么需要Skills?

1. **可靠性提升** - 预定义的工作流程确保一致性
2. **上下文管理** - 渐进式披露(Progressive Disclosure)节省token
3. **专业化** - 将通用Agent转变为领域专家
4. **可组合性** - 多个技能可以组合成复杂工作流

---

## 🎯 课程学习目标

完成本课程后，你将能够：

✅ **理解技能原理** - Agent Skills如何工作，何时使用
✅ **创建自定义技能** - 遵循最佳实践构建可重用技能
✅ **集成多种平台** - 在Claude.ai、Claude Code、API、SDK中使用技能
✅ **组合技术栈** - 结合MCP、子代理创建强大系统
✅ **实战应用** - 代码生成、数据分析、研究工作流

---

## 📖 课程结构概览

### 模块1: 课程介绍
- Skills的定义和价值
- 课程内容概览
- 学习路径规划

### 模块2: Skills的意义 (Part 1)
- 为什么需要Skills
- 传统提示词的局限性
- Skills如何解决这些问题

### 模块3: 从Agent角度理解Skills (Part 2)
- Agent的工作原理
- Skills如何增强Agent能力
- 实际应用场景

### 模块4: Skills vs 工具/MCP/子代理
- 不同技术的对比分析
- 何时使用哪种技术
- 组合使用策略

### 模块5: 预设Skills探索
- Anthropic官方预设技能
- Excel、PowerPoint等文档技能
- 实战演示：营销活动分析

### 模块6: 创建自定义Skills
- 技能文件夹结构
- SKILL.md文件格式
- 最佳实践和设计模式
- 案例：练习题生成器、时间序列分析

### 模块7: Claude API中使用Skills
- API集成方法
- 代码执行工具集成
- 文件系统访问配置

### 模块8: Claude Code中使用Skills
- 代码生成工作流
- 代码审查和测试
- 子代理配置

### 模块9: Claude Agent SDK中使用Skills
- 研究Agent构建
- 文档分析工作流
- GitHub仓库集成

### 模块10: 课程总结
- 核心概念回顾
- 进阶学习路径
- 实战项目建议

---

## 🔑 核心概念

### 1. 技能的结构

```
my-skill/
├── skill/              # 必需目录
│   └── SKILL.md       # 技能定义文件
├── examples/          # 可选：示例文件
├── resources/         # 可选：资源文件
└── README.md          # 可选：说明文档
```

### 2. SKILL.md 文件格式

```markdown
# 技能名称

简短描述（1-2句话）

## 使用时机

描述何时使用此技能

## 指南

[技能的具体指令]
```

### 3. 渐进式披露 (Progressive Disclosure)

**概念**：只在需要时加载相关信息，节省上下文窗口

**实现方式**：
- 📌 将大型技能拆分为多个子技能
- 📌 使用条件判断加载不同部分
- 📌 动态引用外部资源

**优势**：
- ✅ 节省token使用
- ✅ 提高响应速度
- ✅ 保持上下文清晰

---

## 💡 重要区别

### Skills vs Tools vs MCP vs Subagents

| 特性 | Skills | Tools | MCP | Subagents |
|------|--------|-------|-----|-----------|
| **本质** | 指令文件夹 | 函数调用 | 协议标准 | 独立Agent |
| **用途** | 知识传递 | 数据获取 | 外部集成 | 任务委派 |
| **复杂度** | 低 | 中 | 高 | 高 |
| **上下文** | 共享 | 隔离 | 隔离 | 隔离 |
| **持久性** | 持久 | 临时 | 临时 | 会话级 |

**何时使用**：
- 🎯 **Skills**: 传递专业知识、工作流程
- 🔧 **Tools**: 获取实时数据（天气、股票等）
- 🌐 **MCP**: 集成外部系统（数据库、API）
- 🤖 **Subagents**: 需要隔离上下文的复杂任务

---

## 🚀 典型应用场景

### 1. 代码生成和审查
```python
# 技能：Python最佳实践
- 代码风格指南
- 性能优化模式
- 安全检查清单
```

### 2. 数据分析工作流
```python
# 技能：数据分析标准流程
- 数据清洗步骤
- 探索性分析模板
- 可视化最佳实践
```

### 3. 研究Agent
```python
# 技能：学术研究方法
- 文献搜索策略
- 信息提取框架
- 综述写作指南
```

### 4. 文档处理
```python
# 技能：技术文档标准
- API文档规范
- 代码注释风格
- README模板
```

---

## 📋 学习前准备

### 环境要求

**必需**：
- ✅ Claude API Key
- ✅ Python 3.8+
- ✅ 基础编程知识

**推荐**：
- ✅ Claude Code CLI
- ✅ Git基础操作
- ✅ Markdown语法熟悉

### 账号设置

1. **获取Claude API Key**
   - 访问: https://console.anthropic.com/
   - 创建API密钥
   - 保存到环境变量

2. **安装Claude Code** (可选)
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```

3. **Python环境配置**
   ```bash
   pip install anthropic
   pip install python-dotenv
   ```

---

## 📊 学习路径建议

### 路径A: 快速上手 (1天)
- 模块1-2: 理解基本概念
- 模块5: 使用预设技能
- 模块6: 创建第一个自定义技能

### 路径B: 系统学习 (3-5天)
- 按顺序学习所有模块
- 完成每个模块的练习
- 构建完整项目案例

### 路径C: 深度实践 (1-2周)
- 系统学习 + 全部练习
- 创建3个以上自定义技能
- 集成到实际工作流
- 构建技能库

---

## 🎓 学习建议

### 有效学习策略

1. **理论结合实践**
   - 先理解概念
   - 立即动手实验
   - 修改参数观察效果

2. **渐进式掌握**
   - 从简单技能开始
   - 逐步增加复杂度
   - 记录问题和解决方案

3. **构建项目**
   - 选择实际问题
   - 应用所学技能
   - 迭代改进

### 常见陷阱

❌ **避免**：
- 只看不练
- 一次性创建复杂技能
- 忽略错误处理
- 不写测试

✅ **应该**：
- 每个概念都实验
- 拆分为小模块
- 完善异常处理
- 自动化测试

---

## 📚 扩展资源

### 官方资源
- [Claude Documentation](https://docs.anthropic.com/)
- [Skills Open Standard](https://docs.anthropic.com/docs/skills)
- [Anthropic Cookbook](https://github.com/anthropics/cookbook)

### 社区资源
- [DataWhale中文翻译](https://github.com/datawhalechina/agent-skills-with-anthropic)
- [Claude Agent SDK](https://github.com/anthropics/agent-sdk)
- [MCP Protocol](https://modelcontextprotocol.io/)

### 相关课程
- Building Agentic RAG with LangChain
- AI Agentic Design Patterns
- Prompt Engineering for Developers

---

## 🔗 参考资料来源

- [DeepLearning.AI - Agent Skills with Anthropic](https://www.deeplearning.ai/short-courses/agent-skills-with-anthropic/)
- [DataWhale GitHub仓库](https://github.com/datawhalechina/agent-skills-with-anthropic)
- [Anthropic官方文档](https://docs.anthropic.com/)

---

**下一步**: 开始学习模块1 - 课程介绍 🚀
