import React from 'react';
import { Admin, Resource } from 'react-admin';
import jsonServerProvider from 'ra-data-json-server';

const dataProvider = jsonServerProvider('http://jsonplaceholder.typicode.com');
const App: React.FC = () => (
    <Admin dataProvider={dataProvider}>
        {/* Define your resources here */}
    </Admin>
);

export default App;
