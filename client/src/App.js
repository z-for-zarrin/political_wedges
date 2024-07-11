import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './App.css';
import GraphContainer from './containers/GraphContainer.js';
import About from './components/About.js';
import Explanation from './components/Explanation.js';
import Navigation from './components/Navigation.js';
import NotFound from './components/NotFound.js';

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
      <header className="header">
        <h1>Wedgesite</h1>
      </header>
      <RouterProvider router={wedgeRoutes} />
    </>
  );
}

export default App;
