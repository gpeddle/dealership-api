import React from 'react';
import { Admin, CustomRoutes, Resource } from 'react-admin';
import { Route } from 'react-router-dom';
//import jsonServerProvider from 'ra-data-json-server';
import { MyLayout as MainLayout } from './layout';
import ConfigList from './components/ConfigList';
import ConfigEdit from './components/ConfigEdit';
import Settings from './components/Settings';
import createConfigDataProvider from './providers/ConfigDataProvider';

// TODO get api from config
//const apiEndpoint = getApiEndpoint();
const apiUrl = "http://127.0.0.1:8000";

export const AppName = "Configuration Manager";

const configDataProvider = createConfigDataProvider(apiUrl); 

const App: React.FC = () => (
  <Admin dataProvider={configDataProvider} title={AppName} layout={MainLayout}>
    <Resource name="config" list={ConfigList} edit={ConfigEdit}/>

    <CustomRoutes>
            <Route path="/settings" element={<Settings />} />
            
        </CustomRoutes>

  </Admin>
);

export default App;

