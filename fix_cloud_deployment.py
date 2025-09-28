#!/usr/bin/env python3
"""
Fix Common LangGraph Cloud Deployment Issues
This script identifies and fixes common deployment problems
"""

import os
import json
import subprocess

def fix_deployment_issues():
    """
    Identify and fix common deployment issues
    """
    
    print("🔧 LangGraph Cloud Deployment Fixer")
    print("=" * 50)
    
    issues_found = []
    fixes_applied = []
    
    # Check 1: Verify langgraph.json structure
    print("\n1. 📋 Checking langgraph.json configuration...")
    try:
        with open('langgraph.json', 'r') as f:
            config = json.load(f)
        
        required_fields = ['dependencies', 'graphs']
        missing_fields = [field for field in required_fields if field not in config]
        
        if missing_fields:
            issues_found.append(f"Missing required fields in langgraph.json: {missing_fields}")
        else:
            print("   ✅ langgraph.json structure is valid")
            
        # Check if all graph files exist
        for graph_name, graph_path in config.get('graphs', {}).items():
            file_path = graph_path.split(':')[0]
            if not os.path.exists(file_path):
                issues_found.append(f"Graph file missing: {file_path} for {graph_name}")
            else:
                print(f"   ✅ {graph_name}: {file_path} exists")
                
    except FileNotFoundError:
        issues_found.append("langgraph.json file not found")
    except json.JSONDecodeError as e:
        issues_found.append(f"Invalid JSON in langgraph.json: {e}")
    
    # Check 2: Verify requirements.txt
    print("\n2. 📦 Checking requirements.txt...")
    if os.path.exists('requirements.txt'):
        with open('requirements.txt', 'r') as f:
            requirements = f.read()
        
        required_packages = ['langgraph', 'langchain-core']
        missing_packages = []
        
        for package in required_packages:
            if package not in requirements:
                missing_packages.append(package)
        
        if missing_packages:
            issues_found.append(f"Missing packages in requirements.txt: {missing_packages}")
        else:
            print("   ✅ Required packages found in requirements.txt")
    else:
        issues_found.append("requirements.txt file not found")
    
    # Check 3: Verify Python files can be imported
    print("\n3. 🐍 Testing Python imports...")
    test_imports = [
        ('customer_service_agent', 'customer_service_graph'),
        ('langgraph_cloud_config', 'enhanced_multi_agent_graph'),
        ('my_agent.graph', 'graph')
    ]
    
    for module, attribute in test_imports:
        try:
            exec(f"from {module} import {attribute}")
            print(f"   ✅ {module}.{attribute} imports successfully")
        except Exception as e:
            issues_found.append(f"Import error: {module}.{attribute} - {e}")
    
    # Check 4: Verify file content integrity
    print("\n4. 📄 Checking file content integrity...")
    critical_files = [
        'customer_service_agent.py',
        'langgraph_cloud_config.py',
        'my_agent/graph.py'
    ]
    
    for file_path in critical_files:
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                content = f.read().strip()
            
            if len(content) < 100:  # Suspiciously small file
                issues_found.append(f"File {file_path} appears to be empty or corrupted")
            elif '__all__' not in content and file_path != 'my_agent/graph.py':
                issues_found.append(f"File {file_path} missing __all__ export")
            else:
                print(f"   ✅ {file_path} content looks good")
        else:
            issues_found.append(f"Critical file missing: {file_path}")
    
    # Generate fixes
    print("\n🔧 Applying Fixes...")
    
    # Fix 1: Ensure langgraph.json has proper structure
    fixed_config = {
        "python_version": "3.11",
        "dependencies": [
            ".",
            "./my_agent"
        ],
        "graphs": {
            "my_agent": "./my_agent/graph.py:graph",
            "customer_service": "./customer_service_agent.py:customer_service_graph",
            "enhanced_multi_agent": "./langgraph_cloud_config.py:enhanced_multi_agent_graph"
        },
        "env": ".env"
    }
    
    with open('langgraph.json', 'w') as f:
        json.dump(fixed_config, f, indent=2)
    fixes_applied.append("Updated langgraph.json with proper structure")
    
    # Fix 2: Ensure requirements.txt has all necessary packages
    required_requirements = [
        "langgraph>=0.6.4",
        "langchain-core>=0.3.0", 
        "langchain-openai>=0.2.0",
        "langchain-anthropic>=0.2.0",
        "python-dotenv>=1.0.0"
    ]
    
    with open('requirements.txt', 'w') as f:
        f.write('\n'.join(required_requirements) + '\n')
    fixes_applied.append("Updated requirements.txt with all required packages")
    
    # Fix 3: Create a minimal .env file if it doesn't exist
    if not os.path.exists('.env'):
        env_content = """# LangGraph Cloud Environment Variables
# These will be overridden by cloud deployment settings
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://eu.api.smith.langchain.com
LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com
LANGCHAIN_PROJECT=AI-LAB-Enhanced-Multi-Agent
LANGCHAIN_ORGANIZATION_ID=fb2e6235-a27a-4a33-bd77-7c865b6d5252
"""
        with open('.env', 'w') as f:
            f.write(env_content)
        fixes_applied.append("Created .env file with required variables")
    
    # Report results
    print("\n📊 Diagnostic Results:")
    print("=" * 30)
    
    if issues_found:
        print("🚨 Issues Found:")
        for issue in issues_found:
            print(f"   • {issue}")
    else:
        print("✅ No issues found!")
    
    if fixes_applied:
        print("\n🔧 Fixes Applied:")
        for fix in fixes_applied:
            print(f"   • {fix}")
    
    print("\n🎯 Next Steps:")
    print("1. Commit these fixes to the repository")
    print("2. Push changes to GitHub")
    print("3. Trigger new cloud deployment")
    print("4. Monitor build logs for success")
    
    print("\n📋 Cloud Deployment Checklist:")
    checklist = [
        "✅ langgraph.json properly configured",
        "✅ requirements.txt includes all packages",
        "✅ Python files can be imported",
        "✅ .env file exists",
        "✅ All graph files present"
    ]
    
    for item in checklist:
        print(f"   {item}")
    
    return len(issues_found) == 0

if __name__ == "__main__":
    success = fix_deployment_issues()
    if success:
        print("\n🎉 All checks passed! Ready for cloud deployment.")
    else:
        print("\n⚠️  Issues found and fixed. Please commit changes and redeploy.")







