<script lang="ts">
    import {onMount} from "svelte";
    let questions = [
      {
        question: "What document allows you to work legally in Canada as a temporary resident?",
        choices: ["Work Permit", "Permanent Resident Card", "Canadian Passport", "NEXUS Card"],
        correct: 0 
      },
      {
        question: "To open a bank account in Canada, which of the following documents are you allowed to bring in as one of two identification documents?",
        choices: ["Identification issued by Municipal Police Service", "Identification issued by Government of Canada or a Province", "Student ID", ""],
        correct: 1
      },
      {
        question: "What is the purpose of a Tax-Free Savings Account (TFSA)?",
        choices: ["To avoid paying income taxes", "To invest and save money without paying taxes on these gains", "To store money for retirement only", "To receive tax refunds"],
        correct: 1
      },
      {
        question: "What organization provides free or low-cost legal help for immigrants?",
        choices: ["Canadian Human Rights Tribunal", "Canada Border Services Agency", "Legal Aid", "The United Nations"],
        correct: 2
      },
      {
        question: "What is an employee’s right when it comes to workplace safety?",
        choices: ["The right to only follow verbal agreements", "The right to work without safety training", "The right to work for free if necessary", "The right to refuse unsafe work"],
        correct: 3
      },
      {
        question: "How do you get access to healthcare in Canada?",
        choices: ["Apply for a health card from your province", "Only citizens get healthcare", "Pay for all medical services out-of-pocket", "Call the government and request free service"],
        correct: 0
      },
      {
        question: "Which services are NOT covered by provincial health insurance?",
        choices: ["Hospital stays", "Emergency surgeries", "Visits to a family doctor", "Prescription medication"],
        correct: 3
      },
      {
        question: "Can permanent residents vote in Canadian elections?",
        choices: ["Yes, in all elections", "Only in local elections", "No, only Canadian citizens can vote", "Yes, but only after living in Canada for 5 years"],
        correct: 2
      }
    ];
  
    let userAnswers: number[] = Array(questions.length).fill(-1); // Stores selected choices (-1 means unanswered)
    let score: number = 0;
    let showResults = false;

    function randomQuestions() {
        for (let i = 0; i < questions.length; i++) {
            const j = Math.floor(Math.random() * questions.length);
            [questions[i], questions[j]] = [questions[j], questions[i]]
        }
    }

    onMount(() => {
        randomQuestions();
    });
  
    function selectAnswer(questionIndex: number, choiceIndex: number) {
      userAnswers[questionIndex] = choiceIndex;
    }
  
    function submitQuiz() {
      score = userAnswers.reduce((total, answer, i) => {
        return answer === questions[i].correct ? total + 1 : total;
      }, 0);
      showResults = true;
    }
  </script>
  
  <main>
    {#each questions as question, qIndex}
      <div class="question">
        <h3>{question.question}</h3>
        {#each question.choices as choice, cIndex}
          <label>
            <input 
              type="radio" 
              name="question-{qIndex}" 
              bind:group={userAnswers[qIndex]}
              on:change={() => selectAnswer(qIndex, cIndex)}
            />
            {choice}
          </label>
        {/each}
      </div>
    {/each}
  
    <button on:click={submitQuiz}>Submit</button>
  
    {#if showResults}
        {#if score/questions.length >= 0.9}
            <p>Congratulations, you passed the quiz and you are one step further on your great future here in Canada</p>
        {:else}
            <p>You did not pass the quiz, but that's okay, keep on learning</p>
        {/if}
    {/if}
  </main>
  
<style lang="css">
    .question { 
        margin-bottom: 20px; 
        font-family: Arial, sans-serif;
    }
</style>