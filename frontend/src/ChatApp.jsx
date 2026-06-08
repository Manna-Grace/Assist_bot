import React, { useState, useRef, useEffect } from 'react';
import './ChatApp.css'; // We'll define the smooth UI here

export default function ChatApp() {
  const [messages, setMessages] = useState([
    { sender: 'bot', text: 'Welcome to Whiff n Whisk! I am your store assistant. How can I help you today?' }
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  
  const chatEndRef = useRef(null);

  // Auto-scroll to bottom when messages change
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isTyping]);

  const handleSend = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userText = input.trim();
    setInput('');
    
    // Add user message to UI
    setMessages(prev => [...prev, { sender: 'user', text: userText }]);
    setIsTyping(true);

    try {
      // Connect to your FastAPI backend
      const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: userText })
      });

      const data = await response.json();
      
      if (response.ok) {
        setMessages(prev => [...prev, { sender: 'bot', text: data.reply }]);
      } else {
        setMessages(prev => [...prev, { sender: 'bot', text: 'Oops, the server returned an error.' }]);
      }
    } catch (error) {
      console.error("Fetch error:", error);
      setMessages(prev => [...prev, { sender: 'bot', text: 'Error: Could not connect to the API. Is FastAPI running?' }]);
    } finally {
      setIsTyping(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        Whiff n Whisk Assistant
      </div>
      
      <div className="chat-box">
        {messages.map((msg, index) => (
          <div key={index} className={`message-wrapper ${msg.sender}`}>
            <div className={`message ${msg.sender}`}>
              {msg.text}
            </div>
          </div>
        ))}
        
        {isTyping && (
          <div className="message-wrapper bot">
            <div className="message bot typing-indicator">
              <span>.</span><span>.</span><span>.</span>
            </div>
          </div>
        )}
        <div ref={chatEndRef} />
      </div>

      <form className="input-area" onSubmit={handleSend}>
        <input 
          type="text" 
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..." 
          disabled={isTyping}
        />
        <button type="submit" disabled={isTyping || !input.trim()}>
          Send
        </button>
      </form>
    </div>
  );
}