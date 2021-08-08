import React, {useState} from 'react'
import {Link} from 'react-router-dom'
import {FaBars, FaTimes} from 'react-icons/fa'
import './Navbar.css'
import {Button} from './Button';
import companyLogo from './images/RainChecker-Logo.png'


function Navbar() {
    const [click, setClick] = useState(false);
    const [button, setButton] = useState(true)

    const handleClick = () => setClick(!click);
    const closeMobileMenu = () => setClick(false);

    const showButton = () => {
        if(window.innerWidth <= 960){
            setButton(false);
        } else {
            setButton(true);
        }
        };


    window.addEventListener('resize', showButton);

    return (
        <>
        <div className="navbar">
            <div className="navbar-container container">
                <Link to='/' className="navbar-logo">
                <img src={companyLogo} alt="RainChecker Logo" />
                </Link>
                <div className="menu-icon" onClick={handleClick}>
                {click ? <FaTimes/> : <FaBars/>}
                </div>
                <ul className={click ? 'nav-menu active' : 'nav-menu'}>
                    <li className='nav-item'>
                        <Link to='/' className='nav-links'>
                            Home
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/prices' className='nav-links'>
                            Prices Trends
                        </Link>
                    </li>
                    <li className='nav-item'>
                        <Link to='/wishlist' className='nav-links'>
                            Wishlist
                        </Link>
                    </li>
                    <li className='nav-btn'>
                        {button ? (
                            <Link to='/sign-up' className="btn-link">
                                <Button buttonStyle='btn--outline'>SIGN UP</Button>
                            </Link>
                        ): (
                            <Link to='/sign-up' className="btn-link">
                                <Button buttonStyle='btn--outline'
                                buttonSize='btn--mobile'>
                                    SIGN UP</Button>
                            </Link>
                        )}
                    </li>
                </ul>
            </div>
            <div className="nav-underline"></div>
        </div>
        </>
    )
}

export default Navbar