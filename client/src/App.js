import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './App.css';
import logo from './assets/logo-title.png'
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
        <img src={logo} alt='logo' id='logo'/>
      </header>
      <RouterProvider router={wedgeRoutes} />
      <footer>
        <p>&copy; Joey Cartwright & Zarrin Rahman 2024</p>
      </footer>
    </>
  );
}

export default App;
