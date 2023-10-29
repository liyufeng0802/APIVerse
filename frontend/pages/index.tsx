'use client';
/*eslint-disable*/

import MessageBoxChat from '@/components/MessageBox';
import {ChatBody, OpenAIModel} from '@/types/types';
import {Button, Flex, Icon, Img, Input, Text, useColorModeValue, useDisclosure,} from '@chakra-ui/react';
import {useEffect, useRef, useState} from 'react';
import {MdAutoAwesome, MdPerson} from 'react-icons/md';
import Bg from '../public/img/chat/bg-image.png';
import axios from 'axios';
import APIModal from "@/components/apiModal";

type ChatMessage = {
    type: 'sent' | 'received';
    message: string;
};

type ChatHistory = ChatMessage[];


export default function Chat(props: { apiKeyApp: string }) {
    // *** If you use .env.local variable for your API key, method which we recommend, use the apiKey variable commented below
    const {apiKeyApp} = props;
    // Input States
    const [inputOnSubmit, setInputOnSubmit] = useState<string>('');
    const [inputCode, setInputCode] = useState<string>('');
    // Response message
    const [outputCode, setOutputCode] = useState<string>('');
    // ChatGPT model
    const [model, setModel] = useState<OpenAIModel>('gpt-3.5-turbo');
    // Loading state
    const [loading, setLoading] = useState<boolean>(false);

    const {isOpen, onOpen, onClose} = useDisclosure();

    const [apiDocURL, setURL] = useState('');

    const [chatHistory, setChatHistory] = useState<ChatHistory>([]);

    const messagesEndRef = useRef(null);

    const scrollToBottom = () => {
        // @ts-ignore
        messagesEndRef.current?.scrollIntoView({behavior: "smooth"});
    };

    useEffect(() => {
        scrollToBottom();
    }, [chatHistory]);


    useEffect(() => {
        if (apiDocURL === '') {
            return;
        }
        const msg = `Import documentation from ${apiDocURL}`;
        setInputCode(msg);
    }, [apiDocURL]);


    async function fetchAPIImport() {
        try {
            setLoading(true);
            const response = await axios.get('http://127.0.0.1:105/import', {
                params: {"url": 'https://icanhazdadjoke.com/api#endpoints'},
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            console.log("test0")

            // Accessing the response body
            let data = response.data;

            // Now you can use responseBody as needed
            console.log("123test")
            console.log(data);

            // @ts-ignore
            let summary = data['summary']
            // summary = "123981239812938129389123"

            console.log(summary)


            const newChat: ChatMessage =
                {
                    type: 'sent',
                    message: `Import documentation from ${apiDocURL}`
                };
            setChatHistory((prevChats) => [...prevChats, newChat].filter(chat => chat.message.trim() !== ""));

            setOutputCode(summary);
            const newReply: ChatMessage = {type: 'received', message: summary};
            console.log(newReply)
            setChatHistory((prevChats) => [...prevChats, newReply].filter(chat => chat.message.trim() !== ""));
            setLoading(false);
        } catch (error) {
            console.error('Error fetching data: ', error);
            alert('Something went wrong when fetching from the API. Make sure to use a valid API key.');
        }
    }

    async function fetchAPIQuery(conversation: string[]) {
        try {
            if (conversation.length === 0) {
                return;
            }
            console.log(`Final sent convesation ${conversation}`);
            const response = await axios.post('http://127.0.0.1:105/query', {
                conversation: conversation
            }, {
                headers: {
                    'Content-Type': 'application/json',
                }
            });

            setLoading(true);

            console.log("Query Sent");

            // Accessing the response body
            let data = response.data;

            console.log("Response Received");
            console.log(data);

            let summary = data['summary'];

            console.log(`Here is the summary ${summary}`);

            // set new chat to history
            const newReply: ChatMessage = {type: 'received', message: summary};
            const newHist = [...chatHistory, newReply].filter(chat => chat.message.trim() !== "");
            console.log(`Test chat history: ${newHist}`);
            setChatHistory(newHist);
            setLoading(false);

            // Here, add your logic to handle the response as needed
            // For example, you can update the chat history, set output code, etc.

        } catch (error) {
            console.error('Error fetching data: ', error);
            alert('Something went wrong when fetching from the API. Please check the console for more details.');
        }
    }

    function chatHistoryToConversation(chatHistory: ChatHistory): string[] {
        let conversation: string[] = [];
        for (let i = 0; i < chatHistory.length; i++) {
            conversation.push(chatHistory[i].message);
        }
        console.log(`Conversation transformed: ${conversation}`);
        return conversation;
    }

    const handleTranslate = async () => {
        const apiKey = apiKeyApp;
        setInputOnSubmit(inputCode);

        // Chat post conditions(maximum number of characters, valid message etc.)
        const maxCodeLength = model === 'gpt-3.5-turbo' ? 700 : 700;

        if (!inputCode) {
            alert('Please enter your message.');
            return;
        }

        if (inputCode.length > maxCodeLength) {
            alert(
                `Please enter code less than ${maxCodeLength} characters. You are currently at ${inputCode.length} characters.`,
            );
            return;
        }

        const newChat: ChatMessage = {type: 'sent', message: inputCode};
        console.log(`Test new inserted question: ${newChat.message}`);
        let newHist = [...chatHistory, newChat].filter(chat => chat.message.trim() !== "");
        console.log(`Test chat history: ${newHist}`);

        setOutputCode(' ');
        setLoading(true);
        const controller = new AbortController();
        const body: ChatBody = {
            inputCode,
            model,
            apiKey,
        };

        // fetchData();
        await setChatHistory(newHist);
        await fetchAPIQuery(chatHistoryToConversation(newHist));
        setLoading(false);
    };


    // API Key
    // const [apiKey, setApiKey] = useState<string>(apiKeyApp);
    const borderColor = useColorModeValue('gray.200', 'whiteAlpha.200');
    const inputColor = useColorModeValue('navy.700', 'white');
    const iconColor = useColorModeValue('brand.500', 'white');
    const grayColor = useColorModeValue('gray.500', 'gray.500');

    const bgIcon = useColorModeValue(
        'linear-gradient(180deg, #FBFBFF 0%, #CACAFF 100%)',
        'whiteAlpha.200',
    );
    const brandColor = useColorModeValue('brand.500', 'white');
    const buttonBg = useColorModeValue('white', 'whiteAlpha.100');
    const gray = useColorModeValue('gray.500', 'white');
    const buttonShadow = useColorModeValue(
        '14px 27px 45px rgba(112, 144, 176, 0.2)',
        'none',
    );
    const textColor = useColorModeValue('navy.700', 'white');
    const placeholderColor = useColorModeValue(
        {color: 'gray.500'},
        {color: 'whiteAlpha.600'},
    );

    const handleChange = (Event: any) => {
        setInputCode(Event.target.value);
    };

    return (
        <Flex
            w="100%"
            pt={{base: '70px', md: '0px'}}
            direction="column"
            position="relative"
        >
            <Img
                src={Bg.src}
                position={'absolute'}
                w="350px"
                left="50%"
                top="50%"
                transform={'translate(-50%, -50%)'}
            />
            <Flex
                direction="column"
                mx="auto"
                w={{base: '100%', md: '100%', xl: '100%'}}
                minH={{base: '75vh', '2xl': '85vh'}}
                maxW="1000px"
            >
                {/* Model Change */}
                <Flex direction={'column'} w="100%" mb={outputCode ? '20px' : 'auto'}>
                </Flex>
                {/* Main Box */}
                <Flex direction="column" w="100%" mx="auto" mb={'auto'}>
                    {chatHistory.filter(chat => chat.message.trim() !== "").map((chat, index) => (
                        <Flex key={index} w="100%" align={'center'} mb="10px">
                            <Flex
                                borderRadius="full"
                                justify="center"
                                align="center"
                                bg={chat.type === 'sent' ? 'transparent' : 'linear-gradient(15.46deg, #4A25E1 26.3%, #7B5AFF 86.4%)'}
                                me="20px"
                                h="40px"
                                minH="40px"
                                minW="40px"
                            >
                                <Icon
                                    as={chat.type === 'sent' ? MdPerson : MdAutoAwesome}
                                    width="20px"
                                    height="20px"
                                    color={chat.type === 'sent' ? brandColor : 'white'}
                                />
                            </Flex>
                            <Flex
                                p="22px"
                                border="1px solid"
                                borderColor={borderColor}
                                borderRadius="14px"
                                w="100%"
                                zIndex={'2'}
                            >
                                {chat.type === 'sent' ? (
                                    <Text
                                        color={textColor}
                                        fontWeight="600"
                                        fontSize={{base: 'sm', md: 'md'}}
                                        lineHeight={{base: '24px', md: '26px'}}
                                    >
                                        {chat.message}
                                    </Text>
                                ) : (
                                    <MessageBoxChat output={chat.message}/>
                                )}
                            </Flex>
                        </Flex>
                    ))}
                    <div ref={messagesEndRef}/>
                </Flex>


                {/* Chat Input */}
                <Flex
                    ms={{base: '0px', xl: '60px'}}
                    mt="20px"
                    justifySelf={'flex-end'}
                >
                    <Input
                        minH="54px"
                        h="100%"
                        border="1px solid"
                        borderColor={borderColor}
                        borderRadius="45px"
                        p="15px 20px"
                        me="10px"
                        fontSize="sm"
                        fontWeight="500"
                        _focus={{borderColor: 'none'}}
                        color={inputColor}
                        _placeholder={placeholderColor}
                        placeholder="Type your message here..."
                        onChange={handleChange}
                    />
                    <Button
                        variant="primary"
                        py="20px"
                        px="16px"
                        fontSize="sm"
                        borderRadius="45px"
                        ms="auto"
                        w={{base: '160px', md: '210px'}}
                        h="54px"
                        _hover={{
                            boxShadow:
                                '0px 21px 27px -10px rgba(96, 60, 255, 0.48) !important',
                            bg:
                                'linear-gradient(15.46deg, #4A25E1 26.3%, #7B5AFF 86.4%) !important',
                            _disabled: {
                                bg: 'linear-gradient(15.46deg, #4A25E1 26.3%, #7B5AFF 86.4%)',
                            },
                        }}
                        onClick={() => handleTranslate()}
                        isLoading={loading ? true : false}
                    >
                        Submit
                    </Button>
                    <APIModal setApiKey={setURL} sidebar={true} func_2_call={fetchAPIImport}/>
                </Flex>

                <Flex
                    justify="center"
                    mt="20px"
                    direction={{base: 'column', md: 'row'}}
                    alignItems="center"
                >
                </Flex>
            </Flex>
        </Flex>
    );

}
