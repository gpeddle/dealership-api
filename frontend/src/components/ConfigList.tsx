import { Datagrid, List, TextField, DateField } from 'react-admin';

const ConfigList = () => (
    <List>
        <Datagrid bulkActionButtons={false}>
            <TextField source="name" />
            <TextField source="filename" />
            <TextField source="version" />
            <DateField source="updated" showTime={true}/>
            
        </Datagrid>
    </List>
);

export default ConfigList;