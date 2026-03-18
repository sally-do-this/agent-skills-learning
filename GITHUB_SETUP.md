# 🚀 GitHub 上传指南

## 步骤1: 创建GitHub仓库

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `agent-skills-learning`
   - **Description**: `吴恩达Agent Skills课程完整学习系统`
   - **Public**: ✅ (公开)
   - **不要**勾选 "Add a README file" (我们已经有了)
3. 点击 "Create repository"

## 步骤2: 推送到GitHub

创建仓库后，GitHub会显示推送命令。运行以下命令（替换YOUR_USERNAME）：

```bash
cd ~/agent-skills-learning

# 添加远程仓库（替换YOUR_USERNAME为你的GitHub用户名）
git remote add origin https://github.com/YOUR_USERNAME/agent-skills-learning.git

# 推送到GitHub
git push -u origin main
```

## 完整示例

如果你的GitHub用户名是 `zhangyu1774`：

```bash
git remote add origin https://github.com/zhangyu1774/agent-skills-learning.git
git push -u origin main
```

## 步骤3: 验证

推送成功后，访问：
```
https://github.com/YOUR_USERNAME/agent-skills-learning
```

你应该能看到所有的学习材料！

## 🔐 如果需要认证

如果推送时提示登录：

1. **使用GitHub CLI** (推荐):
   ```bash
   brew install gh  # macOS
   gh auth login
   ```

2. **使用Personal Access Token**:
   - 访问 https://github.com/settings/tokens
   - 生成新的token (repo权限)
   - 使用token作为密码

## 📝 后续更新

当你修改内容后：

```bash
cd ~/agent-skills-learning
git add .
git commit -m "你的提交信息"
git push
```

## 🎉 完成！

现在你的学习材料已经在GitHub上了！

可以分享给其他人：
```
https://github.com/YOUR_USERNAME/agent-skills-learning
```
