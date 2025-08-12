#!/usr/bin/env python3
"""
Test script for AI LAB LangGraph Agent
"""

from my_agent.graph import graph
from langchain_core.messages import HumanMessage

def test_agent():
    """Test the LangGraph agent with various inputs."""
    print("🤖 Testing AI LAB LangGraph Agent")
    print("=" * 50)
    
    # Test messages
    test_messages = [
        "Hello!",
        "What is AI LAB?",
        "Can you help me?",
        "Tell me about artificial intelligence",
        "Goodbye"
    ]
    
    config = {'configurable': {'thread_id': 'test-conversation'}}
    
    for i, message in enumerate(test_messages, 1):
        print(f"\n🧪 Test {i}: '{message}'")
        
        try:
            result = graph.invoke({
                'messages': [HumanMessage(content=message)], 
                'user_info': {'test_mode': True}
            }, config)
            
            response = result['messages'][-1].content
            print(f"🤖 Response: {response}")
            
        except Exception as e:
            print(f"❌ Error: {e}")
    
    print("\n✅ All tests completed!")

if __name__ == "__main__":
    test_agent()
