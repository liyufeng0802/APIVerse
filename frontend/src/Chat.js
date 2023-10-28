import React, { useState } from 'react';
import { Container, TextField, Button, List, ListItem, ListItemText } from '@mui/material';

function Chat() {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');

  const handleSendMessage = () => {
    if (inputValue.trim()) {
      setMessages([...messages, { text: inputValue.trim(), sender: 'user' }]);
      setTimeout(() => {
        setMessages([...messages, { text: inputValue.trim(), sender: 'user' }, { text: 'Hello, how can I assist you?', sender: 'bot' }]);
      }, 500);
      setInputValue('');
    }
  };

  return (
    <Container maxWidth="sm">
      <List>
        {messages.map((message, index) => (
          <ListItem key={index} align={message.sender === 'user' ? 'right' : 'left'}>
            <ListItemText primary={message.text} />
          </ListItem>
        ))}
      </List>
      <TextField
        fullWidth
        variant="outlined"
        value={inputValue}
        onChange={(e) => setInputValue(e.target.value)}
        onKeyPress={(e) => { if (e.key === 'Enter') { handleSendMessage(); e.preventDefault(); } }}
      />
      <Button variant="contained" color="primary" onClick={handleSendMessage}>
        Send
      </Button>
    </Container>
  );
}

export default Chat;
