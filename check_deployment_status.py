#!/usr/bin/env python3
"""
Check LangGraph Cloud Deployment Status
This script helps verify if the last cloud build succeeded
"""

import subprocess
import json
from datetime import datetime, timezone

def check_deployment_status():
    """
    Check the status of the LangGraph Cloud deployment
    """
    
    print("🔍 Checking LangGraph Cloud Deployment Status")
    print("=" * 60)
    
    # Deployment information
    deployment_id = "32aaf36c-bc1d-4341-a4a6-94c78a5dccae"
    organization_id = "fb2e6235-a27a-4a33-bd77-7c865b6d5252"
    repo_url = "https://github.com/leadtechcorp/AI-LAB-Enhanced-Multi-Agent"
    
    print(f"📍 Deployment ID: {deployment_id}")
    print(f"🏢 Organization: {organization_id}")
    print(f"📂 Repository: leadtechcorp/AI-LAB-Enhanced-Multi-Agent")
    
    # Check repository status
    try:
        result = subprocess.run(['git', 'log', '--oneline', '-1'], 
                              capture_output=True, text=True, check=True)
        latest_commit = result.stdout.strip()
        print(f"🔗 Latest Commit: {latest_commit}")
    except subprocess.CalledProcessError:
        print("❌ Could not get git commit information")
    
    # Check when last push occurred
    try:
        result = subprocess.run(['git', 'log', '-1', '--format=%cd', '--date=iso'], 
                              capture_output=True, text=True, check=True)
        last_push_time = result.stdout.strip()
        print(f"⏰ Last Push: {last_push_time}")
    except subprocess.CalledProcessError:
        print("❌ Could not get push timestamp")
    
    print("\n🎯 How to Check Build Status:")
    print("-" * 40)
    
    print("\n1. 📊 Direct Deployment Page:")
    deployment_url = f"https://eu.smith.langchain.com/o/{organization_id}/host/deployments/{deployment_id}"
    print(f"   {deployment_url}")
    print("   Look for:")
    print("   • Build status (Success/Failed/In Progress)")
    print("   • Build logs and error messages")
    print("   • Deployment URL if successful")
    
    print("\n2. 🏗️ All Deployments Page:")
    deployments_url = f"https://eu.smith.langchain.com/o/{organization_id}/host/deployments"
    print(f"   {deployments_url}")
    print("   Check for:")
    print("   • Latest deployment status")
    print("   • Build completion time")
    print("   • Active/inactive status")
    
    print("\n3. 📋 Build Success Indicators:")
    print("   ✅ Status shows 'Active' or 'Running'")
    print("   ✅ Build logs show successful completion")
    print("   ✅ Cloud URL is accessible")
    print("   ✅ All 3 graphs load in Visual IDE")
    print("   ✅ No error messages in deployment logs")
    
    print("\n4. 🚨 Build Failure Indicators:")
    print("   ❌ Status shows 'Failed' or 'Error'")
    print("   ❌ Build logs show dependency errors")
    print("   ❌ Cloud URL returns 404 or 500 errors")
    print("   ❌ Graphs fail to load")
    print("   ❌ Environment variable issues")
    
    print("\n🔧 Expected Configuration:")
    print("-" * 30)
    config = {
        "python_version": "3.11",
        "dependencies": [".", "./my_agent"],
        "graphs": 3,
        "graph_names": ["my_agent", "customer_service", "enhanced_multi_agent"]
    }
    
    for key, value in config.items():
        if key == "graph_names":
            print(f"   • graphs: {config['graphs']} configured")
            for graph in value:
                print(f"     - {graph}")
        else:
            print(f"   • {key}: {value}")
    
    print("\n🌐 Test Your Deployment:")
    print("-" * 25)
    print("If build succeeded, you should be able to:")
    print("1. Access the cloud Visual IDE URL")
    print("2. See all 3 graphs in the interface")
    print("3. Run the enhanced_multi_agent demo")
    print("4. View traces in LangSmith dashboard")
    
    print("\n📊 LangSmith Monitoring:")
    langsmith_url = f"https://eu.smith.langchain.com/o/{organization_id}"
    print(f"   Dashboard: {langsmith_url}")
    print("   • Check for new traces from deployment")
    print("   • Monitor performance metrics")
    print("   • Verify agent routing works")
    
    print("\n🚀 Next Steps Based on Status:")
    print("-" * 35)
    print("✅ If Build Succeeded:")
    print("   • Test the enhanced multi-agent system")
    print("   • Run demo scenarios in cloud Visual IDE")
    print("   • Share deployment URL with team")
    print("   • Monitor performance and usage")
    
    print("\n❌ If Build Failed:")
    print("   • Check build logs for specific errors")
    print("   • Verify environment variables are set")
    print("   • Review langgraph.json configuration")
    print("   • Create new deployment if needed")
    
    print("\n" + "=" * 60)
    print("📞 Quick Status Check Instructions:")
    print("1. Open deployment page in browser")
    print("2. Look for green 'Active' status")
    print("3. Click on deployment URL if available")
    print("4. Test graph functionality")
    print("=" * 60)

if __name__ == "__main__":
    check_deployment_status()
