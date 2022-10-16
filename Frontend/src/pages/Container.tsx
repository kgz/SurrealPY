
import React, { useEffect, useState } from 'react';
import ThemeProvider from 'react-bootstrap/esm/ThemeProvider';
import BContainer from 'react-bootstrap/Container';
import Navbar from '../components.tsx/Navbar';
import { Route, Routes } from 'react-router-dom';
import Login from './Login';



const Container: React.FC = () => {


    useEffect(() => {
        console.log(window.user);

    }, [window.user]);
    return (
        <ThemeProvider
            breakpoints={['xxxl', 'xxl', 'xl', 'lg', 'md', 'sm', 'xs', 'xxs']}
            minBreakpoint="xxs"
        >
            <Navbar/>
            <BContainer>
            <Routes>
                <Route index element={<>Home</>}/>
                <Route path="/test1" element={<>Test 1</>} />
                <Route path="/test2" element={<>Test2</>} />
                <Route path="/login" element={<Login/>} />

                {/* Using path="*"" means "match anything", so this route
                        acts like a catch-all for URLs that we don't have explicit
                        routes for. */}
                <Route path="*" element={<>404</>} />
            </Routes>
            </BContainer>

      </ThemeProvider>
    );
};

export default Container;