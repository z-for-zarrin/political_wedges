import '../styles/AboutStyle.css';
import linkedinIcon from '../assets/linkedin.png';
import githubIcon from '../assets/github.png';

const About = () => {
    return(
        <section className="page">
            <section className="profile">
                <h3>Joey Cartwright — Backend Developer & Data Scientist</h3>
                <p>Joey, like his co-creator and (according to historians) close friend Zarrin,
                    spent his post-secondary years at the University of Warwick. There, he
                    co-founded and was eventually president of the Bubble Tea Society, and studied
                    for a degree in Economics and Politics in his spare time. He developed the
                    polarisation parallelogram during his panic master's in quantitative politics,
                    and began working on the python code for what would eventually become the graph
                    generator you see here not long after. His first job was writing practice
                    questions for an introductory textbook in Quantitative Social Science under
                    a professor who accused him of having 'chicken issues'. He is always up for
                    a detailed conversation on the best places to find chicken wings (and once
                    created a chicken wing tier list data set from his friend group after a
                    'Chicken Crawl'), but will happy also talk to you about 3D <i>Zelda</i> or 
                    <i> Mario</i> titles, murder mysteries, or 20<sup>th</sup> century jazz pianists.</p>
                <a href='https://www.linkedin.com/in/joseph-joey-cartwright-13b4b31b6/?originalSubdomain=uk'>
                    <img className='link-icon' src={linkedinIcon} alt="link to Joey's linkedin profile" />
                </a>
                <a href='https://github.com/JoeysPouch'>
                    <img className='link-icon' src={githubIcon} alt="link to Joey's github profile" />
                </a>
            </section>
            <section className="profile">
                <h3>Zarrin Rahman — Frontend Developer</h3>
                <p>Hailing from the town of Bedford, Bedfordshire, Zarrin earned her Mathematics
                    degree from the University of Warwick, Warwickshire, where she also met Joey
                    through the Bubble Tea Society. Eventually she became the publicity officer
                    for the society, which should give her sufficient credentials to claim graphic
                    design is her passion (just look at the lovely logo she designed). Now, Zarrin
                    has turned her eyes to tech for the next step in her journey. Since graduating,
                    she has completed a bootcamp run by the Bright Network Technology Academy,
                    where she learnt about full-stack software development — including the
                    knowledge necessary for building this very project! When she's not tapping
                    away at the laptop, you can find Zarrin playing guitar, getting lost in
                    the woods or farming her time away in Stardew Valley. Please direct all webdev
                    queries and cat pictures to her.</p>
                <a href='https://www.linkedin.com/in/zarrin-rahman'>
                    <img className='link-icon' src={linkedinIcon} alt="link to Zarrin's linkedin profile" />
                </a>
                <a href='https://github.com/z-for-zarrin'>
                    <img className='link-icon' src={githubIcon} alt="link to Zarrin's github profile" />
                </a>
            </section>
            <footer>
                <a href="https://www.flaticon.com/free-icons/linkedin" title="linkedin icons">Linkedin icons created by Fathema Khanom - Flaticon</a>
                <a href="https://www.flaticon.com/free-icons/github" title="github icons">Github icons created by Pixel perfect - Flaticon</a>
            </footer>
        </section>
    );
}

export default About;