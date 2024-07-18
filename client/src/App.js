import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './App.css';
import logo from './assets/political_wedges_logo_sketch-removebg-preview.png'
import GraphContainer from './containers/GraphContainer.js';
import About from './components/About.js';
import Explanation from './components/Explanation.js';
import Navigation from './components/Navigation.js';

function App() {

  const wedgeRoutes = createBrowserRouter([
    {
        path: "/",
        element: <Navigation />,
        children: [ 
            {
                path: "/create",
                element: <GraphContainer />
            },
            {
                path: "/how-it-works",
                element: <Explanation />
            },
            {
                path: "/about-us",
                element: <About />
            }
      ]
    }
  ]);

  return (
    <>
      <header className="header">
        <h1>Political Wedges</h1>
        <img src={logo} alt='logo' id='logo'/>
      </header>
      <RouterProvider router={wedgeRoutes} />
      <footer>
        <a href="https://www.flaticon.com/free-icons/linkedin" title="linkedin icons">Linkedin icons created by Fathema Khanom - Flaticon</a>
        <a href="https://www.flaticon.com/free-icons/github" title="github icons">Github icons created by Pixel perfect - Flaticon</a>
      </footer>
    </>
  );
}

export default App;
