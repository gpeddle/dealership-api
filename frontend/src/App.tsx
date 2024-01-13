import React from 'react';
import { Admin, Resource, ListGuesser } from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';
import ConfigList from './components/ConfigList';
// TODO get api from config
//const endpoint = getApiEndpoint();

const dataProvider = jsonServerProvider('http://127.0.0.1:8000'); 

const App: React.FC = () => (
  <Admin dataProvider={dataProvider}>
    <Resource name="config" list={ConfigList} />

    {/* Add more resources as needed */}
  </Admin>
);

export default App;
