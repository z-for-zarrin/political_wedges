import { useState } from 'react';
import Graph from "../components/Graph";
import GraphInput from "../components/GraphInput";

const GraphContainer = () => {

    const[group1Id, setGroup1Id] = useState(null);
    const[group1Name, setGroup1Name] = useState("");
    const[group2Id, setGroup2Id] = useState(null);
    const[group2Name, setGroup2Name] = useState("");
    const[question, setQuestion] = useState(null);

    return (
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
    );
}

export default GraphContainer;