import { DateInput, Edit, SimpleForm, TextInput } from 'react-admin';

export const ConfigEdit = () => (
    <Edit>
        <SimpleForm>
            <TextInput source="id" />
            <TextInput source="name" />
            <TextInput source="path" />
            <TextInput source="description" />
            <TextInput source="version" />
            <DateInput source="created" />
            <DateInput source="updated" />
        </SimpleForm>
    </Edit>
);

export default ConfigEdit;