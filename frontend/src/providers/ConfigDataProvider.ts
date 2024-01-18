import jsonServerProvider from 'ra-data-json-server';
import { fetchUtils } from 'react-admin';

const httpClient = fetchUtils.fetchJson;

const createConfigDataProvider = (apiUrl: string) => {
    const dataProvider = jsonServerProvider(apiUrl, httpClient);

    // Override the getOne method
    dataProvider.getOne = (resource, params) => {
        // include id (which should be the filename) in the result
        const url = `${apiUrl}/${resource}/${params.id}`;
        return httpClient(url).then(({ json }) => ({
            data: { ...json, id: params.id } // Keep id as is
        }));
    };    

    return dataProvider;
};

export default createConfigDataProvider;
