import React from 'react';
import { Admin, Resource, ListGuesser } from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';
// Example of importing the interface in a React component
import { AutomobileBrandInterface, ServiceBayInterface, WorkingHoursInterface } from '../../shared/frontend';


const dataProvider = jsonServerProvider('http://127.0.0.1:8000'); // Replace with your actual backend URL

const App: React.FC = () => (
  <Admin dataProvider={dataProvider}>
    <Resource name="config/automobile_brands" list={ListGuesser} />
    <Resource name="config/service_bays" list={ListGuesser} />
    <Resource name="config/working_hours" list={ListGuesser} />
    {/* Add more resources as needed */}
  </Admin>
);

export default App;
