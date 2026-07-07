# AI Learning Concept Map

🎯 **零基础到全栈 AI 工程师的 6 个月学习路线图**

## 🚀 快速开始

### 方法一：使用启动脚本（推荐）

```bash
cd AI_Concept_Map
./start.sh
```

脚本会自动：
1. 检查 Python 环境
2. 创建进度文件（如果不存在）
3. 启动本地服务器
4. 在浏览器中打开应用

### 方法二：手动启动

```bash
# 1. 进入项目目录
cd AI_Concept_Map

# 2. 确保进度文件存在
echo "{}" > ai_learning_progress.json

# 3. 启动服务器
python3 server.py

# 4. 打开浏览器访问
# http://localhost:8000
```

## 📊 进度存储

### 自动保存到项目文件

应用现在会**自动将学习进度保存到项目中的 JSON 文件**：

```
AI_Concept_Map/
├── ai_learning_progress.json  ← 学习进度保存在这里
├── index.html
├── script.js
├── style.css
├── course_data.js
├── server.py                  ← 本地服务器
└── start.sh                   ← 启动脚本
```

### 工作原理

1. **本地服务器** (`server.py`)
   - 提供静态文件服务
   - 提供 API 接口读写进度文件
   - 支持跨域请求 (CORS)

2. **前端应用**
   - 检测服务器是否运行
   - 如果服务器运行：使用文件存储（持久化）
   - 如果服务器未运行：回退到 localStorage（临时）

### 进度文件格式

```json
{
  "1-1-1": "completed",
  "1-1-2": "unlocked",
  "1-1-3": "locked"
}
```

格式说明：`{月}-{周}-{日}`: `{状态}`

状态值：
- `completed` - 已完成
- `unlocked` - 已解锁
- `locked` - 锁定中

## 🎮 使用说明

### 学习打卡

1. 点击任意月份卡片进入学习界面
2. 左侧显示本周的学习目录
3. 完成当天学习后，点击底部"完成并继续"按钮
4. 进度自动保存，第二天自动解锁

### 导出/导入进度

在右上角可以找到：
- **📤 导出** - 手动备份进度文件
- **📥 导入** - 从备份恢复进度

## 🛠️ 技术栈

- **前端**: HTML5, CSS3, JavaScript (ES6+)
- **后端**: Python 3 (http.server)
- **数据存储**: JSON 文件
- **Markdown**: Marked.js
- **代码高亮**: Highlight.js

## 📁 项目结构

```
AI_Concept_Map/
├── index.html              # 主页面
├── script.js               # 前端逻辑
├── style.css               # 样式文件
├── course_data.js          # 课程数据
├── server.py               # 本地服务器
├── start.sh                # 启动脚本
├── ai_learning_progress.json # 学习进度
└── README.md               # 说明文档
```

## 🔧 故障排查

### 服务器无法启动

```bash
# 检查端口是否被占用
lsof -i :8000

# 杀掉占用端口的进程
kill -9 <PID>
```

### 进度未保存

1. 检查服务器是否正在运行
2. 打开浏览器控制台 (F12) 查看错误信息
3. 确认 `ai_learning_progress.json` 文件存在且有写权限

### 浏览器缓存问题

如果遇到奇怪的显示问题，尝试：
1. 按 `Cmd+Shift+R` (Mac) 或 `Ctrl+Shift+R` (Windows) 强制刷新
2. 清除浏览器缓存

## 📝 开发计划

- [ ] 添加学习统计功能
- [ ] 支持多用户进度
- [ ] 添加学习计时器
- [ ] 支持自定义学习路径
- [ ] 添加复习提醒功能

## 📄 许可证

MIT License

---

**Happy Learning! 🎓**
