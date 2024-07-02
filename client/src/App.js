import { useState } from 'react';
import './App.css';
import Graph from './components/Graph.js';
import GraphInput from './components/GraphInput.js';

function App() {

  const[group1Id, setGroup1Id] = useState(null);
  const[group1Name, setGroup1Name] = useState("");
  const[group2Id, setGroup2Id] = useState(null);
  const[group2Name, setGroup2Name] = useState("");
  const[question, setQuestion] = useState(null);

  return (
    <>
      <header className="header">
        <h1>Wedgesite</h1>
      </header>
      <section>
        <GraphInput
          group1Id={group1Id}
          setGroup1Id={setGroup1Id}
          group1Name={group1Name}
          setGroup1Name={setGroup1Name}
          group2Id={group2Id}
          setGroup2Id={setGroup2Id}
          group2Name={group2Name}
          setGroup2Name={setGroup2Name}
          question={question}
          setQuestion={setQuestion}/>
        <Graph />
      </section>
      <section>
        High level explanation of stuff here
      </section>
      <section>
        Who we are here
      </section>
    </>
  );
}

export default App;
