"""
Customer Service Agent for LangGraph Studio Demo
This agent demonstrates the Visual IDE features of LangGraph with a realistic customer service workflow.
"""

import os
from typing import TypedDict, Annotated, Literal
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from datetime import datetime
import json

# Define the state schema for our customer service agent
class CustomerServiceState(TypedDict):
    messages: Annotated[list, add_messages]
    customer_info: dict
    ticket_priority: str
    issue_category: str
    sentiment: str
    escalation_reason: str
    resolution_status: str
    agent_notes: list

def customer_identification_node(state: CustomerServiceState):
    """
    Identifies the customer and retrieves their information.
    This node simulates looking up customer data.
    """
    messages = state["messages"]
    last_message = messages[-1] if messages else None
    
    # Simulate customer identification process
    customer_info = {
        "customer_id": "CS-2024-001",
        "name": "John Smith",
        "tier": "Premium",
        "account_status": "Active",
        "previous_tickets": 2,
        "satisfaction_score": 4.2
    }
    
    response = AIMessage(
        content=f"Hello! I've identified you in our system. Welcome back, {customer_info['name']}! "
                f"I see you're a {customer_info['tier']} customer. How can I assist you today?"
    )
    
    return {
        "messages": [response],
        "customer_info": customer_info,
        "resolution_status": "in_progress"
    }

def sentiment_analysis_node(state: CustomerServiceState):
    """
    Analyzes the sentiment of the customer's message to determine urgency and approach.
    """
    messages = state["messages"]
    customer_message = None
    
    # Find the last customer message
    for msg in reversed(messages):
        if isinstance(msg, HumanMessage):
            customer_message = msg.content
            break
    
    # Simple sentiment analysis (in production, you'd use a proper sentiment model)
    sentiment = "neutral"
    if any(word in customer_message.lower() for word in ["angry", "frustrated", "terrible", "awful", "hate"]):
        sentiment = "negative"
    elif any(word in customer_message.lower() for word in ["happy", "great", "excellent", "love", "amazing"]):
        sentiment = "positive"
    elif any(word in customer_message.lower() for word in ["urgent", "emergency", "critical", "asap"]):
        sentiment = "urgent"
    
    return {
        "sentiment": sentiment,
        "agent_notes": [f"Sentiment detected: {sentiment} at {datetime.now().strftime('%H:%M:%S')}"]
    }

def issue_categorization_node(state: CustomerServiceState):
    """
    Categorizes the customer's issue to route to the appropriate handler.
    """
    messages = state["messages"]
    customer_message = None
    
    # Find the last customer message
    for msg in reversed(messages):
        if isinstance(msg, HumanMessage):
            customer_message = msg.content.lower()
            break
    
    # Issue categorization logic
    if any(word in customer_message for word in ["billing", "payment", "charge", "invoice", "refund"]):
        category = "billing"
        priority = "medium"
    elif any(word in customer_message for word in ["technical", "error", "bug", "not working", "broken"]):
        category = "technical"
        priority = "high"
    elif any(word in customer_message for word in ["account", "login", "password", "access"]):
        category = "account"
        priority = "medium"
    elif any(word in customer_message for word in ["complaint", "dissatisfied", "problem"]):
        category = "complaint"
        priority = "high"
    else:
        category = "general"
        priority = "low"
    
    # Adjust priority based on customer tier and sentiment
    customer_info = state.get("customer_info", {})
    sentiment = state.get("sentiment", "neutral")
    
    if customer_info.get("tier") == "Premium":
        priority = "high" if priority == "medium" else priority
    
    if sentiment in ["negative", "urgent"]:
        priority = "high"
    
    return {
        "issue_category": category,
        "ticket_priority": priority,
        "agent_notes": state.get("agent_notes", []) + [
            f"Issue categorized as {category} with {priority} priority"
        ]
    }

def knowledge_base_search_node(state: CustomerServiceState):
    """
    Searches the knowledge base for solutions related to the customer's issue.
    """
    issue_category = state.get("issue_category", "general")
    
    # Simulate knowledge base search
    knowledge_base = {
        "billing": [
            "To request a refund, please provide your transaction ID and reason for the refund.",
            "Billing cycles are processed on the 1st of each month.",
            "You can update your payment method in the account settings."
        ],
        "technical": [
            "Try clearing your browser cache and cookies.",
            "Ensure you're using the latest version of our application.",
            "Check your internet connection and try again."
        ],
        "account": [
            "Reset your password using the 'Forgot Password' link on the login page.",
            "Account verification may take 24-48 hours to complete.",
            "Enable two-factor authentication for enhanced security."
        ],
        "complaint": [
            "We take all feedback seriously and will investigate your concern.",
            "A manager will review your case within 24 hours.",
            "Please provide specific details about your experience."
        ],
        "general": [
            "Visit our FAQ section for common questions.",
            "Contact us during business hours for immediate assistance.",
            "Check our status page for any ongoing service issues."
        ]
    }
    
    relevant_articles = knowledge_base.get(issue_category, knowledge_base["general"])
    
    response = AIMessage(
        content=f"I've found some relevant information for your {issue_category} inquiry:\n\n" + 
                "\n".join([f"• {article}" for article in relevant_articles[:2]]) +
                "\n\nDoes this help resolve your issue, or would you like me to look into this further?"
    )
    
    return {
        "messages": [response],
        "agent_notes": state.get("agent_notes", []) + [
            f"Knowledge base searched for {issue_category} issues"
        ]
    }

