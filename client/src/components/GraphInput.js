import { useState } from "react";

const GraphInput = ({group1Id, setGroup1Id, group1Name, setGroup1Name,
    group2Id, setGroup2Id, group2Name, setGroup2Name, question, setQuestion}) => {

    const[groupKey, setGroupKey] = useState("");
    const[groupArray, setGroupArray] = useState([]);
    const[questionArray, setQuestionArray] = useState([]);
    
    const characteristics = {
        ageCat:   ["18-34", "35-54", "55+"],
       DVSex21:   ["Female", "Male"],
       partyfw:   ["Conservative", "Labour", "Liberal Democrats", "Scottish National Party",
                   "Plaid Cymru", "Green", "UKIP", "Reform"],
         SRInc:   ["Identify as high income", "Idenitfy as middle income", "Identify as low income"],
      hedqual2:   ["Degree", "No degree"]
    }

    const topics = {
        healthcare: ["question", "question 2"],
        secondTopic: ["question 3", "inquiry"]
    }

    const charChangeHandler = (event) => {
        setGroupArray(characteristics[`${event.target.value}`]);
        setGroupKey(event.target.value);
        setGroup1Id(0);
        setGroup1Name("");
        setGroup2Id(0);
        setGroup2Name("");
    }

    const group1Options = groupArray.map((group, index) => {
        if(index !== group2Id - 1){
            return <option key={index} value={JSON.stringify({index, value:group})}>{group}</option>
        } else {
            return <option key={index} value={group} disabled>{group}</option>
        }
    });
  
    const group2Options = groupArray.map((group, index) => {
        if(index !== group1Id - 1){
            return <option key={index} value={JSON.stringify({index, value:group})}>{group}</option>
        } else {
            return <option key={index} value={group} disabled>{group}</option>
        }
    });

    const topicChangeHandler = (event) => {
        setQuestionArray(topics[`${event.target.value}`]);
        setQuestion("");
    }

    const questionOptions = questionArray.map((questionOption, index) => {
        if(questionOption !== question){
            return <option key={index} value={questionOption}>{questionOption}</option>
        } else {
            return <option key={index} value={questionOption} disabled>{questionOption}</option>
        }
    })

    return(
        <form id="parameters-form">
            <label htmlFor="characteristic-select">Characteristic</label>
            <select
                id="characteristic-select"
                type="text"
                name="characteristic"
                defaultValue=""
                onChange={charChangeHandler}>
                
                <option disabled value="">Select demographic characteristic</option>
                <option value="partyfw">Party Preference</option>
                <option value="ageCat">Age</option>
                <option value="DVSex21">Sex</option>
                <option value="SRInc">Income</option>
                <option value="hedqual2">University Education</option>
            </select>
            <label htmlFor="group-1">Group 1</label>
            <select
                id="group-1"
                type="text"
                name="group1"
                defaultValue={JSON.stringify({index: null, value:""})}
                onChange={(event) => {
                    let obj = JSON.parse(event.target.value);
                    setGroup1Id(obj["index"]+1);
                    setGroup1Name(obj.value);
                }}>
                
                <option disabled value={JSON.stringify({index: null, value:""})}>Select first group</option>
                {group1Options}
            </select>
            <label htmlFor="group-2">Group 2</label>
            <select
                id="group-2"
                type="text"
                name="group2"
                // value={JSON.stringify({index:group1Id, value:group2Name})}
                defaultValue={JSON.stringify({index: null, value:""})}
                onChange={(event) => {
                    let obj = JSON.parse(event.target.value);
                    setGroup2Name(obj.value);
                    setGroup2Id(obj["index"]+1);
                    console.log(group2Name);
                }}>
                
                <option disabled value={JSON.stringify({index: null, value:""})}>Select second group</option>
                {group2Options}
            </select>
            <label htmlFor="topic-select">Characteristic</label>
            <select
                id="topic-select"
                type="text"
                name="topic"
                defaultValue=""
                onChange={topicChangeHandler}>
                
                <option disabled value="">Select topic</option>
                <option value="healthcare">Healthcare</option>
            </select>
            <label htmlFor="question">Question</label>
            <select
                id="question-select"
                type="text"
                name="question"
                defaultValue=""
                onChange={(event) => {
                    setQuestion(event.target.value);
                }}>
                
                <option disabled value="">Select question</option>
                {questionOptions}
            </select>
        </form>
    )
}

export default GraphInput;