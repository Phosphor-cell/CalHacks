<script lang="ts">
    const questions = [
        "What is your current financial situation?",
        "How stable is your housing situation?",
        "What is your employment status?",
        "Do you have recognized credentials for your field in Canada?",
        "How is your legal status in Canada?",
        "Do you have access to healthcare and mental health support?",
        "How well do you speak English/French?",
        "Do you have a support network in Canada? ",
        "How much do you know about your rights and laws in Canada?",
        "How confident are you in navigating daily life in Canada? ",
        "Which country are you originally from?",
        "What is your first name (This would help us to help you in further steps!)?",
    ];
    let questionIndex = $state(0)
    let answers = []
    function nextQuestion() {
        questionIndex += 1;
        console.log(questionIndex)
        if (questionIndex >= questions.length) {
            let results = [...document.querySelectorAll('input')].map(x=>x.value)
            alert(results)
        }

        document.querySelectorAll('input').item(questionIndex).focus()




        
    }


</script>


<header>
    <h1>Just getting some info...</h1>
</header>
<main>
    {#each questions as question, i}
        <div class={`question ${questionIndex > i ? "show" : ""}`} id={`q${i}`}>
            <h2>{question}</h2>
            <input onkeydown={e => {
                if (e.key == "Enter") {
                    nextQuestion()
                }
            }} type="text"/>
            <button onclick={() => {nextQuestion()}}>Next</button>
        </div>
    {/each}
</main>

<style lang="scss">
    input {
        border-radius: 10em;
        background-color: #313131;
        color: grey;
        padding: 0.5em;
        border: none;
    }

    button {
        appearance: none;
        border: none;
        border-radius: 2em;
        padding: 0.5em;
    }

    div.question {
        opacity: 0.2;
        transition: all 0.7s linear;

        &.show {
            opacity: 0.5;
        }

        &:focus-within {
            opacity: 1;
        }
    }


</style>