import { useState } from "react";

const GraphInput = ({group1Id, setGroup1Id, group1Name, setGroup1Name,
    group2Id, setGroup2Id, group2Name, setGroup2Name, question, setQuestion
    }) => {

    // const[groupKey, setGroupKey] = useState(null);
    const[groupArray, setGroupArray] = useState([]);
    
    const characteristics = {
        ageCat:   ["18-34", "35-54", "55+"],
       DVSex21:   ["Female", "Male"],
       partyfw:   ["Conservative", "Labour", "Liberal Democrats", "Scottish National Party",
                   "Plaid Cymru", "Green", "UKIP", "Reform"],
         SRInc:   ["Identify as high income", "Idenitfy as middle income", "Identify as low income"],
      hedqual2:   ["Degree", "No degree"]
    }
  
    const groupOptions = groupArray.map((group, index) => {
        return <option key={index} value={[index+1, group]}>{group}</option>
    });

    return(
        <form id="parameters-form">
            <label htmlFor="characteristic-select">Characteristic</label>
            <select
                id="characteristic-select"
                type="text"
                name="characteristic"
                defaultValue={""}
                onChange={async (event) => {
                    const groupKey = `${event.target.value}`;
                    setGroupArray(characteristics[groupKey]);
                }}>
                
                <option disabled value="">Select demographic characteristic</option>
                <option value="partyfw">Party Preference</option>
                <option value="ageCat">Age</option>
                <option value="DVSex21">Sex</option>
                <option value="SRInc">Income</option>
                <option value="hedqual2">Education Level</option>
            </select>
            <label htmlFor="group-1"></label>
            <select
                id="group-1"
                type="text"
                name="group1"
                defaultValue={[]}
                onChange={(event) => console.log(event.target.value)}>
                
                <option disabled value="">Select first group</option>
            </select>
        </form>
    )
}

export default GraphInput;