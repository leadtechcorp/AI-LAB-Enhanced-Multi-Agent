#!/bin/bash

# LangGraph Studio Startup Script
# This script starts the LangGraph Studio environment for the customer service demo

echo "🚀 Starting LangGraph Studio Environment..."
echo "================================================"

# Check if we're in the right directory
if [ ! -f "langgraph.json" ]; then
    echo "❌ Error: langgraph.json not found. Please run this script from the AI-LAB-langGraph-dev directory."
    exit 1
fi

# Activate virtual environment
echo "📦 Activating virtual environment..."
source .venv/bin/activate

# Check if dependencies are installed
echo "🔍 Checking dependencies..."
python3 -c "import langgraph, langsmith, customer_service_agent" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Dependencies missing. Installing..."
    pip install -r requirements.txt
    pip install langsmith
    pip install -U "langgraph-cli[inmem]"
fi

# Set environment variables
echo "🔧 Setting environment variables..."
export LANGCHAIN_TRACING_V2=true
export LANGSMITH_ENDPOINT=https://eu.api.smith.langchain.com
export LANGCHAIN_ENDPOINT=https://eu.api.smith.langchain.com
export LANGCHAIN_ORGANIZATION_ID=fb2e6235-a27a-4a33-bd77-7c865b6d5252

# Display environment info
echo "✅ Environment configured:"
echo "   • LangSmith Endpoint: $LANGSMITH_ENDPOINT"
echo "   • Organization ID: $LANGCHAIN_ORGANIZATION_ID"
echo "   • Tracing: Enabled"

# Test the customer service agent
echo ""
echo "🧪 Testing customer service agent..."
python3 -c "
from customer_service_agent import customer_service_graph
print('✅ Customer service agent loaded successfully!')
print('📊 Available graphs: my_agent, customer_service')
" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "✅ Agent test passed!"
else
    echo "❌ Agent test failed. Check your configuration."
    exit 1
fi

echo ""
echo "🎯 Starting LangGraph Studio..."
echo "================================================"
echo "📱 Studio URL: http://127.0.0.1:8123"
echo "🌐 LangSmith Dashboard: https://eu.smith.langchain.com/o/fb2e6235-a27a-4a33-bd77-7c865b6d5252"
echo "📚 Documentation: See LANGGRAPH_STUDIO_DEMO.md"
echo ""
echo "🎮 To run demo scenarios:"
echo "   python3 demo_customer_service.py"
echo ""
echo "🛑 To stop the server: Ctrl+C"
echo "================================================"

# Start the LangGraph development server
langgraph dev --host 127.0.0.1 --port 8123







