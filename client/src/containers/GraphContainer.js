import { useState } from 'react';
import Graph from "../components/Graph";
import GraphInput from "../components/GraphInput";

const GraphContainer = () => {

    const[group1Id, setGroup1Id] = useState(null);
    const[group2Id, setGroup2Id] = useState(null);
    const[question, setQuestion] = useState(null);
    const[graphSrc, setGraphSrc] = useState("");

    const postGraph = async (parameters) => {
        const response = await fetch("http://192.168.1.127:8000/generate-graph/", {
            method: "POST",
            headers: {"Content-Type": "application/json",},
            body: JSON.stringify(parameters),
        });
        const graphData = await response.json();
        setGraphSrc(graphData.graph);
    }

    return (
        <section className='page'>
            Make a graph!
            <GraphInput
                group1Id={group1Id}
                setGroup1Id={setGroup1Id}
                group2Id={group2Id}
                setGroup2Id={setGroup2Id}
                question={question}
                setQuestion={setQuestion}
                postGraph={postGraph} />
            {graphSrc ? <img id="graph" src={"data:image/jpeg;base64," + graphSrc} /> : null}
            
        </section>
    );
}

export default GraphContainer;