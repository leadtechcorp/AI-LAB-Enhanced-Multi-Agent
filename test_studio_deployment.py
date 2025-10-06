#!/usr/bin/env python3
"""
Quick test script to verify all graphs are working in LangGraph Studio
"""

import sys

def test_graphs():
    """Test that all graphs can be imported successfully."""
    
    print("🧪 Testing LangGraph Studio Deployment")
    print("=" * 60)
    
    # Test 1: Basic Agent
    try:
        from my_agent.graph import graph
        print("✅ Test 1: Basic Agent (my_agent) - PASSED")
    except Exception as e:
        print(f"❌ Test 1: Basic Agent - FAILED: {e}")
        return False
    
    # Test 2: Customer Service Agent
    try:
        from customer_service_agent import customer_service_graph
        print("✅ Test 2: Customer Service Agent - PASSED")
    except Exception as e:
        print(f"❌ Test 2: Customer Service Agent - FAILED: {e}")
        return False
    
    # Test 3: Enhanced Multi-Agent System
    try:
        from langgraph_cloud_config import enhanced_multi_agent_graph, AGENT_DEFINITIONS
        print("✅ Test 3: Enhanced Multi-Agent System - PASSED")
        print(f"   → {len(AGENT_DEFINITIONS)} specialized agents configured")
    except Exception as e:
        print(f"❌ Test 3: Enhanced Multi-Agent System - FAILED: {e}")
        return False
    
    print("\n" + "=" * 60)
    print("🎉 All graphs loaded successfully!")
    print("\n📊 Available in LangGraph Studio:")
    print("   1. my_agent - Basic conversational agent")
    print("   2. customer_service - Customer service workflow")
    print("   3. enhanced_multi_agent - Advanced multi-agent system")
    print("\n🌐 Access Studio at: http://localhost:8123")
    print("=" * 60)
    
    return True

if __name__ == "__main__":
    success = test_graphs()
    sys.exit(0 if success else 1)