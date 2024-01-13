import { Datagrid, List, TextField } from 'react-admin';

const ConfigList = () => (
    <List>
        <Datagrid rowClick="edit">
            <TextField source="id" />
            <TextField source="name" />
        </Datagrid>
    </List>
);


export default ConfigList;