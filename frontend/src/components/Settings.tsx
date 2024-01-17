// in src/Settings.js
import * as React from "react";
import { Card, CardContent } from '@mui/material';
import { Title } from 'react-admin';
import { AppName } from "../App";

const Settings = () => (
    <Card>
        <Title title="Settings" />
        <CardContent>
            <p>This is the settings page.</p>
        </CardContent>
    </Card>
);

export default Settings;