'use client';
import Card from '@/components/card/Card';
import {
  Accordion,
  AccordionItem,
  AccordionButton,
  AccordionPanel,
  AccordionIcon,
  Box,
  Button,
  Flex,
  Icon,
  Input,
  Link,
  ListItem,
  UnorderedList,
  Modal,
  ModalBody,
  ModalCloseButton,
  ModalContent,
  ModalHeader,
  ModalOverlay,
  Text,
  useColorModeValue,
  useDisclosure,
  useToast,
} from '@chakra-ui/react';
import { useState } from 'react';
import { MdLock } from 'react-icons/md';

function APIModal(props: { setApiKey: any; func_2_call?: any }) {
  const { setApiKey } = props;
  const { isOpen, onOpen, onClose } = useDisclosure();
  const [inputCode, setInputCode] = useState<string>('');

  const textColor = useColorModeValue('navy.700', 'white');
  const grayColor = useColorModeValue('gray.500', 'gray.500');
  const inputBorder = useColorModeValue('gray.200', 'whiteAlpha.200');
  const inputColor = useColorModeValue('navy.700', 'white');
  const link = useColorModeValue('brand.500', 'white');
  const navbarIcon = useColorModeValue('gray.500', 'white');
  const toast = useToast();

  const handleChange = (Event: any) => {
    setInputCode(Event.target.value);
  };

  const handleApiKeyChange = (value: string) => {
    setApiKey(value);

    localStorage.setItem('apiKey', value);
  };
  return (
    <>
      <Button
        onClick={onOpen}
        display="flex"
        variant="api"
        fontSize={'sm'}
        fontWeight="600"
        borderRadius={'45px'}
        mt="0px"
        minH="54px"
        w={{base: '150px', md: '150px'}}
      >
        Import APIs
      </Button>

      <Modal blockScrollOnMount={false} isOpen={isOpen} onClose={onClose}>
        <ModalOverlay />
        <ModalContent bg="none" boxShadow="none">
          <Card textAlign={'center'}>
            <ModalHeader
              fontSize="22px"
              fontWeight={'700'}
              mx="auto"
              textAlign={'center'}
              color={textColor}
            >
              Import available APIs by providing url to API Documentation
            </ModalHeader>
            <ModalCloseButton _focus={{ boxShadow: 'none' }} />
            <ModalBody p="0px">
              <Text
                color={grayColor}
                fontWeight="500"
                fontSize="md"
                lineHeight="28px"
                mb="22px"
              >
                Our LLM streamlines the API understanding process
                by automatically analyzing the content on the documentation
                and extract the the available APIs.
              </Text>
              <Flex mb="20px">
                <Input
                  h="100%"
                  border="1px solid"
                  borderColor={inputBorder}
                  borderRadius="45px"
                  p="15px 20px"
                  me="10px"
                  fontSize="sm"
                  fontWeight="500"
                  _focus={{ borderColor: 'none' }}
                  _placeholder={{ color: 'gray.500' }}
                  color={inputColor}
                  placeholder="url to the documentation"
                  onChange={handleChange}
                  value={inputCode}
                />
                <Button
                  variant="chakraLinear"
                  py="20px"
                  px="16px"
                  fontSize="sm"
                  borderRadius="45px"
                  ms="auto"
                  mb={{ base: '20px', md: '0px' }}
                  w={{ base: '300px', md: '180px' }}
                  h="54px"
                  onClick={() => {
                    inputCode?.includes('http')
                      ? handleApiKeyChange(inputCode)
                      : null;
                    if (inputCode) {
                      toast({
                        title: inputCode?.includes('http')
                          ? `Success! You have upload the url`
                          : !inputCode?.includes('http')
                          ? `Error! You have not upload valid url`
                          : 'Cannot be empty',
                        position: 'top',
                        status: inputCode?.includes('http')
                          ? 'success'
                          : !inputCode?.includes('http')
                          ? `error`
                          : !inputCode
                          ? 'warning'
                          : 'error',
                        isClosable: true,
                      });
                                    //  if status success, then call func_2_call
                      if (inputCode && inputCode.includes('http') && props.func_2_call) {
                        console.log('calling func_2_call');
                        console.log(inputCode);
                        props.func_2_call();
                      }

                      setInputCode('')
                      onClose();
                    }
                  }}
                >
                  Import
                </Button>
              </Flex>
            </ModalBody>
          </Card>
        </ModalContent>
      </Modal>
    </>
  );
}

export default APIModal;
