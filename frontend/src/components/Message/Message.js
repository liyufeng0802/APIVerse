import React from 'react';
import {ListItem, ListItemText} from '@mui/material';
import './Message.css';


function Message({message}) {
    const isUserMessage = message.sender === 'user';
    const backgroundColor = isUserMessage ? '#e0f7fa' : '#fff9c4';
    const fontStyle = isUserMessage ? 'normal' : 'italic';
    const align = isUserMessage ? 'right' : 'left';

    return (
        <ListItem className={`message ${align}`} alignItems="flex-start">
            <ListItemText
                primary={message.text}
                sx={{backgroundColor, borderRadius: '10px', padding: '8px', fontStyle}}
            />
        </ListItem>
    );
}

export default Message;
