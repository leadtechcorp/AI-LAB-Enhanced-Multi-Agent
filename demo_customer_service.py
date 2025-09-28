#!/usr/bin/env python3
"""
LangGraph Studio Demo - Customer Service Agent
This script demonstrates the Visual IDE features of LangGraph Studio
"""

from customer_service_agent import customer_service_graph
from langchain_core.messages import HumanMessage
import asyncio
import json
from datetime import datetime

async def run_demo_scenarios():
    """
    Run multiple demo scenarios to showcase the customer service agent workflow.
    These scenarios will be visible in the LangGraph Studio Visual IDE.
    """
    
    print("🎭 LangGraph Studio Customer Service Agent Demo")
    print("=" * 60)
    print("This demo showcases the Visual IDE features of LangGraph Studio")
    print("Open your browser to: http://127.0.0.1:8123")
    print("=" * 60)
    
    # Demo Scenario 1: Premium Customer with Urgent Billing Issue
    print("\n📞 Scenario 1: Premium Customer - Urgent Billing Issue")
    print("-" * 50)
    
    config1 = {'configurable': {'thread_id': 'demo-premium-urgent'}}
    
    result1 = customer_service_graph.invoke({
        'messages': [HumanMessage(content="I'm really frustrated! I was charged twice for my premium subscription this month and this is urgent - I need this fixed immediately!")], 
        'customer_info': {},
        'ticket_priority': '',
        'issue_category': '',
        'sentiment': '',
        'escalation_reason': '',
        'resolution_status': '',
        'agent_notes': []
    }, config1)
    
    print(f"✅ Result: {result1['resolution_status']}")
    print(f"📊 Category: {result1['issue_category']} | Priority: {result1['ticket_priority']} | Sentiment: {result1['sentiment']}")
    if result1['escalation_reason']:
        print(f"🔼 Escalation: {result1['escalation_reason']}")
    print(f"💬 Final Response: {result1['messages'][-1].content[:150]}...")
    
    # Demo Scenario 2: Technical Issue - Standard Customer
    print("\n🔧 Scenario 2: Standard Customer - Technical Issue")
    print("-" * 50)
    
    config2 = {'configurable': {'thread_id': 'demo-tech-standard'}}
    
    result2 = customer_service_graph.invoke({
        'messages': [HumanMessage(content="Hi, I'm having trouble logging into my account. The app keeps showing an error message when I try to sign in.")], 
        'customer_info': {},
        'ticket_priority': '',
        'issue_category': '',
        'sentiment': '',
        'escalation_reason': '',
        'resolution_status': '',
        'agent_notes': []
    }, config2)
    
    print(f"✅ Result: {result2['resolution_status']}")
    print(f"📊 Category: {result2['issue_category']} | Priority: {result2['ticket_priority']} | Sentiment: {result2['sentiment']}")
    print(f"💬 Final Response: {result2['messages'][-1].content[:150]}...")
    
    # Demo Scenario 3: General Inquiry - Positive Customer
    print("\n😊 Scenario 3: Happy Customer - General Inquiry")
    print("-" * 50)
    
    config3 = {'configurable': {'thread_id': 'demo-general-positive'}}
    
    result3 = customer_service_graph.invoke({
        'messages': [HumanMessage(content="Hello! I love your service so far. I just wanted to ask about upgrading my account to get more features. What options are available?")], 
        'customer_info': {},
        'ticket_priority': '',
        'issue_category': '',
        'sentiment': '',
        'escalation_reason': '',
        'resolution_status': '',
        'agent_notes': []
    }, config3)
    
    print(f"✅ Result: {result3['resolution_status']}")
    print(f"📊 Category: {result3['issue_category']} | Priority: {result3['ticket_priority']} | Sentiment: {result3['sentiment']}")
    print(f"💬 Final Response: {result3['messages'][-1].content[:150]}...")
    
    # Demo Scenario 4: Repeat Customer with Complaint
    print("\n😤 Scenario 4: Repeat Customer - Service Complaint")
    print("-" * 50)
    
    config4 = {'configurable': {'thread_id': 'demo-complaint-repeat'}}
    
    result4 = customer_service_graph.invoke({
        'messages': [HumanMessage(content="This is my fourth time contacting support about the same problem. I'm very dissatisfied with the service quality and I'm considering canceling my subscription.")], 
        'customer_info': {},
        'ticket_priority': '',
        'issue_category': '',
        'sentiment': '',
        'escalation_reason': '',
        'resolution_status': '',
        'agent_notes': []
    }, config4)
    
    print(f"✅ Result: {result4['resolution_status']}")
    print(f"📊 Category: {result4['issue_category']} | Priority: {result4['ticket_priority']} | Sentiment: {result4['sentiment']}")
    if result4['escalation_reason']:
        print(f"🔼 Escalation: {result4['escalation_reason']}")
    print(f"💬 Final Response: {result4['messages'][-1].content[:150]}...")
    
    print("\n" + "=" * 60)
    print("🎯 Demo Complete! Visual Workflow Features Demonstrated:")
    print("   • Multi-node workflow visualization")
    print("   • Conditional routing (escalation logic)")
    print("   • State management across nodes")
    print("   • Real-time execution tracking")
    print("   • Message flow visualization")
    print("   • Agent notes and metadata display")
    print("\n🌐 Access LangGraph Studio at: http://127.0.0.1:8123")
    print("📊 View traces at: https://eu.smith.langchain.com/o/fb2e6235-a27a-4a33-bd77-7c865b6d5252")
    print("=" * 60)

def print_visual_workflow_info():
    """
    Print information about the visual workflow structure for the demo.
    """
    print("\n🎨 LangGraph Studio Visual Workflow Structure:")
    print("=" * 50)
    print("START")
    print("  ↓")
    print("📋 Customer Identification")
    print("  ↓")
    print("😊 Sentiment Analysis")
    print("  ↓")
    print("🏷️  Issue Categorization")
    print("  ↓")
    print("📚 Knowledge Base Search")
    print("  ↓")
    print("🔀 Escalation Router")
    print("  ↓")
    print("  ├─ (if escalation needed) → 🔼 Escalation → END")
    print("  └─ (if no escalation) → ✅ Resolution → END")
    print("\n🎯 Key Visual IDE Features:")
    print("• Real-time node execution highlighting")
    print("• State inspection at each step")
    print("• Message flow visualization")
    print("• Conditional edge routing display")
    print("• Agent notes and metadata tracking")
    print("• Interactive debugging capabilities")

if __name__ == "__main__":
    print_visual_workflow_info()
    asyncio.run(run_demo_scenarios())







