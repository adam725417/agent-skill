# Colab Secrets 設定 GROQ_API_KEY

## 為什麼改用 Secrets？
避免：
- API Key 顯示在 Notebook
- 學生不小心截圖或分享金鑰
- 每次重跑都重新貼 Key

## 設定步驟
1. 開啟 Google Colab
2. 左側點「🔑 Secrets」
3. 點新增
4. Name 輸入：`GROQ_API_KEY`
5. Value 貼上 Groq API Key
6. 開啟該 Secret 的 Notebook access

## Notebook 讀取方式
```python
from google.colab import userdata
GROQ_API_KEY = userdata.get("GROQ_API_KEY")
```

## 注意
Secret 名稱一定要完全相同：
`GROQ_API_KEY`

大小寫錯誤也會讀不到。
