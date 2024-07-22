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
        path: '/',
        element: <Navigation />,
        children: [ 
            {
                path: "/",
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
    </>
  );
}

export default App;
