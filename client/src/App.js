import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import './App.css';
import GraphContainer from './containers/GraphContainer.js';
import About from './components/About.js';
import Explanation from './components/Explanation.js';

function App() {

  const wedgeRoutes = createBrowserRouter([
    {
        path: '/',
        element: <GraphContainer />
    },
    {
        path: '/about-us',
        element: <About />
    },
    {
        path: '/how-it-works',
        element: <Explanation />
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
