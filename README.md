# 📡 Drop Detective AI

**Drop Detective AI** is a telecom network troubleshooting assistant that analyzes telecom tower logs and provides insights about call drops, signal strength, congestion, and network performance.

The system helps network engineers quickly identify issues such as weak signals, high congestion, and handoff failures.

---

# 🚀 Features

* 📊 Telecom log analysis
* 🗼 Tower performance investigation
* 🌍 Region network analysis
* 📉 Call drop detection
* 📶 Signal strength monitoring
* ⚡ Congestion hotspot detection
* 🧠 Root cause analysis using telecom logs
* 💬 ChatGPT-style interface built with Streamlit

---

# 🏗️ Project Architecture

```
User Query
     ↓
Streamlit Chat Interface
     ↓
Query Detection Engine
     ↓
Pandas Data Analysis
     ↓
Telecom Logs Dataset
     ↓
Network Insights + Suggested Fix
```

---

# 📂 Project Structure

```
DropDetective/
│
├── agents/
│   ├── agent.py
│   ├── prompts.py
│   └── tools.py
│
├── app/
│   ├── app.py
│   └── cli.py
│
├── data/
│   ├── raw/
│   │   └── telecom_logs.csv
│   └── processed/
│
├── embeddings/
│
├── llm/
│   └── load_model.py
│
├── rag/
│   ├── ingest.py
│   └── retrieve.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

The telecom dataset contains the following fields:

| Column           | Description                    |
| ---------------- | ------------------------------ |
| Region           | City or network region         |
| Tower_ID         | Unique tower identifier        |
| Date             | Log date                       |
| Call_Drops       | Number of dropped calls        |
| Signal_Strength  | Signal power in dBm            |
| Congestion_Level | Network congestion level       |
| Handoff_Failure  | Percentage of handoff failures |
| Notes            | Additional observations        |

Example:

```
Region,Tower_ID,Date,Call_Drops,Signal_Strength,Congestion_Level,Handoff_Failure,Notes
Hyderabad,T123,2025-09-01,56,-95,High,12,Heavy user load
Mumbai,T789,2025-09-01,22,-75,Low,2,Normal operation
Kolkata,T200,2025-09-02,47,-93,High,12,Peak hour congestion
```

---

# 🧑‍💻 Installation

Clone the repository:

```
git clone https://github.com/sujan-mondal-cu/drop-detective.git
cd drop-detective-ai
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# ▶️ Run the Application

Start the Streamlit app:

```
python -m streamlit run app/chat_ui.py
```

Then open:

```
http://localhost:8501
```

---

# 💬 Example Queries

### Region Analysis

```
Why are call drops high in Hyderabad?
Analyze network performance in Kolkata
Which region has the highest congestion?
```

### Tower Investigation

```
Analyze tower T123 performance
Tower T789 signal strength
Check tower T456 network condition
```

### Network Insights

```
Find the tower with the worst network performance
Which city has the most stable network?
Show average call drops per region
Find towers with weak signal strength
```

---

# 🧠 Example Output

```
Tower Analysis

Tower ID: T123
Region: Hyderabad

Average Call Drops: 64
Signal Strength: -96 dBm
Congestion Level: High
Handoff Failure: 15%

Cause: Heavy user load

Suggested Fix
1. Increase tower capacity
2. Deploy additional microcells
3. Optimize handoff algorithms
```

---

# 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* LangChain
* HuggingFace Transformers
* ChromaDB
* Sentence Transformers

---

# 📈 Future Improvements

* Telecom analytics dashboard with charts
* AI anomaly detection for network failures
* Real-time telecom monitoring
* Integration with live telecom network logs

---

# 👨‍💻 Author

**Sujan Mondal**
Computer Science Engineering
Telecom AI / Data Analysis Enthusiast

---

✅ In **VS Code**:

1. Open your project folder
2. Click **README.md**
3. Paste this content
4. Save

VS Code will automatically show the **formatted preview**.

---

If you want, I can also give you a **professional GitHub README with badges, screenshots, and architecture diagram** that makes your project look like a **top open-source AI project**.
