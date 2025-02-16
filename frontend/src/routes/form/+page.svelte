<script>
    import {text} from "@sveltejs/kit";
    import {read} from "$app/server";
    import {compile} from "svelte/compiler";
    import {onMount, tick } from "svelte";

    let qna = [
        "What is your name?",
        "How old are you?",
        "Where do you live?",
        "What is your favorite hobby?",
        "What is your dream job?"
    ];
    let user_inp;
    let jsonify = {};
    let answers = [];
    let i = 0;
    let completed = false;

    onMount(()=>{
        user_inp?.focus();
    });
    async function jsonfy() {
        if (user_inp.trim() !== "") {
            answers.push(user_inp);
        } else {
            answers.push("0");
        }
        user_inp = "";

        if (i < qna.length - 1) {
            i++;
            await tick();
            user_inp?.focus();
        } else {
            jsonify = {responses: answers};
            completed = true;
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
    {/if}
</main>