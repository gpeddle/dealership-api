// CustomAppBar.tsx
import React from 'react';
import { AppBar, UserMenu, useGetResourceLabel } from 'react-admin';
import { useLocation } from 'react-router-dom';
import Typography from '@mui/material/Typography';
import { AppName } from "../App";

const MyAppBar = (props: any) => {
    const getResourceLabel = useGetResourceLabel();
    const location = useLocation();

    // Extract resource name from the URL
    const resourceName = location.pathname.split('/')[1];
    const resourceLabel = getResourceLabel(resourceName, 2);

    // Format the title
    const title = resourceName ? `${AppName} - ${resourceLabel}` : AppName;

    return (
        <AppBar {...props}>
            <div style={{ flex: 1, display: 'flex', alignItems: 'center' }}>
                <Typography variant="h6" color="inherit">
                    {title}
                </Typography>
            </div>
            <UserMenu />
        </AppBar>
    );
};

export default MyAppBar;
