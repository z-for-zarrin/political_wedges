import { Link, Outlet } from "react-router-dom";

const Navigation = () => {
    return(
        <>
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