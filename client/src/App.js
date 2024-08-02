import { createHashRouter, RouterProvider } from 'react-router-dom';
import './App.css'
import GraphContainer from './containers/GraphContainer.js';
import About from './components/About.js';
import Explanation from './components/Explanation.js';
import Navigation from './components/Navigation.js';
import NotFound from './components/NotFound.js';

function App() {

  const wedgeRoutes = createHashRouter([
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
            },
            {
                path: "*",
                element: <NotFound />
            }
      ]
    }
  ]);

  return (
    <>
      <RouterProvider router={wedgeRoutes} />   
      <footer>
        <p>&copy; Joey Cartwright & Zarrin Rahman 2024</p>
      </footer>
    </>
  );
}

export default App;
