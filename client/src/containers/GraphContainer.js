import { useState } from 'react';
import GraphInput from "../components/GraphInput";

const GraphContainer = () => {

    const[group1Id, setGroup1Id] = useState(null);
    const[group2Id, setGroup2Id] = useState(null);
    const[question, setQuestion] = useState(null);
    const[graphSrc, setGraphSrc] = useState("");

    const postGraph = async (parameters) => {
        const response = await fetch("https://political-wedges-79f88a2118a5.herokuapp.com/generate-graph", {
            method: "POST",
            headers: {"Content-Type": "application/json",},
            body: JSON.stringify(parameters),
        });
        const graphData = await response.json();
        setGraphSrc(graphData.graph);
    }

    return (
        <section className='page'>
            <section id='graph-creation-guide'>
                <h3>Welcome!</h3>
                <h4>Wondering where to start?</h4>
                <p>For some interesting shapes, try the following:</p>
                <ol id='suggestions'>
                    <li>Green Party vs Reform Party leaners on 'For some crimes, the death penalty is the most appropriate sentence' (from 'Law and Order')</li>
                    <i>Can you find an example with a higher polarisation value?</i>
                    <li>High vs Low Income people on 'Governments should redistribute income...' (from 'Finance and Economics')</li>
                    <i>How does the polarisation compare to what you expected? Now try some of the Law and Order questions for High vs Low Income.</i>
                    <li>High vs Low Income on the issue of transgender people being allowed to change their birth certificates (from 'Gender and Sexual Minorities')</li>
                    <i>Why do you think the 'jump' in the middle occurs?</i>
                </ol>
            </section>
            <GraphInput
                group1Id={group1Id}
                setGroup1Id={setGroup1Id}
                group2Id={group2Id}
                setGroup2Id={setGroup2Id}
                question={question}
                setQuestion={setQuestion}
                postGraph={postGraph} />
            {graphSrc ? 
            <>
                <img id="graph" src={"data:image/jpeg;base64," + graphSrc} alt='polarisation parallelogram graph'/>
                <p className='citation'>Data from NatCen Social Research. (2023). British Social Attitudes Survey, 2021. [data collection]. UK Data Service. SN: 9072, DOI: http://doi.org/10.5255/UKDA-SN-9072-1</p>
            </>
            : null}
            
        </section>
    );
}

export default GraphContainer;