"""
MCP服务器模块
"""
import sys
from mcp.server.fastmcp import FastMCP
from weather_mcp.weather import weather_service

# 创建MCP服务器，启用Streamable HTTP支持
mcp = FastMCP(
    "Weather Server",
    stateless_http=True,  # 启用无状态HTTP模式
    json_response=True    # 使用JSON响应格式
)

@mcp.tool()
async def get_weather(city: str) -> dict:
    """获取指定城市的天气信息
    
    Args:
        city: 城市编码
        
    Returns:
        dict: 天气信息
    """
    return await weather_service.get_weather(city)

def main():
    """主函数"""
    if len(sys.argv) != 2 or sys.argv[1] not in ["stdio", "http"]:
        print("Usage: amap-weather-mcp [stdio|http]")
        sys.exit(1)
    
    mode = sys.argv[1]
    
    if mode == "http":
        # 使用Streamable HTTP模式
        mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
    else:
        # 使用stdio模式
        mcp.run()

if __name__ == "__main__":
    main() 