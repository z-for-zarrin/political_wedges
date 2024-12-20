import { useState } from "react";
import '../styles/GraphStyle.css';

const GraphInput = ({group1Id, setGroup1Id, group2Id, setGroup2Id, question, setQuestion, postGraph, setIsDataLoading}) => {

    const[groupKey, setGroupKey] = useState("");
    const[groupArray, setGroupArray] = useState([]);
    const[questionArray, setQuestionArray] = useState([]);
    
    const characteristics = {
      AgeGroup:   ["18-34", "35-54", "55+"],
       DVSex21:   ["Female", "Male"],
       partyfw:   ["Conservative", "Labour", "Liberal Democrats", "Scottish National Party",
                   "Plaid Cymru", "Green", "UKIP", "Reform"],
         SRInc:   ["Identify as high income", "Identify as middle income", "Identify as low income"],
      HigherEd:   ["Degree", "No degree"]
    }

    const topics = {
        britishValues:      ["On a scale of 1 to 7, with 1 being ‘not at all British’, and 7 ‘being very strongly British’, to what extent do you think of yourself as British?",
                             "'The world would be a better place if people from other countries were more like the British'",
                             "'Generally speaking, Britain is a better country than most other countries'",
                             "'Young people today don't have enough respect for traditional British values'",
                             "How important do you think being born in britain is for being truly british?†",
                             "How important do you think having british ancestry is for being truly british?†",
                             "How important do you think feeling british is for being truly british?†",
                             "Would you say that Britain's cultural life is generally undermined or enriched by migrants coming to live here from other countries?"],
        class:              ["How wide are the differences between social classes in this country, do you think?",
                             "How difficult would you say it is for people to move from one class to another?",
                             "Do you think [social class] differences have become greater or less or have remained about the same?†"],
        economics:          ["'Overall, it is worthwhile for me to save into a private pension'",
                             "'Government should redistribute income from the better-off to those who are less well off'",
                             "'Big business benefits owners at the expense of workers'",
                             "'Ordinary working people do not get their fair share of the nation's wealth'",
                             "'There is one law for the rich and one for the poor'",
                             "'Management will always try to get the better of employees if it gets the chance'",
                             "Would you say it is generally bad or good for Britain's economy that migrants come to Britain from other countries?"],
        genSexMinorites:    ["If a man and woman have sexual relations before marriage, what would your general opinion be?",
                             "Opinions on sexual relations between two adults of the same sex",
                             "How much do you agree or disagree that a person who is transgender should be able to have the sex recorded on their birth certificate changed if they want?"],
        healthcare:         ["Please say what you think overall about the state of health services in Britain nowadays"],
        housingUrban:       ["Would you support or oppose more homes being built in your local area?",
                             "To what extent would you support or oppose requiring people in existing buildings to make changes to their homes to meet new energy regulations, should new homes be built in that area?†",           
                             "To what extent are you in favour of, or against, new cycle lanes in roads being introduced in your area?†",           
                             "To what extent are you in favour of, or against, your local council spending more money to improve existing public transport, although this may mean spending less on other council services?†",           
                             "To what extent are you in favour of, or against, reserving parking spaces for electric car charging points being introduced in your area?†",           
                             "To what extent are you in favour of, or against, building carparks to introduce more “park and ride” routes being introduced in your area?†",           
                             "To what extent are you in favour of, or against, narrowing roads to widen pavements being introduced in your area?†",           
                             "To what extent are you in favour of, or against, closing roads to create pedestrian high streets being introduced in your area?†"],
        law:                ["'People who break the law should be given stiffer sentences'",
                             "'For some crimes, the death penalty is the most appropriate sentence'",
                             "'Schools should teach children to obey authority'",
                             "'The law should always be obeyed, even if a particular law is wrong'",
                             "'Censorship of films and magazines is necessary to uphold moral standards'"],
        welfare:            ["'Around here, most unemployed people could find a job if they really wanted one'",
                             "'Many people who get social security don't really deserve any help'",
                             "'Most people on the dole are fiddling in one way or another'",
                             "'If welfare benefits weren't so generous, people would learn to stand on their own two feet'",
                             "'The welfare state encourages people to stop helping each other'",
                             "'The government should spend more money on welfare benefits for the poor, even if it leads to higher taxes'",
                             "'Cutting welfare benefits would damage too many people's lives'",
                             "'The creation of the welfare state is one of Britain's proudest achievements'",
                             "Would you like to see more or less government spending on [benefits for unemployed people] than now?†",
                             "Would you like to see more or less government spending on [benefits for disabled people who cannot work] than now?†",
                             "Would you like to see more or less government spending on [benefits for parents who work on very low incomes] than now?†",
                             "Would you like to see more or less government spending on [single parents] than now?†",
                             "Would you like to see more or less government spending on [retired people] than now?†",
                             "Would you like to see more or less government spending on [carers for those who are sick or disabled] than now?†"],
        workplaces:         ["Have attempts to give people with physical impairments an equal chance in the workplace gone too far or not far enough?",
                             "Have attempts to give people with mental health conditions an equal chance in the workplace gone too far or not far enough?",
                             "Do you think attempts to give equal opportunities have gone too far or not gone far enough for LGB people?†",
                             "Do you think attempts to give equal opportunities have gone too far or not gone far enough for transgender people?†",
                             "Do you think attempts to give equal opportunities have gone too far or not gone far enough for women?†",
                             "Do you think attempts to give equal opportunities have gone too far or not gone far enough for black and asian people?†",
                             "How strongly do you agree or disagree that, in principle, someone who has been off work with a back problem going back to work quickly will help speed their recovery?†",
                             "How strongly do you agree or disagree that, in principle, someone who has been off work with depression going back to work quickly will help speed their recovery?†"],
        misc:               ["To what extent would you say that online and mobile communication undermines personal privacy?",
                             "To what extent would you say that online and mobile communication exposes people to misinformation?"]
    }

    const charChangeHandler = (event) => {
        setGroupArray(characteristics[`${event.target.value}`]);
        setGroupKey(event.target.value);
        setGroup1Id(0);
        document.getElementById("group-1").value=JSON.stringify({index: null, value:""});
        setGroup2Id(0);
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
        document.getElementById("question-select").value = "";
    }

    const questionOptions = questionArray.map((questionOption, index) => {
        return <option key={index} value={questionOption}>{questionOption}</option>
    })

    const handleSubmit = async (event) => {
        event.preventDefault();
        setIsDataLoading(true);
        let parameters = {
            groupVar: groupKey,
            group1Value: group1Id,
            group2Value: group2Id,
            question: question
        }
        await postGraph(parameters);
        setIsDataLoading(false);
    }

    return(
        <form id="parameters-form" onSubmit={handleSubmit}>
            <label htmlFor="characteristic-select">Characteristic</label>
            <select
                id="characteristic-select"
                type="text"
                name="characteristic"
                required
                defaultValue=""
                onChange={charChangeHandler}>
                
                <option disabled value="">Select demographic characteristic</option>
                <option value="partyfw">Party Preference</option>
                <option value="AgeGroup">Age</option>
                <option value="DVSex21">Sex</option>
                <option value="SRInc">Income</option>
                <option value="HigherEd">University Education</option>
            </select>
            <label htmlFor="group-1" className="indented-element">Group 1</label>
            <select
                id="group-1"
                className="indented-element"
                type="text"
                name="group1"
                required
                defaultValue={JSON.stringify({index: null, value:""})}
                onChange={(event) => {
                    let obj = JSON.parse(event.target.value);
                    setGroup1Id(obj["index"]+1);
                }}>
                
                <option disabled value={JSON.stringify({index: null, value:""})}>Select first group</option>
                {group1Options}
            </select>
            <label htmlFor="group-2" className="indented-element">Group 2</label>
            <select
                id="group-2"
                className="indented-element"
                type="text"
                name="group2"
                required
                defaultValue={JSON.stringify({index: null, value:""})}
                onChange={(event) => {
                    let obj = JSON.parse(event.target.value);
                    setGroup2Id(obj["index"]+1);
                }}>
                
                <option disabled value={JSON.stringify({index: null, value:""})}>Select second group</option>
                {group2Options}
            </select>
            <label htmlFor="topic-select" id="topic-label">Topic</label>
            <select
                id="topic-select"
                type="text"
                name="topic"
                required
                defaultValue=""
                onChange={topicChangeHandler}>
                
                <option disabled value="">Select topic</option>
                <option value="britishValues">British Values and Traditions</option>
                <option value="class">Class</option>
                <option value="economics">Finance and Economics</option>
                <option value="genSexMinorites">Gender and Sexual Minorities</option>
                <option value="healthcare">Health and Social Care</option>
                <option value="housingUrban">Housing and Urban Development</option>
                <option value="law">Law and Order</option>
                <option value="welfare">Welfare</option>
                <option value="workplaces">Workplaces</option>
                <option value="misc">Miscellaneous</option>
            </select>
            <label htmlFor="question-select" id="question-label" className="indented-element">Question</label>
            <select
                id="question-select"
                className="indented-element"
                type="text"
                name="question"
                required
                defaultValue=""
                onChange={(event) => {
                    setQuestion(event.target.value);
                }}>
                
                <option disabled value="">Select question</option>
                {questionOptions}
            </select>
            <input type="submit" value="Generate"/>
        </form>
    )
}

export default GraphInput;