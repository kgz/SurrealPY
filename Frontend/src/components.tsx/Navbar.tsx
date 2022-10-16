import { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/esm/Nav';
import Offcanvas from 'react-bootstrap/esm/Offcanvas';
import BNavbar from 'react-bootstrap/Navbar';
import { Link, NavLink } from 'react-router-dom';
import styles from './Navbar.module.scss';
import User from './User';

const navClass = (navData: { isActive: any; }) => (navData.isActive ? styles.link + ' ' + styles.active : styles.link);

function Navbar() {

    const [show , setShow] = useState(false);


    return (
        <BNavbar bg="dark" variant='dark' expand='md'>
            <Container className={styles.navbar}>
                <NavLink className={styles.title} to="/" end><h2>My Camino</h2></NavLink>
                <BNavbar.Toggle onClick={()=>setShow(!show)} />
                <BNavbar.Offcanvas placement='end' className='bg-dark text-light' show={show} >
                    <Offcanvas.Header>
                        <Offcanvas.Title id={`offcanvasNavbarLabel-expand-md`} >
                            Menu
                        </Offcanvas.Title>
                        <button type="button" className="btn-close btn-close-white text-reset" color='white' data-bs-dismiss="offcanvas" aria-label="Close" onClick={()=>setShow(!show)}></button>
                        
                       
                    </Offcanvas.Header>
                    <div className='d-md-none p-3'>
                            <User setShow={setShow}/>
                            <hr/>
                        </div>
                    <Offcanvas.Body className='d-flex justify-content-between'>
                        <Nav variant='dark'>
                            <NavLink onClick={()=>setShow(false)} className={navClass} to="/" end>Home</NavLink>
                            <NavLink onClick={()=>setShow(false)} className={navClass} to="/test1">Test 1</NavLink>
                            <NavLink onClick={()=>setShow(false)} className={navClass} to="/test2">Test 2</NavLink>
                        </Nav>
                        <div className='d-none d-md-block'>
                            <User setShow={setShow}/>
                        </div>
                    </Offcanvas.Body>
                </BNavbar.Offcanvas>
            </Container>
        </BNavbar>
    );
}

export default Navbar;