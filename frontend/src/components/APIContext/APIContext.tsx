import React, { createContext, useState, useContext } from 'react';

interface APIContextType {
  apiData: {
    listData: any; // Adjust according to the correct type
    summary: string;
  };
  setApiData: React.Dispatch<React.SetStateAction<APIContextType['apiData']>>;
}

const APIContext = createContext<APIContextType | undefined>(undefined);

export const APIProvider: React.FC = ({ children }) => {
  const [apiData, setApiData] = useState<APIContextType['apiData']>({
    listData: null,
    summary: '',
  });

  return (
    <APIContext.Provider value={{ apiData, setApiData }}>
      {children}
    </APIContext.Provider>
  );
};

export const useAPI = () => {
  const context = useContext(APIContext);
  if (context === undefined) {
    throw new Error('useAPI must be used within an APIProvider');
  }
  return context;
};
