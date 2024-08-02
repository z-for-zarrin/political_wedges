import { Link, Outlet } from "react-router-dom";
import logo from '../assets/logo-title.png'

const Navigation = () => {
    return(
        <>
            <header className="header">
                <Link to='/'>
                    <img src={logo} alt='logo' id='logo'/>            
                </Link>
            </header>
            <nav>
                <ul>
                    <li className="nav-item"><Link to='/'>Make a graph</Link></li>
                    <li className="nav-item"><Link to='/how-it-works'>How it works</Link></li>
                    <li className="nav-item"><Link to='/about-us'>About us</Link></li>
                </ul>
            </nav>
            <Outlet />
        </>
    );
}

export default Navigation;