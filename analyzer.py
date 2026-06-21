from pathlib import Path
import ollama

# Read Jenkins log
log = Path("logs/failed_build.log").read_text(encoding="utf-8")

prompt = f"""
You are a Senior DevOps Engineer.

Analyze the following Jenkins build log.

Return:

1. Root Cause
2. Explanation
3. Suggested Fix
4. Severity
5. Prevention Tips

Jenkins Log:

{log}
"""

response = ollama.chat(
    model="qwen2.5-coder:7b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print("\n========== AI Analysis ==========\n")
print(response["message"]["content"])
