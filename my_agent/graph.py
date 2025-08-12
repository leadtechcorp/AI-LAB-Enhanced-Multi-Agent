"""
AI LAB LangGraph - Main Graph Definition
A sample conversational AI agent built with LangGraph
"""

import os
from typing import TypedDict, Annotated
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

# Define the state schema
class State(TypedDict):
    messages: Annotated[list, add_messages]
    user_info: dict

def chatbot_node(state: State):
    """
    Main chatbot node that processes user messages and generates responses.
    """
    messages = state["messages"]
    user_info = state.get("user_info", {})
    
    # Get the last message from the user
    last_message = messages[-1] if messages else None
    
    if not last_message:
        response_content = "Hello! I'm the AI LAB assistant. How can I help you today?"
    else:
        # Simple response logic - in a real application, you'd use an LLM here
        user_content = last_message.content if hasattr(last_message, 'content') else str(last_message)
        
        # Basic conversational responses
        if "hello" in user_content.lower() or "hi" in user_content.lower():
            response_content = f"Hello! Welcome to AI LAB. I'm here to assist you. What would you like to know?"
        elif "help" in user_content.lower():
            response_content = "I can help you with various AI and technology questions. Feel free to ask me anything!"
        elif "what" in user_content.lower() and "ai lab" in user_content.lower():
            response_content = "AI LAB is a cutting-edge research and development facility focused on artificial intelligence, machine learning, and advanced technologies."
        elif "bye" in user_content.lower() or "goodbye" in user_content.lower():
            response_content = "Goodbye! Feel free to come back anytime if you have more questions."
        else:
            response_content = f"I understand you said: '{user_content}'. Let me help you with that. Could you provide more specific details about what you're looking for?"
    
    # Create the AI response message
    ai_message = AIMessage(content=response_content)
    
    return {
        "messages": [ai_message],
        "user_info": user_info
    }

def create_graph():
    """
    Create and configure the LangGraph workflow.
    """
    # Create the graph
    workflow = StateGraph(State)
    
    # Add nodes
    workflow.add_node("chatbot", chatbot_node)
    
    # Define the flow
    workflow.add_edge(START, "chatbot")
    workflow.add_edge("chatbot", END)
    
    # Add memory for persistence
    memory = MemorySaver()
    
    # Compile the graph
    app = workflow.compile(checkpointer=memory)
    
    return app

# Create the main graph instance
graph = create_graph()

# Export for LangGraph deployment
__all__ = ["graph"]
