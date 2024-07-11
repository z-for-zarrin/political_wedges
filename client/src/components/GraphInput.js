import { useState } from "react";
import '../styles/GraphStyle.css';

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
        britishValues:      ["On a scale of 1 to 7, with 1 being ‘not at all British’, and 7 ‘being very strongly British’, to what extent do you think of yourself as British?",
                             "The world would be a better place if people from other countries were more like the British",
                             "Generally speaking, Britain is a better country than most other countries",
                             "Young people today don't have enough respect for traditional British values"],
        economics:          ['Overall, it is worthwhile for me to save into a private pension?',
                             'Government should redistribute income from the better-off to those who are less well off',
                             'Big business benefits owners at the expense of workers',
                             "Ordinary working people do not get their fair share of the nation's wealth",
                             'There is one law for the rich and one for the poor',
                             'Management will always try to get the better of employees if it gets the chance'],
        genSexMinorites:   ["If a man and woman have sexual relations before marriage, what would your general opinion be?",
                             "Opinions on sexual relations between two adults of the same sex",
                             "How much do you agree or disagree that a person who is transgender should be able to have the sex recorded on their birth certificate changed if they want?"],
        governance:         ["On a score of 0-10 how much do you personally trust Britain's legal system?*",
                             "On a score of 0-10 how much do you personally trust Britain's Police*",
                             "On a score of 0-10 how much do you personally trust Britain's Politicans?*",
                             "Now that Scotland has its own parliament, Scottish MP’s should no longer be allowed to vote in the House of commons on laws that only affect England"],
        healthcare:         [],
        housingUrban:       ["Would you support or oppose more homes being built in your local area?",
                             "To what extent would you support or oppose requiring people in existing buildings to make changes to their homes to meet new energy regulations, should new homes be built in that area?*",           
                             "To what extent are you in favour of, or against, new cycle lanes in roads being introduced in your area?*",           
                             "To what extent are you in favour of, or against, your local council spending more money to improve existing public transport, although this may mean spending less on other council services?*",           
                             "To what extent are you in favour of, or against, reserving parking spaces for electric car charging points being introduced in your area?*",           
                             "To what extent are you in favour of, or against, building carparks to introduce more “park and ride” routes being introduced in your area?*",           
                             "To what extent are you in favour of, or against, narrowing roads to widen pavements being introduced in your area?*",           
                             "To what extent are you in favour of, or against, closing roads to create pedestrian high streets being introduced in your area?*"],
        law:                ["People who break the law should be given stiffer sentences",
                             "For some crimes, the death penalty is the most appropriate sentence",
                             "Schools should teach children to obey authority",
                             "The law should always be obeyed, even if a particular law is wrong",
                             "Censorship of films and magazines is necessary to uphold moral standards"],
        welfare:            ["Around here, most unemployed people could find a job if they really wanted one",
                             "Many people who get social security don't really deserve any help",
                             "Most people on the dole are fiddling in one way or another",
                             "If welfare benefits weren't so generous, people would learn to stand on their own two feet",
                             "The welfare state encourages people to stop helping each other",
                             "The government should spend more money on welfare benefits for the poor, even if it leads to higher taxes",
                             "Cutting welfare benefits would damage too many people's lives",
                             "The creation of the welfare state is one of Britain's proudest achievements"],
        workplaces:         ["Have attempts to give people with physical impairments an equal chance in the workplace gone too far or not far enough?",
                             "Have attempts to give people with mental health conditions an equal chance in the workplace gone too far or not far enough?",
                             "How strongly do you agree or disagree that, in principle, someone who has been off work with a back problem going back to work quickly will help speed their recovery?*",
                             "How strongly do you agree or disagree that, in principle, someone who has been off work with depression going back to work quickly will help speed their recovery?*"],
        misc:               ["To what extent would you say that online and mobile communication undermines personal privacy?",
                             "To what extent would you say that online and mobile communication exposes people to misinformation?"]
    }

    const charChangeHandler = (event) => {
        setGroupArray(characteristics[`${event.target.value}`]);
        setGroupKey(event.target.value);
        setGroup1Id(0);
        setGroup1Name("");
        document.getElementById("group-1").value=JSON.stringify({index: null, value:""});
        setGroup2Id(0);
        setGroup2Name("");
        document.getElementById("group-2").value=JSON.stringify({index: null, value:""});
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
        return <option key={index} value={questionOption}>{questionOption}</option>
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
            <label htmlFor="topic-select" id="topic-label">Topic</label>
            <select
                id="topic-select"
                type="text"
                name="topic"
                defaultValue=""
                onChange={topicChangeHandler}>
                
                <option disabled value="">Select topic</option>
                <option value="britishValues">British Values and Traditions</option>
                <option value="economics">Finance and Economics</option>
                <option value="genSexMinorites">Gender and Sexual Minorities</option>
                <option value="governance">Governance</option>
                <option value="healthcare">Health and Social Care</option>
                <option value="housingUrban">Housing and Urban Development</option>
                <option value="law">Law and Order</option>
                <option value="welfare">Welfare</option>
                <option value="workplaces">Workplaces</option>
                <option value="misc">Miscellaneous</option>
            </select>
            <label htmlFor="question" id="question-label">Question</label>
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