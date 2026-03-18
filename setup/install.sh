#!/bin/bash

# Agent Skills 学习环境配置脚本
# 运行此脚本自动配置所有必需的环境

set -e  # 遇到错误立即退出

echo "🚀 开始配置Agent Skills学习环境..."
echo ""

# 颜色定义
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 检查Python
echo -e "${YELLOW}检查Python...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ 已安装Python: $PYTHON_VERSION${NC}"
else
    echo -e "${YELLOW}⚠ 未找到Python，正在安装...${NC}"
    # macOS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        if command -v brew &> /dev/null; then
            brew install python3
        else
            echo "请先安装Homebrew: https://brew.sh/"
            exit 1
        fi
    fi
fi

# 创建虚拟环境
echo ""
echo -e "${YELLOW}创建Python虚拟环境...${NC}"
cd ~/agent-skills-learning
python3 -m venv venv
source venv/bin/activate
echo -e "${GREEN}✓ 虚拟环境已创建${NC}"

# 安装依赖
echo ""
echo -e "${YELLOW}安装Python依赖包...${NC}"
pip install --upgrade pip > /dev/null 2>&1

pip install anthropic > /dev/null 2>&1
echo -e "${GREEN}✓ anthropic${NC}"

pip install python-dotenv > /dev/null 2>&1
echo -e "${GREEN}✓ python-dotenv${NC}"

pip install pandas > /dev/null 2>&1
echo -e "${GREEN}✓ pandas${NC}"

pip install numpy > /dev/null 2>&1
echo -e "${GREEN}✓ numpy${NC}"

pip install matplotlib > /dev/null 2>&1
echo -e "${GREEN}✓ matplotlib${NC}"

pip install openpyxl > /dev/null 2>&1
echo -e "${GREEN}✓ openpyxl (Excel支持)${NC}"

pip install jupyter > /dev/null 2>&1
echo -e "${GREEN}✓ jupyter${NC}"

# 创建环境变量模板
echo ""
echo -e "${YELLOW}创建环境配置文件...${NC}"
cat > .env.example << 'EOF'
# Anthropic API配置
ANTHROPIC_API_KEY=your-api-key-here

# 可选：其他配置
CLAUDE_MODEL=claude-3-5-sonnet-20250129
EOF
echo -e "${GREEN}✓ 已创建.env.example${NC}"

# 检查API key
if [ ! -f .env ]; then
    echo ""
    echo -e "${YELLOW}⚠ 未找到.env文件${NC}"
    echo "请执行以下步骤："
    echo "1. 访问 https://console.anthropic.com/"
    echo "2. 创建API密钥"
    echo "3. 复制.env.example为.env"
    echo "4. 填入你的API密钥"
    echo ""
    echo "命令："
    echo "  cp .env.example .env"
    echo "  然后编辑.env填入API密钥"
fi

# 创建示例数据
echo ""
echo -e "${YELLOW}创建示例数据文件...${NC}"

# 创建示例CSV数据
mkdir -p data
cat > data/sample_sales.csv << 'EOF'
date,product,category,sales,quantity
2024-01-01,Product A,Electronics,15230,23
2024-01-02,Product B,Electronics,18560,31
2024-01-03,Product C,Clothing,8900,45
2024-01-04,Product A,Electronics,16780,25
2024-01-05,Product D,Home,12340,18
2024-01-06,Product B,Electronics,19200,32
2024-01-07,Product C,Clothing,9500,48
2024-01-08,Product E,Electronics,22100,15
2024-01-09,Product A,Electronics,15890,24
2024-01-10,Product D,Home,11800,17
EOF
echo -e "${GREEN}✓ 示例销售数据${NC}"

# 创建示例文本
cat > data/sample_notes.txt << 'EOF'
# Python装饰器教程

## 什么是装饰器？

装饰器是Python中用于修改函数或类行为的强大工具。
它允许你在不修改原函数代码的情况下，为函数添加额外功能。

## 基本语法

使用@符号应用装饰器：

```python
@decorator_name
def my_function():
    pass
```

## 工作原理

1. 定义装饰器函数
2. 接受函数作为参数
3. 返回新函数

## 常见用途

- 日志记录
- 性能计时
- 权限验证
- 缓存
- 重试机制
EOF
echo -e "${GREEN}✓ 示例课程笔记${NC}"

# 创建快速启动脚本
cat > run_examples.sh << 'EOF'
#!/bin/bash
# 快速运行示例代码

source ~/agent-skills-learning/venv/bin/activate
cd ~/agent-skills-learning/code/examples

echo "选择要运行的示例："
echo "1. 基础技能使用"
echo "2. API集成示例"
echo "3. 数据分析示例"
echo "4. 生成练习题示例"
read -p "输入选择 (1-4): " choice

case $choice in
    1)
        python3 basic_skill_usage.py
        ;;
    2)
        python3 api_integration.py
        ;;
    3)
        python3 data_analysis.py
        ;;
    4)
        python3 practice_generator.py
        ;;
    *)
        echo "无效选择"
        ;;
esac
EOF
chmod +x run_examples.sh
echo -e "${GREEN}✓ 快速启动脚本${NC}"

# 完成信息
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo -e "${GREEN}✅ 环境配置完成！${NC}"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📁 项目位置: ~/agent-skills-learning"
echo ""
echo "📝 下一步："
echo "1. 配置API密钥："
echo "   cd ~/agent-skills-learning"
echo "   cp .env.example .env"
echo "   # 编辑.env填入你的API密钥"
echo ""
echo "2. 激活虚拟环境："
echo "   source ~/agent-skills-learning/venv/bin/activate"
echo ""
echo "3. 运行示例："
echo "   bash run_examples.sh"
echo ""
echo "4. 开始学习："
echo "   查看笔记: cd ~/agent-skills-learning/notes"
echo "   查看练习: cd ~/agent-skills-learning/practice"
echo ""
