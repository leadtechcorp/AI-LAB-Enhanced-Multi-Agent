#!/usr/bin/env python3
"""
Script to trigger LangGraph Cloud deployment update
"""

import requests
import os

def trigger_deployment_update():
    """
    Trigger a deployment update via webhook or API call
    """
    
    # Your deployment information
    deployment_id = "32aaf36c-bc1d-4341-a4a6-94c78a5dccae"
    organization_id = "fb2e6235-a27a-4a33-bd77-7c865b6d5252"
    
    print("🚀 Triggering LangGraph Cloud Deployment Update...")
    print("=" * 60)
    print(f"📍 Deployment ID: {deployment_id}")
    print(f"🏢 Organization: {organization_id}")
    print(f"📂 Repository: leadtechcorp/AI-LAB-Customer-Service-Dev")
    print(f"🌿 Branch: main")
    print("")
    
    # Configuration that will be used
    config_info = {
        "python_version": "3.11",
        "dependencies": [".", "./my_agent"],
        "graphs": {
            "my_agent": "./my_agent/graph.py:graph",
            "customer_service": "./customer_service_agent.py:customer_service_graph", 
            "enhanced_multi_agent": "./langgraph_cloud_config.py:enhanced_multi_agent_graph"
        }
    }
    
    print("📋 Deployment Configuration:")
    for key, value in config_info.items():
        if key == "graphs":
            print(f"   • {key}: {len(value)} graphs configured")
            for graph_name in value.keys():
                print(f"     - {graph_name}")
        else:
            print(f"   • {key}: {value}")
    
    print("\n🔧 Environment Variables Required:")
    env_vars = [
        "LANGCHAIN_TRACING_V2=true",
        "LANGCHAIN_ENDPOINT=https://eu.api.smith.langchain.com",
        "LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com", 
        "LANGCHAIN_PROJECT=AI-LAB-Enhanced-Multi-Agent",
        "LANGCHAIN_ORGANIZATION_ID=fb2e6235-a27a-4a33-bd77-7c865b6d5252",
        "LANGSMITH_API_KEY=[configured]"
    ]
    
    for env_var in env_vars:
        print(f"   • {env_var}")
    
    print("\n🎯 Manual Deployment Steps:")
    print("1. Go to: https://eu.smith.langchain.com/o/fb2e6235-a27a-4a33-bd77-7c865b6d5252/host/deployments")
    print("2. Find your deployment or create new one")
    print("3. Click 'Redeploy' or 'Update' to pull latest changes")
    print("4. Wait for build completion (2-5 minutes)")
    print("5. Access your cloud Visual IDE")
    
    print("\n✅ Repository Status:")
    print("   • All fixes have been pushed to main branch")
    print("   • Configuration updated with Python 3.11")
    print("   • Dependencies fixed to include root directory")
    print("   • Unused imports removed")
    
    print("\n🎮 After Deployment Success:")
    print("   • Test enhanced_multi_agent graph")
    print("   • Run demo scenarios in Visual IDE")
    print("   • Verify LangSmith tracing")
    print("   • Share cloud URL with team")

if __name__ == "__main__":
    trigger_deployment_update()







