#!/bin/bash

# AI Learning Concept Map - 启动脚本

echo "================================"
echo "🚀 AI Learning Concept Map"
echo "================================"
echo ""

# 检查 Python 是否安装
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到 Python3"
    echo "请先安装 Python3: brew install python3"
    exit 1
fi

# 进入项目目录
cd "$(dirname "$0")"

# 检查 ai_learning_progress.json 是否存在
if [ ! -f "ai_learning_progress.json" ]; then
    echo "📁 创建进度文件..."
    echo "{}" > ai_learning_progress.json
fi

# 启动服务器
echo "🌐 启动本地服务器..."
echo "📱 打开浏览器访问: http://localhost:8000"
echo ""
echo "按 Ctrl+C 停止服务器"
echo "================================"
echo ""

python3 server.py
