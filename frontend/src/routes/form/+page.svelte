<script>
    import {text} from "@sveltejs/kit";
    import {read} from "$app/server";
    import {compile} from "svelte/compiler";
    import {onMount, tick } from "svelte";

    let qna = [
        'What are your main concerns regarding living in Canada?',
        'Have you had access to services who are offering support to immigrants (e.g. english classes, support for financial, employment, or living needs)? If so, how helpful have they been?', 
        'Do you plan on being a Canadian Citizen? If so, have you applied for, or are eligible for Canadian Citizenship yet?', 
        'What is your current employment status?', 
        'Have you applied, or own a Work Permit?',
        'Do you have access to financial services such as a bank?', 
        'How fluent are you in English or French, even if it is not your first language?', 
        'Are you currently enrolled in a language class right now? If so how helpful have they been for you?',
        'What kind of housing unit do you live in right now (e.g. apartment, house, etc.)?',
        'Do you feel safe with your current living conditions?',
        'How affordable are you finding your current housing situation?',
        'Do you have good access to healthcare services?', 
        'Have you applied for any form of insurance?'
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