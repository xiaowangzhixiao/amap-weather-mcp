# Weather MCP Server

基于高德地图天气API的MCP服务器，支持stdio和Streamable HTTP两种传输模式。

## 功能特点

- 支持高德地图天气API查询
- 支持stdio和Streamable HTTP两种传输模式
- 使用uv管理Python虚拟环境
- 可配置的高德API密钥

## 安装

### 方法1：使用pip安装

```bash
pip install amap-weather-mcp
```

### 方法2：从源码安装

1. 克隆仓库：
```bash
git clone https://github.com/xiaowangzhixiao/amap-weather-mcp.git
cd amap-weather-mcp
```

2. 使用uv创建虚拟环境：
```bash
uv venv
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate  # Windows
```

3. 安装依赖：
```bash
uv pip install -e .
```

## 配置

1. 复制环境变量示例文件：
```bash
cp .env.example .env
```

2. 编辑 `.env` 文件，填入你的高德地图API密钥：
```
AMAP_API_KEY=your_api_key_here
```

## 使用方法

### 命令行使用

安装后，可以直接使用 `amap-weather-mcp` 命令：

```bash
# stdio模式
amap-weather-mcp stdio

# HTTP模式
amap-weather-mcp http
```

### 作为Python模块使用

```python
from weather_mcp.server import mcp

# 使用stdio模式
mcp.run()

# 使用HTTP模式
mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
```

### MCP Inspector 配置

1. stdio模式：
```json
{
    "command": "amap-weather-mcp",
    "args": ["stdio"]
}
```

2. HTTP模式：
```json
{
    "url": "http://localhost:8000/mcp",
    "transport": "streamable-http"
}
```

## 开发

### 安装开发依赖

```bash
uv pip install -e ".[dev]"
```

### 运行测试

```bash
pytest
```

### 代码格式化

```bash
ruff format .
```

## 许可证

MIT 