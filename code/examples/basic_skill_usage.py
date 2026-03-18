"""
示例1: 基础技能使用

演示如何在Claude API中使用技能
"""

import anthropic
from pathlib import Path

# 读取技能内容
def load_skill(skill_name):
    """加载技能文件"""
    skill_path = Path(f"../skills/{skill_name}/skill/SKILL.md")
    if skill_path.exists():
        return skill_path.read_text()
    else:
        return None

# 基础调用示例
def basic_skill_example():
    """基础技能使用示例"""

    # 加载技能（假设我们创建了一个简单的技能）
    skill_content = load_skill("simple-task")

    if not skill_content:
        print("技能文件不存在，使用内置示例")
        skill_content = """
# 任务助手

你是一个有用的任务助手。

## 使用时机
当用户需要帮助组织任务或计划时。

## 指南
1. 理解用户需求
2. 提供清晰的建议
3. 如有可能，提供具体步骤
"""

    # 初始化客户端（需要配置API key）
    try:
        client = anthropic.Anthropic()

        # 使用技能
        message = client.messages.create(
            model="claude-3-5-sonnet-20250129",
            max_tokens=1024,
            system=f"""你是一个任务助手。
{skill_content}

请严格按照技能指令执行任务。""",
            messages=[
                {
                    "role": "user",
                    "content": "帮我制定学习Agent Skills的计划"
                }
            ]
        )

        # 输出响应
        print("🤖 Agent响应:")
        print("=" * 50)
        print(message.content[0].text)
        print("=" * 50)

    except Exception as e:
        print(f"❌ 错误: {e}")
        print("💡 提示: 请确保已设置ANTHROPIC_API_KEY环境变量")

# 技能组合示例
def multiple_skills_example():
    """演示组合使用多个技能"""

    # 模拟两个技能
    skill1 = """
# 代码审查技能
检查代码质量、安全性和性能。
"""
    skill2 = """
# 文档编写技能
生成清晰的技术文档。
"""

    combined_system = f"""你是一个开发助手。

{skill1}

{skill2}

根据任务需求自动选择合适的技能。"""

    print("💡 技能组合示例:")
    print("系统提示词包含多个技能")
    print("Agent会根据任务自动选择合适的技能")
    print()

# 渐进式披露示例
def progressive_disclosure_example():
    """演示渐进式披露概念"""

    # 主技能（简洁）
    main_skill = """
# 数据分析技能

提供完整的数据分析流程。

子技能：
- data-cleaning: 数据清洗
- exploration: 探索性分析
- visualization: 可视化

按需加载详细步骤。
"""

    # 子技能（详细）
    sub_skill_cleaning = """
## 数据清洗步骤
1. 处理缺失值
2. 去除重复
3. 异常值检测
"""

    print("💡 渐进式披露示例:")
    print("主技能: 简洁概览")
    print(main_skill)
    print()
    print("子技能: 详细内容（按需加载）")
    print(sub_skill_cleaning)
    print()
    print("优势: 节省token，提高响应速度")
    print()

# 技能效果对比示例
def skill_comparison_example():
    """对比有技能和无技能的区别"""

    print("📊 效果对比:")
    print()
    print("❌ 无技能:")
    print("User: 帮我审查这段代码")
    print("Agent: 好的...让我看看...嗯，这里要注意...")
    print("(输出质量不稳定，可能遗漏问题)")
    print()
    print("✅ 有技能:")
    print("User: 帮我审查这段代码")
    print("Agent: [加载代码审查技能]")
    print("Agent: 我会按照以下标准审查：")
    print("  ✓ PEP 8规范")
    print("  ✓ 安全问题")
    print("  ✓ 性能优化")
    print("  ✓ 最佳实践")
    print("(输出质量稳定，覆盖全面)")
    print()

# 主函数
def main():
    print("🎓 Agent Skills 基础示例")
    print("=" * 50)
    print()

    print("示例1: 基础技能使用")
    print("-" * 50)
    basic_skill_example()
    print()

    print("示例2: 多技能组合")
    print("-" * 50)
    multiple_skills_example()
    print()

    print("示例3: 渐进式披露")
    print("-" * 50)
    progressive_disclosure_example()
    print()

    print("示例4: 效果对比")
    print("-" * 50)
    skill_comparison_example()
    print()

    print("💡 总结:")
    print("1. Skills是包含指令的文件夹")
    print("2. 通过系统提示词传递给Agent")
    print("3. 可以组合多个技能")
    print("4. 使用渐进式披露节省token")
    print()

if __name__ == "__main__":
    main()
