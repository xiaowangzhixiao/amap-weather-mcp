from setuptools import setup, find_packages

setup(
    name="amap-weather-mcp",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "mcp[cli]>=1.9.3",
        "python-dotenv==1.0.0",
        "httpx==0.28.1",
        "pydantic==2.11.5",
        "pydantic-settings==2.5.2",
    ],
    entry_points={
        "console_scripts": [
            "amap-weather-mcp=weather_mcp.server:main",
        ],
    },
    python_requires=">=3.10",
    author="wangzhi",
    author_email="xiaowangzhixia@gmail.com",
    description="高德天气查询 MCP 服务器",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xiaowangzhixia/amap-weather-mcp",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 