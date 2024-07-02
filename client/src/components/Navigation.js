import { Link, Outlet } from "react-router-dom";

const Navigation = () => {
    return(
        <>
            <nav>
                <ul>
                    <li><Link to='/create'>Make a graph</Link></li>
                    <li><Link to='/how-it-works'>How it works</Link></li>
                    <li><Link to='/about-us'>About us</Link></li>
                </ul>
            </nav>
            <Outlet />
        </>
    );
}

export default Navigation;