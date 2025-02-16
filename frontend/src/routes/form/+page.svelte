<script>
    import {text} from "@sveltejs/kit";
    import {read} from "$app/server";
    import {compile} from "svelte/compiler";
    import {onMount, tick } from "svelte";

    let qna = [
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

    let user_inp;
    let jsonify = {};
    let answers = [];
    let i = 0;
    let completed = false;
    let responseAI="";

    onMount(()=>{
        document.querySelector('input')?.focus();
    });
    async function jsonfy(event) {
        event.preventDefault();
        if (user_inp.trim() !== "") {
            answers.push(user_inp);
        } else {
            answers.push("0");
        }
        user_inp = "";

        if (i < qna.length - 1) {
            i++;
            await tick();
            document.querySelector('input')?.focus();
        } else {
            jsonify = {responses: answers};
            completed = true;
            await callCohere(jsonify);
        }
    }

    async function callCohere(jsondata){
        try {
            const response = await fetch("https://api.cohere.ai/v1/chat", {
                method: "POST",
                headers: {
                    "Authorization": "Bearer <API>", // 🔴 Replace with your actual API key
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    model: "command-r7b-12-2024",
                    message: `Here are responses, give me support resources helping me be independent: ${JSON.stringify(jsondata)}.`,
                    max_tokens: 200,
                    temperature: 0.5
                })
            });
            const data = await response.json();
            responseAI = data.text;
            console.log("Cohere API Response:", data); // ✅ Log full response



            if (data.error) {
                console.error("Cohere API Error:", data.error);
                responseAI = `Cohere API Error: ${data.error.message}`;
            } else if (data.text && data.text.length > 0) {
                responseAI = data.text;
            } else {
                console.error("Error: No generations returned from Cohere");
                responseAI = "Cohere did not return any data.";
            }
        } catch (error) {
            console.error("Network or Fetch Error:", error);
            responseAI = "A network error occurred. Please try again.";
        }
    }
</script>


<main>
    {#if !completed}
        <form>
            <label class="questions">{qna[i]}</label>
            <input type="text" bind:value={user_inp}/>
            <button on:click={jsonfy}>Next</button>
        </form>
    {:else }
        <p>{JSON.stringify(jsonify, null, 2)}</p>
        <pre class="respond">{responseAI}</pre>
    {/if}
</main>

<style lang="css">
    .respond {
        white-space: pre-wrap;
        word-wrap: break-word;
        max-width: 600px;
    }
</style>