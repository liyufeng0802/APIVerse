import React, {useState} from 'react';
import {Container} from '@mui/material';
import './ChatContainer.css';
import InputArea from '../InputArea/InputArea';
import MessageList from '../MessageList/MessageList';

function ChatContainer() {
    const [messages, setMessages] = useState([]);
    const [isBotTyping, setIsBotTyping] = useState(false);

    const handleSendMessage = (messageText) => {
        setIsBotTyping(true);  // Set typing indicator on
        setTimeout(() => {
            setIsBotTyping(false);  // Set typing indicator off
            if (messageText.trim()) {
                const newMessage = {text: messageText.trim(), sender: 'user'};
                setMessages([...messages, newMessage]);
                handleBotResponse(messageText.trim());
            }
        }, 500);
    };

    const handleBotResponse = (userMessage) => {
      // Simulate a delay for bot response
      setTimeout(() => {
        let botResponseText = 'Hello, how can I assist you?';
        if (userMessage.toLowerCase().includes('hello')) {
          botResponseText = 'Hello! How can I help you today?';
        } else if (userMessage.toLowerCase().includes('help')) {
          botResponseText = 'Of course! What do you need help with?';
        }
        const botResponse = { text: botResponseText, sender: 'bot' };
        setMessages(prevMessages => [...prevMessages, botResponse]);
      }, 500);
    };

    return (
      <Container maxWidth="sm" className="chat-container">
        <MessageList messages={messages} />
        {isBotTyping && <div className="typing-indicator">Bot is typing...</div>}
        <InputArea onSendMessage={handleSendMessage} />
      </Container>
    );
}

export default ChatContainer;
