"""
LangGraph Cloud Deployment Configuration
Optimized for cloud deployment with full Visual IDE support
"""

import os
from typing import Dict, Any

# Cloud deployment settings
DEPLOYMENT_CONFIG = {
    "project_name": "AI-LAB-Customer-Service-Dev",
    "description": "Customer service AI agent with sophisticated routing and coordination",
    "version": "2.0.0",
    "environment": "production",
    
    # LangSmith configuration for cloud
    "langsmith": {
        "endpoint": "https://eu.api.smith.langchain.com",
        "organization_id": "fb2e6235-a27a-4a33-bd77-7c865b6d5252",
        "project_name": "AI-LAB-Customer-Service-Dev",
        "tracing_enabled": True
    },
    
    # Graph configurations
    "graphs": {
        "enhanced_multi_agent": {
            "description": "Sophisticated multi-agent orchestration system",
            "entry_point": "./langgraph_cloud_config.py:enhanced_multi_agent_graph",
            "features": [
                "multi_agent_coordination",
                "dynamic_routing", 
                "specialized_agents",
                "visual_workflow",
                "cloud_optimized"
            ]
        },
        "customer_service": {
            "description": "Customer service workflow with escalation handling",
            "entry_point": "./customer_service_agent.py:customer_service_graph",
            "features": [
                "sentiment_analysis",
                "escalation_logic",
                "knowledge_base_integration"
            ]
        },
        "my_agent": {
            "description": "Simple conversational agent",
            "entry_point": "./my_agent/graph.py:graph",
            "features": [
                "basic_conversation",
                "memory_persistence"
            ]
        }
    },
    
    # Performance optimization
    "performance": {
        "concurrent_executions": 100,
        "timeout_seconds": 300,
        "memory_limit_mb": 1024,
        "auto_scaling": True
    },
    
    # Visual IDE optimization
    "visual_ide": {
        "real_time_updates": True,
        "state_inspection": True,
        "flow_visualization": True,
        "debug_mode": True,
        "performance_metrics": True
    }
}

def get_cloud_environment_variables() -> Dict[str, str]:
    """
    Returns environment variables optimized for cloud deployment.
    """
    return {
        "LANGCHAIN_TRACING_V2": "true",
        "LANGCHAIN_ENDPOINT": "https://eu.api.smith.langchain.com",
        "LANGSMITH_ENDPOINT": "https://eu.api.smith.langchain.com",
        "LANGCHAIN_PROJECT": "AI-LAB-Customer-Service-Dev",
        "LANGCHAIN_ORGANIZATION_ID": "fb2e6235-a27a-4a33-bd77-7c865b6d5252",
        
        # Performance settings
        "LANGGRAPH_CLOUD_TIMEOUT": "300",
        "LANGGRAPH_MAX_CONCURRENT": "100",
        "LANGGRAPH_MEMORY_LIMIT": "1024",
        
        # Visual IDE settings
        "LANGGRAPH_VISUAL_UPDATES": "true",
        "LANGGRAPH_DEBUG_MODE": "true",
        "LANGGRAPH_METRICS": "true"
    }

def validate_deployment_config() -> bool:
    """
    Validates the deployment configuration.
    """
    required_env_vars = [
        "LANGSMITH_API_KEY",
        "LANGCHAIN_ORGANIZATION_ID"
    ]
    
    missing_vars = []
    for var in required_env_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print(f"❌ Missing required environment variables: {missing_vars}")
        return False
    
    print("✅ Deployment configuration validated successfully")
    return True

# Export configuration
__all__ = ["DEPLOYMENT_CONFIG", "get_cloud_environment_variables", "validate_deployment_config"]







