import { useState } from 'react';
import Graph from "../components/Graph";
import GraphInput from "../components/GraphInput";

const GraphContainer = () => {

    const[group1Id, setGroup1Id] = useState(null);
    const[group2Id, setGroup2Id] = useState(null);
    const[question, setQuestion] = useState(null);

    return (
        <section class='page'>
            Make a graph!
            <GraphInput
                group1Id={group1Id}
                setGroup1Id={setGroup1Id}
                group2Id={group2Id}
                setGroup2Id={setGroup2Id}
                question={question}
                setQuestion={setQuestion}/>
            <Graph />
        </section>
    );
}

export default GraphContainer;