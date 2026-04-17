import React, { useState, useRef, useEffect } from 'react';

function App() {
  const [messages, setMessages] = useState([
    { role: 'bot', content: 'Welcome to the AI Assistant. How can I help you today?' }
  ]);
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isTyping]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage = input.trim();
    setInput('');
    setMessages(prev => [...prev, { role: 'user', content: userMessage }]);
    setIsTyping(true);

    try {
      const response = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
      });
      
      const data = await response.json();
      
      // Artificial slight delay to make it feel natural
      setTimeout(() => {
        setMessages(prev => [...prev, { role: 'bot', content: data.response }]);
        setIsTyping(false);
      }, 500);

    } catch (error) {
      console.error('Error fetching chat response:', error);
      setMessages(prev => [...prev, { role: 'bot', content: 'Sorry, I am having trouble connecting to the server right now.' }]);
      setIsTyping(false);
    }
  };

  return (
    <>
      <div className="bg-blobs">
        <div className="blob blob-1"></div>
        <div className="blob blob-2"></div>
        <div className="blob blob-3"></div>
      </div>
      
      <div className="app-container">
        <div className="chat-window">
          <div className="chat-header">
            <div className="bot-avatar-header">
              🤖
              <div className="status-dot"></div>
            </div>
            <div className="header-info">
              <h1>SkillBot AI</h1>
              <p>Online & Ready to help</p>
            </div>
          </div>
          
          <div className="chat-messages">
            {messages.map((msg, idx) => (
              <div key={idx} className={`message-wrapper ${msg.role}`}>
                {msg.role === 'bot' && <div className="avatar-small bot">🤖</div>}
                <div className={`message ${msg.role}`}>
                  {msg.content}
                </div>
                {msg.role === 'user' && <div className="avatar-small user">👤</div>}
              </div>
            ))}
            
            {isTyping && (
              <div className="message-wrapper bot">
                <div className="avatar-small bot">🤖</div>
                <div className="message bot">
                  <div className="typing-indicator">
                    <div className="typing-dot"></div>
                    <div className="typing-dot"></div>
                    <div className="typing-dot"></div>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <div className="chat-input-container">
            <form onSubmit={handleSubmit} className="chat-form">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask me anything..."
                className="chat-input"
                disabled={isTyping}
                autoFocus
              />
              <button type="submit" className="send-button" disabled={!input.trim() || isTyping}>
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
                  <line x1="22" y1="2" x2="11" y2="13"></line>
                  <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
                </svg>
              </button>
            </form>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;
