import explanationPDF from '../assets/Parallelogram-Description-And-Proofs.pdf';

const Explanation = () => {
    return(
        <section className="page">
            <i>For a more academic and mathematical explanation, including various semi-formal proofs,
            you can download <a href={explanationPDF}>this pdf</a>. For those of you with social skills, you may find the below a bit more helpful instead</i>
        </section>
    );
}

export default Explanation;