<script lang="ts">
    import type { PageData } from './$types';

    let { data }: { data: PageData } = $props();
    let headings = ["Lorem", "Ipsum"]

</script>


<header>
    <h1>We've Curated these Resources for you:</h1>
</header>

<main>
    {#each headings as heading, i}
        <div style={`animation-delay: ${i + 1}s;`}>
            <h2>{heading[0].toUpperCase() + heading.slice(1)}</h2>
        </div>
    {/each}
</main>

<style lang="scss">

    header {
        width: 100%;
        height: 50vh;
        display: grid;
        align-items: center;
    }

    h1 {
        font-size: 3em;
        animation: fadeIn 1s linear forwards;
    }

    main {
        display: flex;
        justify-content: space-evenly;

        div {
            opacity: 0%;
            animation: fadeIn 1s linear forwards;
            text-shadow:
                -1px -1px 0 var(--background),
                1px -1px 0 var(--background),
                -1px 1px 0 var(--background),
                1px 1px 0 var(--background); 
        }
    }

    @keyframes fadeIn {
        0% {
            opacity: 0%;
        }

        100% {
            opacity: 1;
        }
    }


    
</style>