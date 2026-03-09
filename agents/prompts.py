ANALYSIS_PROMPT = """
Analyze the following telecom logs and identify:
1. Root cause of call drops
2. Evidence from data

Logs:
{logs}
"""

RECOMMEND_PROMPT = """
Based on the analysis below, suggest practical telecom solutions:

Analysis:
{analysis}
"""
