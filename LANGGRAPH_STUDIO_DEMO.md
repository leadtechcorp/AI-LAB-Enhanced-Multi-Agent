# LangGraph Studio Demo - Customer Service Agent

## 🎯 Overview

This project demonstrates the Visual IDE features of **LangGraph Studio** through a comprehensive customer service agent workflow. The demo showcases advanced graph-based AI agent capabilities with real-time visualization and debugging features.

## 🚀 LangGraph Studio Environment

- **LangSmith Dashboard**: [https://eu.smith.langchain.com/o/fb2e6235-a27a-4a33-bd77-7c865b6d5252](https://eu.smith.langchain.com/o/fb2e6235-a27a-4a33-bd77-7c865b6d5252)
- **Local Studio URL**: http://127.0.0.1:8123
- **Region**: EU (European Union)
- **Organization ID**: `fb2e6235-a27a-4a33-bd77-7c865b6d5252`

## 🎨 Visual Workflow Architecture

The customer service agent demonstrates a sophisticated multi-node workflow:

```
START
  ↓
📋 Customer Identification
  ↓
😊 Sentiment Analysis
  ↓
🏷️ Issue Categorization
  ↓
📚 Knowledge Base Search
  ↓
🔀 Escalation Router
  ↓
  ├─ (if escalation needed) → 🔼 Escalation → END
  └─ (if no escalation) → ✅ Resolution → END
```

## 🛠️ Quick Start

### 1. Start LangGraph Studio
```bash
cd AI-LAB-langGraph-dev
source .venv/bin/activate
langgraph dev --host 127.0.0.1 --port 8123
```

### 2. Run Demo Scenarios
```bash
python3 demo_customer_service.py
```

### 3. Access Visual IDE
Open your browser to: **http://127.0.0.1:8123**

## 📊 Demo Scenarios

The demo includes four comprehensive scenarios designed to showcase different workflow paths:

### 🚨 Scenario 1: Premium Customer - Urgent Billing Issue
- **Input**: "I'm really frustrated! I was charged twice for my premium subscription this month and this is urgent!"
- **Expected Flow**: Customer ID → Sentiment (negative) → Categorization (billing) → Knowledge Base → **Escalation**
- **Outcome**: Escalated to specialist team due to negative sentiment + premium customer + billing issue

### 🔧 Scenario 2: Standard Customer - Technical Issue  
- **Input**: "Hi, I'm having trouble logging into my account. The app keeps showing an error message."
- **Expected Flow**: Customer ID → Sentiment (neutral) → Categorization (technical) → Knowledge Base → **Resolution**
- **Outcome**: Direct resolution with technical guidance

### 😊 Scenario 3: Happy Customer - General Inquiry
- **Input**: "Hello! I love your service so far. I just wanted to ask about upgrading my account."
- **Expected Flow**: Customer ID → Sentiment (positive) → Categorization (account) → Knowledge Base → **Resolution**
- **Outcome**: Smooth resolution with account upgrade information

### 😤 Scenario 4: Repeat Customer - Service Complaint
- **Input**: "This is my fourth time contacting support about the same problem. I'm very dissatisfied."
- **Expected Flow**: Customer ID → Sentiment (negative) → Categorization (complaint) → Knowledge Base → **Escalation**
- **Outcome**: Escalated due to repeat customer with multiple tickets

## 🎯 Visual IDE Features Demonstrated

### 1. **Real-time Node Execution**
- Watch nodes light up as they execute
- See the flow progress through the workflow
- Visual indication of current processing step

### 2. **State Inspection**
- View complete state at each node
- Inspect message history
- Monitor agent notes and metadata

### 3. **Conditional Routing Visualization**
- See decision points in the workflow
- Understand escalation logic
- Track routing decisions visually

### 4. **Message Flow Tracking**
- Follow conversation progression
- See AI responses generated at each step
- Monitor state transformations

### 5. **Interactive Debugging**
- Pause execution at any node
- Inspect variable values
- Modify state for testing

### 6. **LangSmith Integration**
- Automatic trace logging
- Performance monitoring
- Error tracking and analysis

## 📋 Agent Capabilities

### Core Functionality
- **Customer Identification**: Simulates customer lookup and tier detection
- **Sentiment Analysis**: Detects emotional tone (positive, negative, neutral, urgent)
- **Issue Categorization**: Classifies problems (billing, technical, account, complaint, general)
- **Priority Assessment**: Determines urgency based on customer tier + sentiment + issue type
- **Knowledge Base Search**: Retrieves relevant solutions and articles
- **Escalation Logic**: Smart routing based on multiple criteria
- **Resolution Handling**: Provides tailored responses and solutions

### Escalation Criteria
- High priority + negative sentiment
- Premium customer + negative experience  
- Customer with multiple previous tickets (>3)
- Critical technical issues
- Billing disputes over threshold amounts

## 🔧 Technical Implementation

### Node Structure
Each node in the workflow performs specific functions:

```python
# Example node implementation
def sentiment_analysis_node(state: CustomerServiceState):
    """Analyzes customer sentiment to determine approach"""
    # Extract last customer message
    # Apply sentiment detection logic
    # Update state with sentiment score
    # Return updated state
```

### State Management
```python
class CustomerServiceState(TypedDict):
    messages: Annotated[list, add_messages]
    customer_info: dict
    ticket_priority: str
    issue_category: str
    sentiment: str
    escalation_reason: str
    resolution_status: str
    agent_notes: list
```

### Conditional Edges
```python
def should_escalate(state: CustomerServiceState) -> Literal["escalate", "resolve"]:
    """Determines routing based on escalation status"""
    return "escalate" if state.get("resolution_status") == "escalated" else "resolve"
```

## 🚀 Available Graphs

The project includes two graphs for demonstration:

1. **`my_agent`**: Simple conversational agent (original)
2. **`customer_service`**: Advanced customer service workflow (demo focus)

## 📊 Monitoring & Analytics

### LangSmith Tracing
All executions are automatically traced to LangSmith for:
- Performance analysis
- Error tracking
- Usage patterns
- Conversation quality metrics

### Local Metrics
- Node execution times
- State size tracking
- Message count per session
- Escalation rates

## 🎮 Interactive Features

### Test Different Scenarios
Modify the demo script to test:
- Different customer tiers (Standard, Premium, Enterprise)
- Various sentiment expressions
- Different issue types
- Custom escalation triggers

### Custom Workflows
Extend the agent with additional nodes:
- Payment processing
- Account management
- Product recommendations
- Feedback collection

## 🔗 Integration Points

### External Services (Simulated)
- Customer database lookup
- Knowledge base search
- Ticketing system
- Escalation routing
- Follow-up scheduling

### Real-world Extensions
- CRM integration
- Email/SMS notifications
- Live chat handoff
- Analytics dashboard
- Feedback loops

## 📈 Success Metrics

### Workflow Efficiency
- ✅ 100% scenario completion rate
- ✅ Appropriate escalation routing
- ✅ Contextual response generation
- ✅ State persistence across nodes

### Visual IDE Demonstration
- ✅ Real-time workflow visualization
- ✅ Interactive debugging capabilities
- ✅ State inspection features
- ✅ Conditional routing display
- ✅ Message flow tracking

## 🛡️ Best Practices Demonstrated

1. **Modular Node Design**: Each node has a single responsibility
2. **State Management**: Clean state transitions between nodes
3. **Error Handling**: Graceful handling of edge cases
4. **Logging**: Comprehensive agent notes for audit trails
5. **Conditional Logic**: Smart routing based on multiple criteria
6. **User Experience**: Contextual and personalized responses

## 🚀 Next Steps

1. **Extend the Workflow**: Add more sophisticated nodes
2. **Real Integration**: Connect to actual CRM/ticketing systems
3. **ML Enhancement**: Integrate advanced sentiment analysis models
4. **Performance Optimization**: Optimize for high-volume scenarios
5. **A/B Testing**: Test different workflow configurations

---

## 📞 Demo Access

- **LangGraph Studio**: http://127.0.0.1:8123
- **LangSmith Dashboard**: https://eu.smith.langchain.com/o/fb2e6235-a27a-4a33-bd77-7c865b6d5252
- **Demo Script**: `python3 demo_customer_service.py`

*This demo showcases the full capabilities of LangGraph Studio's Visual IDE for building, testing, and debugging sophisticated AI agent workflows.*
