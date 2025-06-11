"""
天气服务模块
"""
from typing import Dict, Any, Optional
import httpx
from weather_mcp.config import settings

class WeatherService:
    """天气服务类"""
    BASE_URL = "https://restapi.amap.com/v3/weather/weatherInfo"

    def __init__(self):
        self.api_key = settings.amap_api_key

    async def get_weather(self, city: str, extensions: str = "base") -> Dict[str, Any]:
        """
        获取天气信息
        
        Args:
            city: 城市编码
            extensions: 气象类型，base:返回实况天气，all:返回预报天气
            
        Returns:
            Dict[str, Any]: 天气信息
        """
        params = {
            "key": self.api_key,
            "city": city,
            "extensions": extensions,
            "output": "JSON"
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(self.BASE_URL, params=params)
            response.raise_for_status()
            return response.json()

weather_service = WeatherService() 