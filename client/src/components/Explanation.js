import '../styles/ExplanationStyle.css';
import explanationPDF from '../assets/Parallelogram-Description-And-Proofs.pdf';
import redistribution from '../assets/Redist.png';
import RPFairShare from '../assets/ordpeople.png';
import RPDeathPenalty from '../assets/deathpen.png';

const Explanation = () => {
    return(
        <section className="page" id='how-it-works'>
            <div id='pdf-box'>
                <i>For a more academic and mathematical explanation, including various semi-formal proofs,
                you can download <a id='pdf-link' href={explanationPDF}>this pdf</a>. For those of you with social skills,
                you may find the below a bit more helpful instead.</i>
            </div>

            <p>
                Whenever I would read about how two different groups in society 'disagreed' on a certain
                issue, it always felt a bit too abstract, and the information never seemed to be
                presented in an intuitive way. Usually the explanation or the associated graph would only
                talk about one end of the scale (often simply how many of each group 'agreed' with
                something) and it never felt like the 'big picture' was fully encapsulated.
            </p>
            <p>
                The <em>Polarisation Parallelogram</em> was my attempt at fixing this. I developed it as part of
                my master's thesis, and realised it'd be pretty neat if I could make it into more than
                just a chapter of something nobody other than my supervisor would ever read. So, following
                my graduation, I sat on the idea for a bit before starting to work on some python code
                that would auto-generate the graphical framework alongside all the essential information it
                pulls. And this is the result! Of course, I had little to no role in the development of the
                website itself. That's the work of my incredible partner, Zarrin. I don't know the first
                thing about web development, and the final product is as much her creation as it is mine.
            </p>
            <p>
                The framework is based on one intuitive rule: <em>the larger the wedge (or occasionally
                wedges) the more polarised the two groups specified are.</em> All possible answers are
                included in the graph, and the full exact distribution of answers for each group can be
                easily derived. With some background maths, you can do a lot more with it (and I think
                there are some quite beautiful and surprising properties the maths nerds will appreciate),
                but the core only requires that one piece of knowledge — bigger wedge, higher polarisation
                — to understand.
            </p>
            <p>
                In the 'Make a Graph' section of the website, you can input two societal groups of your choice
                — perhaps people who lean towards different parties, or age groups, or degree vs non-degree
                holders. You can then pick an issue of your choice — this could be about taxes, or healthcare,
                or even smaller-scale questions about things like urban planning. There's a huge variety of
                questions to choose from! One you've picked, a graph will be generated that will tell you about
                how and to what extent those two groups in society differ in opinion.
            </p>
            <img id='example-1' src={redistribution} alt='A polarisation parallelogram that compares the views
            of labour and conservative leaners on the issue of resditriburing income'/>
            <p>
                Look at the two lines here, for example, on the question 'Government should redistribute
                income from the better-off to those who are less well off'. You can see that, at the point of
                'strongly agree', the 'Conservative Lean' number is close to zero, while for 'Labour Lean' it
                is almost 40%. So just under four in ten Labour leaners strongly agree with the sentiment,
                while almost no Conservatives do.
            </p>
            <p>
                Now, follow the lines along the x-axis. Once we get to 'agree' the Labour number goes up to
                just over 70%. This does not mean that 70% of Labour lean respondents picked 'agree'
                specifically — it means that 70% picked 'agree' <i>or</i> 'strongly agree'. We've gone up by around
                thirty percentage points, so that is the percentage of respondents that answered 'agree'.
                This is because the graph is <em>cumulative</em> — at each point, the number on the y-axis is the
                percent of respondents who answered something <em>up to and including that answer</em>. The same
                principle applies for both groups as you keep going up the graph. This is why both groups
                start at zero and finish at 100% — by the time all options have been exhausted, the two graphs
                will meet again. And this creates our 'wedge'. It's also why you'll never see either of the
                lines go down. If nobody answered a certain way, then the line from that answer to the next
                would be a horizontal line, as the total percentage of answerers would not have changed.   
            </p>
            <p>
                If the Labour and Conservative distributions were exactly the same, then the area between
                them would be zero. In other words, polarisation would be non-existent.
            </p>
            <p>
                Now imagine <i>every</i> member of one group answered with 'strongly disagree' and every member of
                the other answered 'strongly agree'. In this case, the groups would follow opposite ends of
                the dashed parallelogram. In our case, if our party leaners were truly fully polarised, the
                red Labour line would jump straight up to 100% for 'strongly agree'. The blue Conservative
                line would follow along the bottom, and then jump up from 0 to 100% at 'strongly disagree'.
                This would be 100% polarisation.
            </p>
            <p>
                So our wedge is telling us where in relation to these two extremes each group is. The bigger
                the wedge, the further from that 'equal distribution' scenario. This is quantified as the
                area of the wedge as a percentage of the area of the hypothetical 100% polarisation
                parallelogram, which is represented by the dotted lines.
            </p>
            <p>
                <em>In practice, any large group of humans will be complex and diverse.</em> It is <i>very</i> rare
                to find a 'polarisation score' here above 50% (the highest I've ever found with this dataset is just
                over 60%). Nothing coming close to 100% polarisation ever happens in practice with large groups.
                Make of that what you will!
            </p>
            <p>
                You'll see this score (represented by <span className='maths'>&lambda;</span>) in the top left
                alongside two epsilon values, <span className='maths'>&epsilon;<sub>1</sub></span> and <span className='maths'>&epsilon;<sub>2</sub></span>. <em>The
                epsilons measure how far towards each extreme our groups are.</em> <span className='maths'>&epsilon;<sub>1</sub></span> always
                refers to the top graph, while <span className='maths'>&epsilon;<sub>2</sub></span> refers to
                the bottom one. An epsilon value of 0% for a group would mean our distribution of scores centers
                right in the middle (e.g. if everyone chose the middle option or if each option had an equal
                number of responses). A positive epsilon means the top graph leans at least partially towards the low
                end of the scale. If Labour unaninmously strongly agreed, <span className='maths'>&epsilon;<sub>1</sub></span> would
                be 100%. Similarly, if Conservative respondents all unanimously strongly disagreed, then <i>their</i> epsilon, <span className='maths'>&epsilon;<sub>2</sub></span>,
                would be 100%. Here, we can see that <span className='maths'>&epsilon;<sub>1</sub></span> is 46% and <span className='maths'>&epsilon;<sub>2</sub></span> is
                18%. This means that the Conservatives are actually quite a bit closer to neutrality on the question than Labour!
            </p>
            <p>
                You might be realising that if there were no 'strong' options, both our epsilon values and lambda
                value would imply greater extremity and polarisation respectively. That's absolutely right. <em>I
                find that the best use of the parallelogram is to compare the number between issues.</em> You
                might ask 'do citizens with vs without a degree have a higher polarisation score on
                <i>this</i> issue or <i>that</i> one?' The number you see in the middle isn't as much use on its own
                as it is when compared with other issues or groups that interest you. 
            </p>
            <div id='example-box'>
                <img src={RPFairShare} alt="A polarisation parallelogram that compares the views of high and low income people on
                the whether workers get their fair share of the nation's wealth"/>
                <img src={RPDeathPenalty} alt='A polarisation parallelogram that compares the views of high and low income people on the issue of
                the death penalty' />
            </div>
            <p>
                For example, it surprised me that the rich and the poor tended to be more polarised on issues
                relating to law and order, values and traditions than on issues related to economic equality — which
                one might intuitively think would be more relevant to those two groups.
            </p>
            <p>
                But my goal isn't to tell you what to think about what you find! I just hoped to make a tool that might
                make you learn something interesting about our society and how it thinks. What you make of those results
                is where your own inner social scientist comes in.
            </p>
            <p>
                So really, just have some fun with it! I haven't tried anything like every combination of issues myself,
                of course. It's very possible that you'll be the first person in history to ever 'create' the result that
                you do. If you create a graph that looks interesting or surprises you, let me know! I'd love to hear
                about what you've discovered and your thoughts on it. <em>Happy graphing!</em>
            </p>
            <h2><i>~ Joey</i></h2>
            <p className='citation'>Data from NatCen Social Research. (2023). British Social Attitudes Survey, 2021. [data collection]. UK Data Service. SN: 9072, DOI: http://doi.org/10.5255/UKDA-SN-9072-1</p>
        </section>
    );
}

export default Explanation;