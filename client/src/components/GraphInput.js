import { useState } from "react";

const GraphInput = ({group1Id, setGroup1Id, group1Name, setGroup1Name,
    group2Id, setGroup2Id, group2Name, setGroup2Name, question, setQuestion
    }) => {

    const[groupKey, setGroupKey] = useState(null);
    const[groupArray, setGroupArray] = useState([]);

    return(
        <form id="parameters-form">
            Form goes here
        </form>
    )
}

export default GraphInput;