def escalation_router_node(state: CustomerServiceState):
    """
    Determines if the issue needs to be escalated based on various factors.
    """
    priority = state.get("ticket_priority", "low")
    sentiment = state.get("sentiment", "neutral")
    customer_info = state.get("customer_info", {})
    
    escalation_needed = False
    escalation_reason = ""
    
    # Escalation criteria
    if priority == "high" and sentiment in ["negative", "urgent"]:
        escalation_needed = True
        escalation_reason = "High priority issue with negative sentiment"
    elif customer_info.get("tier") == "Premium" and sentiment == "negative":
        escalation_needed = True
        escalation_reason = "Premium customer with negative experience"
    elif customer_info.get("previous_tickets", 0) > 3:
        escalation_needed = True
        escalation_reason = "Customer with multiple previous tickets"
    
    if escalation_needed:
        response = AIMessage(
            content="I understand this is an important issue for you. Let me connect you with a specialist "
                   "who can provide more detailed assistance. Please hold for a moment while I transfer your case."
        )
        resolution_status = "escalated"
    else:
        response = AIMessage(
            content="I'll continue working on resolving this issue for you. Let me gather a bit more information "
                   "to provide you with the best possible solution."
        )
        resolution_status = "in_progress"
    
    return {
        "messages": [response],
        "escalation_reason": escalation_reason,
        "resolution_status": resolution_status,
        "agent_notes": state.get("agent_notes", []) + [
            f"Escalation check: {'Required' if escalation_needed else 'Not required'}"
        ]
    }

def resolution_node(state: CustomerServiceState):
    """
    Provides resolution or next steps for the customer's issue.
    """
    issue_category = state.get("issue_category", "general")
    priority = state.get("ticket_priority", "low")
    customer_info = state.get("customer_info", {})
    
    # Provide tailored resolution based on issue category
    resolutions = {
        "billing": f"I've processed your billing request. As a {customer_info.get('tier', 'Standard')} customer, "
                  "you should see the changes reflected in your account within 24 hours.",
        "technical": "I've identified the technical issue and applied a fix. Please try the process again "
                    "and let me know if you continue to experience any problems.",
        "account": "Your account issue has been resolved. You should now be able to access all features. "
                  "Please log out and log back in to see the changes.",
        "complaint": "Thank you for bringing this to our attention. I've documented your feedback "
                    "and our team will use it to improve our services.",
        "general": "I hope I've been able to help with your inquiry today. Is there anything else "
                  "I can assist you with?"
    }
    
    response = AIMessage(
        content=resolutions.get(issue_category, resolutions["general"]) +
               "\n\nYour ticket has been resolved. You'll receive a follow-up email with the details. "
               "Thank you for contacting our support team!"
    )
    
    return {
        "messages": [response],
        "resolution_status": "resolved",
        "agent_notes": state.get("agent_notes", []) + [
            f"Issue resolved for {issue_category} category",
            f"Resolution completed at {datetime.now().strftime('%H:%M:%S')}"
        ]
    }

def escalation_node(state: CustomerServiceState):
    """
    Handles escalated cases that need specialist attention.
    """
    escalation_reason = state.get("escalation_reason", "")
    customer_info = state.get("customer_info", {})
    
    response = AIMessage(
        content=f"Hello {customer_info.get('name', 'valued customer')}, this is Sarah from our specialist team. "
                f"I've reviewed your case and I'm here to ensure we resolve this issue to your satisfaction. "
                f"Let me personally handle your concern and provide you with the priority attention you deserve."
    )
    
    return {
        "messages": [response],
        "resolution_status": "escalated_handling",
        "agent_notes": state.get("agent_notes", []) + [
            f"Escalated to specialist team: {escalation_reason}",
            f"Specialist engaged at {datetime.now().strftime('%H:%M:%S')}"
        ]
    }

def should_escalate(state: CustomerServiceState) -> Literal["escalate", "resolve"]:
    """
    Conditional edge function to determine if escalation is needed.
    """
    return "escalate" if state.get("resolution_status") == "escalated" else "resolve"

def create_customer_service_graph():
    """
    Creates the customer service workflow graph with visual IDE features.
    """
    # Create the graph
    workflow = StateGraph(CustomerServiceState)
    
    # Add all nodes to showcase the visual workflow
    workflow.add_node("customer_identification", customer_identification_node)
    workflow.add_node("sentiment_analysis", sentiment_analysis_node)
    workflow.add_node("issue_categorization", issue_categorization_node)
    workflow.add_node("knowledge_base_search", knowledge_base_search_node)
    workflow.add_node("escalation_router", escalation_router_node)
    workflow.add_node("resolution", resolution_node)
    workflow.add_node("escalation", escalation_node)
    
    # Define the workflow edges for visual representation
    workflow.add_edge(START, "customer_identification")
    workflow.add_edge("customer_identification", "sentiment_analysis")
    workflow.add_edge("sentiment_analysis", "issue_categorization")
    workflow.add_edge("issue_categorization", "knowledge_base_search")
    workflow.add_edge("knowledge_base_search", "escalation_router")
    
    # Conditional edge based on escalation decision
    workflow.add_conditional_edges(
        "escalation_router",
        should_escalate,
        {
            "escalate": "escalation",
            "resolve": "resolution"
        }
    )
    
    # Both escalation and resolution paths end the workflow
    workflow.add_edge("escalation", END)
    workflow.add_edge("resolution", END)
    
    # Add memory for persistence
    memory = MemorySaver()
    
    # Compile the graph
    app = workflow.compile(checkpointer=memory)
    
    return app

# Create the customer service graph instance
customer_service_graph = create_customer_service_graph()

# Export for LangGraph deployment
__all__ = ["customer_service_graph"]
