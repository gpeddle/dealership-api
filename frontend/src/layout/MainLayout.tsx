// Layout.tsx
import * as React from 'react';
import { Layout } from 'react-admin';
import MainAppBar from './MainAppBar';

const MainLayout = (props: any) => <Layout {...props} appBar={MainAppBar} />;

export default MainLayout;
