import React, { useEffect, useRef } from 'react';
import { List } from '@mui/material';
import './MessageList.css';
import Message from '../Message/Message';


function MessageList({ messages }) {
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  return (
    <List className="message-list">
      {messages.map((message, index) => (
        <Message key={index} message={message} />
      ))}
      <div ref={messagesEndRef} />
    </List>
  );
}

export default MessageList;
