<script lang="ts">
    import type { PageData } from './$types';

    let { data }: { data: PageData } = $props();

</script>


<header>
    <h1>We've Curated these Resources for you:</h1>
</header>

<main>
    {#each ["Lorem", "Ipsum"] as heading, i}
        <div style={`animation-delay: ${i}s;`}>
            <h2>{heading}</h2>
        </div>
    {/each}
</main>

<style lang="scss">
    @import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400..800;1,400..800&display=swap');
    :root {
        background-color: rgb(35, 35, 35);
        color: white;
        font-family: "EB Garamond", serif;
        text-align: center;
    }

    header {
        width: 100%;
        height: 50vh;
        display: grid;
        align-items: center;
    }

    h1 {
        font-size: 3em;
        transition: all 1s linear;

        &:hover {
            color: transparent;
        }
    }

    main {
        display: flex;
        justify-content: space-evenly;

        div {
            opacity: 0%;
            animation: fadeIn 1s linear forwards;
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