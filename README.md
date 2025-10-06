# AI LAB Customer Service Development

A LangGraph-based customer service AI agent for the AI LAB platform.

## 📊 Solution Architecture

```mermaid
graph TB
    subgraph "User Interface Layer"
        USER[👤 User Input]
        STUDIO[🎨 LangGraph Studio<br/>Visual IDE]
    end
    
    subgraph "LangGraph Cloud Platform"
        subgraph "Graph Registry"
            ENHANCED[🎯 Enhanced Multi-Agent<br/>5 Specialized Agents]
            CUSTOMER[🎧 Customer Service<br/>7-Node Workflow]
            BASIC[💬 Basic Agent<br/>Simple Chatbot]
        end
        
        subgraph "Enhanced Multi-Agent System"
            COORD[🎯 COORDINATOR<br/>AI-Powered Routing]
            
            TECH[🛠️ Technical Expert<br/>System Diagnostics]
            CS[🎧 Customer Service<br/>Premium Support]
            SALES[💼 Sales Advisor<br/>Enterprise Consultation]
            DATA[📊 Data Analyst<br/>Advanced Analytics]
            GEN[💡 General Assistant<br/>Standard Queries]
            
            COORD -->|Route by Context| TECH
            COORD -->|Route by Sentiment| CS
            COORD -->|Route by Intent| SALES
            COORD -->|Route by Analytics| DATA
            COORD -->|Route by Default| GEN
        end
        
        subgraph "Customer Service Workflow"
            CS_ID[1️⃣ Customer ID]
            SENT[2️⃣ Sentiment Analysis]
            ISSUE[3️⃣ Issue Categorization]
            KB[4️⃣ Knowledge Base Search]
            ESC_ROUTER[5️⃣ Escalation Router]
            RESOLVE[6️⃣ Resolution]
            ESCALATE[7️⃣ Escalation Handler]
            
            CS_ID --> SENT
            SENT --> ISSUE
            ISSUE --> KB
            KB --> ESC_ROUTER
            ESC_ROUTER -->|Standard| RESOLVE
            ESC_ROUTER -->|High Priority| ESCALATE
        end
        
        subgraph "State Management"
            MEMORY[(🧠 Memory Saver<br/>Checkpointer)]
            STATE[📝 Conversation State<br/>Context Tracking]
        end
    end
    
    subgraph "Integration & Monitoring"
        LANGSMITH[📈 LangSmith<br/>Tracing & Analytics]
        GITHUB[🐙 GitHub<br/>Version Control]
        ENV[🔐 Environment Variables<br/>API Keys & Config]
    end
    
    subgraph "Deployment Infrastructure"
        DOCKER[🐳 Docker<br/>Containerization]
        API[🔌 REST API<br/>Endpoints]
        AUTO[⚡ Auto-Scaling<br/>Load Management]
    end
    
    USER --> ENHANCED
    USER --> CUSTOMER
    USER --> BASIC
    
    ENHANCED --> COORD
    CUSTOMER --> CS_ID
    
    COORD --> MEMORY
    CS_ID --> MEMORY
    MEMORY --> STATE
    
    ENHANCED --> LANGSMITH
    CUSTOMER --> LANGSMITH
    BASIC --> LANGSMITH
    
    GITHUB -->|CI/CD| DOCKER
    DOCKER -->|Deploy| API
    API -->|Scale| AUTO
    
    STUDIO -.->|Monitor & Debug| ENHANCED
    STUDIO -.->|Monitor & Debug| CUSTOMER
    
    ENV -.->|Configure| ENHANCED
    ENV -.->|Configure| CUSTOMER
    ENV -.->|Configure| BASIC
    
    style COORD fill:#4A90E2,stroke:#2E5C8A,stroke-width:3px,color:#fff
    style ENHANCED fill:#7B68EE,stroke:#4B0082,stroke-width:2px,color:#fff
    style CUSTOMER fill:#FF6B6B,stroke:#C92A2A,stroke-width:2px,color:#fff
    style BASIC fill:#51CF66,stroke:#2F9E44,stroke-width:2px,color:#fff
    style LANGSMITH fill:#FFA94D,stroke:#E67700,stroke-width:2px,color:#000
    style STUDIO fill:#20C997,stroke:#0CA678,stroke-width:2px,color:#fff
    style MEMORY fill:#845EF7,stroke:#5F3DC4,stroke-width:2px,color:#fff
```

### Key Components

- **Enhanced Multi-Agent**: 5 specialized agents with intelligent routing for complex scenarios
- **Customer Service**: 7-node workflow with sentiment analysis and escalation logic
- **Basic Agent**: Simple conversational baseline with memory persistence
- **LangGraph Cloud**: Production-ready deployment with auto-scaling
- **LangSmith Integration**: Real-time tracing, analytics, and monitoring
- **Visual IDE**: Cloud-native development and debugging interface

## 🚀 Features

- **Stateful Conversations**: Maintains context across multiple interactions
- **Memory Persistence**: Uses LangGraph's checkpointing for conversation history
- **Modular Design**: Clean separation of concerns with reusable components
- **Cloud Deployment Ready**: Configured for LangGraph Cloud deployment

## 📁 Project Structure

```
AI-LAB-Customer-Service-Dev/
├── langgraph.json          # LangGraph configuration
├── my_agent/              # Main agent package
│   ├── __init__.py        # Package initialization
│   └── graph.py           # Main graph definition
├── requirements.txt       # Python dependencies
├── env.example           # Environment variables template
└── README.md             # This file
```

## 🛠️ Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/leadtechcorp/AI-LAB-Customer-Service-Dev.git
   cd AI-LAB-Customer-Service-Dev
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   ```bash
   cp env.example .env
   # Edit .env with your API keys
   ```

## 🔧 Configuration

The `langgraph.json` file defines:
- **Dependencies**: Python packages and local modules
- **Graphs**: Entry points for your LangGraph applications
- **Environment**: Environment variable file location

## 🚀 Deployment

### Local Testing

```bash
# Test the graph locally
python -c "from my_agent.graph import graph; print('Graph loaded successfully!')"
```

### LangGraph Cloud

1. Push to GitHub repository
2. Connect repository in LangGraph Studio
3. Deploy using the web interface

## 🔑 Environment Variables

Copy `env.example` to `.env` and configure:

- `OPENAI_API_KEY`: OpenAI API key (if using OpenAI models)
- `ANTHROPIC_API_KEY`: Anthropic API key (if using Claude models)
- `LANGCHAIN_API_KEY`: LangSmith API key for tracing
- `LANGCHAIN_PROJECT`: Project name for LangSmith

## 🎯 Usage

The agent provides conversational AI capabilities with:
- Greeting and help responses
- AI LAB information
- Context-aware conversations
- Memory persistence across sessions

## 🔄 Development

To modify the agent behavior, edit `my_agent/graph.py`:
- Add new nodes for different capabilities
- Modify the conversation logic
- Integrate with external APIs or models

## 📊 Monitoring

Enable LangSmith tracing by setting:
```bash
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📜 License

This project is part of the AI LAB platform.
