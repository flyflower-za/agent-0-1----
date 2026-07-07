#!/usr/bin/env python3
"""
AI Learning Progress Server
简单的 HTTP 服务器，用于读写本地进度文件
"""
import json
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

# 进度文件路径
PROGRESS_FILE = Path(__file__).parent / 'ai_learning_progress.json'

class ProgressHandler(SimpleHTTPRequestHandler):
    """自定义请求处理器"""

    def do_GET(self):
        """处理 GET 请求"""
        if self.path == '/api/progress':
            self.send_progress()
        else:
            # 静态文件服务
            super().do_GET()

    def do_POST(self):
        """处理 POST 请求"""
        if self.path == '/api/progress':
            self.save_progress()
        else:
            self.send_error(404, "Not Found")

    def do_OPTIONS(self):
        """处理 OPTIONS 请求（CORS 预检）"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def send_progress(self):
        """返回进度数据"""
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        if PROGRESS_FILE.exists():
            with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
                progress = json.load(f)
        else:
            progress = {}

        self.wfile.write(json.dumps(progress).encode('utf-8'))

    def save_progress(self):
        """保存进度数据"""
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            progress = json.loads(post_data.decode('utf-8'))

            # 保存到文件
            with open(PROGRESS_FILE, 'w', encoding='utf-8') as f:
                json.dump(progress, f, indent=2, ensure_ascii=False)

            print(f"✅ 进度已保存到: {PROGRESS_FILE}")

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True}).encode('utf-8'))

        except Exception as e:
            print(f"❌ 保存失败: {e}")
            self.send_response(500)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode('utf-8'))

    def log_message(self, format, *args):
        """自定义日志输出"""
        print(f"[{self.log_date_time_string()}] {format % args}")


def main():
    """启动服务器"""
    port = 8000
    server_address = ('', port)

    print("=" * 60)
    print("🚀 AI Learning Progress Server")
    print("=" * 60)
    print(f"📁 项目目录: {Path(__file__).parent}")
    print(f"📊 进度文件: {PROGRESS_FILE}")
    print(f"🌐 服务器地址: http://localhost:{port}")
    print("=" * 60)
    print("按 Ctrl+C 停止服务器")
    print("=" * 60)

    httpd = HTTPServer(server_address, ProgressHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    main()
