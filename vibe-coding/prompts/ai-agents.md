# 🤖 Vibe Coding Prompts: AI Agents

> Copy-paste these prompts into your AI-Native IDE to build
> AI-powered applications — the ultimate Vibe Coding skill!

---

## 🧠 Build Your First AI Agent

### Smart Q&A Assistant

```
Build a Python AI assistant that can answer questions about any document:

1. Accept a text file or PDF as input
2. Use OpenAI API (or any available LLM API) to:
   - Read and chunk the document
   - Answer questions about its content
   - Provide relevant quotes from the source
3. Features:
   - Interactive terminal chat interface
   - Conversation memory (remember context within session)
   - "I don't know" response when the answer isn't in the document
   - Show confidence level for each answer
4. Add colorful terminal output with:
   - 🤖 prefix for AI responses
   - 👤 prefix for user input
   - Typing animation for AI responses
5. Handle API errors gracefully

Use openai + tiktoken. Store API key in .env file.
Ask me for my API key before starting.
```

### AI-Powered Code Reviewer

```
Create a Python script that reviews code using AI:

1. Accept a Python file as command-line argument
2. Send the code to an LLM and request:
   - Code quality assessment (1-10 score)
   - Bug detection and potential issues
   - Performance improvement suggestions
   - PEP 8 style recommendations
   - Security concerns if any
3. Output a structured review report:
   - Summary with overall score
   - Issues categorized by severity (Critical/Warning/Info)
   - Specific line references for each issue
   - Suggested code improvements with diff format
4. Save report as both Markdown and terminal output
5. Support --fix flag to auto-apply simple fixes

Use any available LLM API. Handle rate limits and API errors.
```

---

## 🔗 Multi-Agent Systems

### Research Assistant Pipeline

```
Build a multi-step AI research assistant:

1. Input: A research topic (from command line)
2. Pipeline steps:
   Step 1 - Research: Search the web for the topic, collect 5-10 relevant sources
   Step 2 - Summarize: Have AI summarize each source into key points
   Step 3 - Synthesize: Combine all summaries into a coherent overview
   Step 4 - Report: Generate a structured research report with:
      - Executive summary
      - Key findings
      - Sources and citations
      - Recommended next steps
3. Save the report as a Markdown file
4. Show progress for each step in the terminal
5. Cache intermediate results to avoid re-fetching

Use requests for web search + any LLM API for analysis.
```

### AI Content Generator

```
Create an AI-powered blog post generator:

1. Input: Topic and target audience
2. Generation pipeline:
   - Generate 3 title options → let user pick one
   - Create detailed outline → show for approval
   - Write each section with proper transitions
   - Generate SEO meta description
   - Suggest relevant tags
3. Output features:
   - Save as Markdown file
   - Include estimated reading time
   - Add table of contents
   - Suggest places for images (with AI-generated descriptions)
4. Support multiple tones: professional, casual, technical, storytelling
5. Add --language flag for Chinese or English output

Use any available LLM API. Implement retry logic for API calls.
```

---

## 🏗️ Practical AI Applications

### Smart Email Classifier

```
Build an AI-powered email classifier and auto-responder:

1. Generate 50 sample emails (various types: inquiry, complaint,
   feedback, spam, urgent request)
2. Classification pipeline:
   - Categorize each email (inquiry/complaint/feedback/spam/urgent)
   - Extract key entities (names, dates, products mentioned)
   - Assign priority level (Critical/High/Medium/Low)
   - Generate suggested reply draft
3. Dashboard output:
   - Category distribution chart
   - Priority breakdown
   - Response time estimation
4. Export results to JSON and CSV
5. Interactive mode: paste an email → get instant classification

Use any LLM API. Show processing progress with a nice spinner.
```

---

## 💡 Tips for AI Agent Prompts

| Tip                             | Why                                                  |
| ------------------------------- | ---------------------------------------------------- |
| **Specify the LLM**             | "Use OpenAI API" or "Use any available LLM"          |
| **Ask for error handling**      | API rate limits, network issues, invalid responses   |
| **Request conversation memory** | Makes agents actually useful for follow-up questions |
| **Define the output format**    | "Respond in JSON" or "Generate Markdown report"      |
| **Include fallbacks**           | "If API fails, show cached results"                  |
| **Set guardrails**              | "Say 'I don't know' when answer isn't in the data"   |

### 🔑 Important: API Keys

Most AI agent prompts require API keys. Best practices:

```bash
# Create a .env file (never commit this!)
echo "OPENAI_API_KEY=sk-your-key-here" > .env
echo ".env" >> .gitignore
```

Your AI IDE agent can help you set this up — just ask!

---

<p align="center">
  📚 Learn the full Vibe Coding methodology at <a href="https://www.hoppypy.com/en/learn/python-vibe/01-choose-your-weapon">HoppyPy</a>
</p>
