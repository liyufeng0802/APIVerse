import React, { useState } from 'react';
import { TextField, Button } from '@mui/material';
import './InputArea.css';


function InputArea({ onSendMessage }) {
  const [inputValue, setInputValue] = useState('');

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleSendMessage = () => {
    onSendMessage(inputValue);
    setInputValue('');
  };

  const handleKeyPress = (event) => {
    if (event.key === 'Enter' && !event.shiftKey) {
      handleSendMessage();
      event.preventDefault();
    }
  };

  return (
    <div className="input-area">
      <TextField
        fullWidth
        variant="outlined"
        value={inputValue}
        onChange={handleInputChange}
        onKeyPress={handleKeyPress}
        placeholder="Type your message..."
      />
      <Button variant="contained" color="primary" onClick={handleSendMessage}>
        Send
      </Button>
    </div>
  );
}

export default InputArea;
