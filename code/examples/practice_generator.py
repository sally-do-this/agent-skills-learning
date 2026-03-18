"""
示例2: API集成 - 练习题生成器

演示如何创建一个实际的技能：从笔记自动生成练习题
"""

import anthropic
import json
from pathlib import Path

class PracticeQuestionGenerator:
    """练习题生成器"""

    def __init__(self):
        self.client = anthropic.Anthropic()
        self.skill = self._load_skill()

    def _load_skill(self):
        """加载练习题生成技能"""
        return """
# practice-question-generator

从学习材料自动生成练习题和测验。

## 使用时机

✅ 使用本技能当：
- 输入是课程笔记、教材、技术文档
- 需要生成测试题或练习题
- 目的是检验学习效果

❌ 不使用本技能当：
- 需要创作原创内容
- 输入是结构化数据

## 指令

### 生成流程

1. **内容分析**
   - 识别5-10个关键概念
   - 提取重要原理
   - 标记关键公式或代码

2. **题目生成**
   - 每个概念生成2-3题
   - 包含不同难度级别
   - 确保题型多样性

3. **输出格式**

使用以下格式：

```markdown
# [主题] 练习题

生成时间：[时间戳]
难度分布：基础 [X]% | 中级 [Y]% | 高级 [Z]%

---

## 第一部分：选择题

1. [题目]
   A. 选项1
   B. 选项2
   C. 选项3
   D. 选项4

   ✅ 答案：B
   💡 解析：[详细解释]
   📊 难度：基础

---

## 第二部分：填空题

...

---

## 第三部分：简答题

...

---

## 参考答案汇总

1. B  2. A  3. D  ...
```

### 题型分配建议

- 选择题：40-50%（检验记忆和理解）
- 填空题：20-30%（检验关键概念）
- 简答题：20-30%（检验理解和应用）
- 应用题：0-20%（如适用，检验综合能力）
"""

    def generate(self, notes, num_questions=10):
        """生成练习题"""

        # 构建请求
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20250129",
            max_tokens=4096,
            system=self.skill,
            messages=[
                {
                    "role": "user",
                    "content": f"""基于以下学习材料生成{num_questions}道练习题：

{notes}

确保：
1. 覆盖所有关键概念
2. 包含不同难度级别
3. 提供详细答案和解析
4. 使用标准输出格式"""
                }
            ]
        )

        return message.content[0].text

# 演示使用
def demo_with_sample_notes():
    """使用示例笔记生成练习题"""

    print("🎓 练习题生成器演示")
    print("=" * 60)
    print()

    # 示例笔记
    sample_notes = """
# Python装饰器教程

## 基本概念

装饰器（Decorator）是Python中用于修改函数或类行为的强大工具。
它允许你在不修改原函数代码的情况下，为函数添加额外功能。

## 工作原理

装饰器的工作原理：
1. 定义一个接受函数作为参数的函数
2. 在这个函数内部定义一个包装函数
3. 包装函数添加额外功能
4. 返回包装函数

## 基本语法

使用@符号应用装饰器：

```python
@my_decorator
def my_function():
    pass
```

这等价于：

```python
my_function = my_decorator(my_function)
```

## 常见用途

1. **日志记录**: 记录函数调用信息
2. **性能计时**: 测量函数执行时间
3. **权限验证**: 检查用户权限
4. **缓存**: 缓存函数结果
5. **重试机制**: 失败时自动重试

## 示例代码

```python
def timer_decorator(func):
    """计时装饰器"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 耗时: {end - start:.2f}秒")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(1)
    return "完成"

slow_function()  # 输出: slow_function 耗时: 1.00秒
```

## 重要概念

- **函数是一等公民**: 可以作为参数传递
- **闭包**: 内部函数可以访问外部函数的变量
- **语法糖**: @符号是简洁的语法
- **高阶函数**: 接受或返回函数的函数
"""

    print("📝 输入笔记:")
    print("-" * 60)
    print(sample_notes[:200] + "...")
    print()

    # 创建生成器
    generator = PracticeQuestionGenerator()

    # 生成练习题
    print("🤖 正在生成练习题...")
    print()

    try:
        questions = generator.generate(sample_notes, num_questions=10)

        print("✅ 生成成功!")
        print()
        print("📋 生成的练习题:")
        print("=" * 60)
        print(questions)
        print("=" * 60)

        # 保存到文件
        output_path = Path("generated_practice_questions.md")
        output_path.write_text(questions)
        print()
        print(f"💾 已保存到: {output_path}")

    except Exception as e:
        print(f"❌ 生成失败: {e}")
        print("💡 请确保已设置ANTHROPIC_API_KEY")

# 交互式版本
def interactive_mode():
    """交互式模式"""

    print("🎓 练习题生成器 - 交互模式")
    print("=" * 60)
    print()

    # 获取输入
    print("📝 请粘贴学习笔记（输入完成后按Ctrl+D）:")
    notes = []
    try:
        while True:
            line = input()
            notes.append(line)
    except EOFError:
        pass

    notes_text = "\n".join(notes)

    if not notes_text.strip():
        print("❌ 输入为空")
        return

    # 获取题目数量
    try:
        num = int(input("\n🔢 生成多少道题？(默认10): ") or "10")
    except ValueError:
        num = 10

    print()
    print("🤖 正在生成...")

    # 生成
    generator = PracticeQuestionGenerator()
    try:
        questions = generator.generate(notes_text, num_questions=num)
        print("\n✅ 生成成功!")
        print("\n" + "=" * 60)
        print(questions)
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ 错误: {e}")

# 主函数
def main():
    import sys

    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_mode()
    else:
        demo_with_sample_notes()

if __name__ == "__main__":
    main()
