# Github每日趋势自动获取

## 结构图

<img src="assets/graph.png" style="width: 60%; height: auto;">

## 使用

### 依赖安装

```bash
pip install -r requirements.txt
```

### 模型配置

打开[文件](llms.py)，并修改相应内容

```
BASE_URL = ""
OLLAMA_MODEL = ""
REMOTE_MODEL = ""
API_KEY = "empty"
TEMPERATURE = 0.5
```

### 执行

```bash
python run.py
```

## 效果

![img.png](assets/result.png)

---

wx公众号： ai智能熊熊

<img src="assets/img.png" style="width: 60%; height: auto;">

飞书群: ai智能熊熊

<img src="assets/qun.jpg" style="width: 60%; height: auto;">
