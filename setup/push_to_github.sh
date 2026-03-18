#!/bin/bash

# GitHub 自动推送脚本

set -e

echo "🚀 Agent Skills 学习系统 - GitHub 推送工具"
echo "=============================================="
echo ""

# 检查是否在正确的目录
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if [ ! -f "${PROJECT_DIR}/README.md" ]; then
    echo "❌ 错误：无法找到项目目录"
    exit 1
fi

# 切换到项目目录
cd "${PROJECT_DIR}"

# 询问GitHub用户名
read -p "👤 请输入你的GitHub用户名: " github_username

if [ -z "$github_username" ]; then
    echo "❌ 用户名不能为空"
    exit 1
fi

# 仓库名
repo_name="agent-skills-learning"
repo_url="https://github.com/${github_username}/${repo_name}.git"

echo ""
echo "📋 仓库信息:"
echo "   用户名: ${github_username}"
echo "   仓库名: ${repo_name}"
echo "   URL: ${repo_url}"
echo ""

# 确认
read -p "✅ 确认推送？(y/n): " confirm
if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
    echo "❌ 取消操作"
    exit 0
fi

echo ""
echo "🔧 配置Git远程仓库..."
git remote add origin ${repo_url} 2>/dev/null || git remote set-url origin ${repo_url}

echo "✅ 远程仓库配置完成"
echo ""
echo "📤 推送到GitHub..."
echo ""

# 推送
if git push -u origin main; then
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "🎉 推送成功！"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "📍 你的仓库地址:"
    echo "   ${repo_url}"
    echo ""
    echo "💡 下次更新时，运行:"
    echo "   git add ."
    echo "   git commit -m '你的更新'"
    echo "   git push"
    echo ""
else
    echo ""
    echo "❌ 推送失败"
    echo ""
    echo "🔧 可能的原因:"
    echo "1. GitHub仓库还不存在"
    echo "   → 请先访问 https://github.com/new 创建仓库"
    echo ""
    echo "2. 需要身份验证"
    echo "   → 运行: gh auth login"
    echo "   → 或生成Personal Access Token"
    echo ""
    echo "📖 详细说明: 查看 GITHUB_SETUP.md"
    exit 1
fi
