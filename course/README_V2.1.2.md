# 企業 AI Agent｜業務報價決策 Agent V2.1.2 學員教學版

## 特色
這一版不改 V2 技術架構，只提升教學可讀性。

每個 Notebook 都增加：
- 逐格解說
- 大量繁體中文註解
- 學生修改區
- 不需修改區
- 成功畫面
- 常見錯誤
- 每 LAB 學習回顧

## 技術架構
Google ADK + Groq API + Agent Skills + MCP + LINE

## 建議操作順序
1. LAB01_ADK_Groq_First_Agent.ipynb
2. LAB02_ADK_Agent_Skill.ipynb
3. LAB03_ADK_Groq_MCP.ipynb
4. LAB04_Final_ADK_Skill_MCP_LINE.ipynb

## 學生最重要規則
只修改有：
`👨‍🎓 學生修改區`
標示的地方。


## V2.1.2 穩定性修正

課堂預設 Groq 模型改為：

`groq/qwen/qwen3.8-27b`

並在 ADK `LiteLlm` 中設定：

`reasoning_effort="none"`

目的：避免 reasoning_content 在多輪 Tool Calling 歷史中造成 Groq 400。


## V2.1.2 變更

Groq API Key 改為完全從 Google Colab Secrets 讀取。

請在 Colab 左側「🔑 Secrets」建立：

`GROQ_API_KEY`

Notebook 不再使用 `getpass()` 讀取 Groq API Key。
