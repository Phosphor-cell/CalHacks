<script lang="ts">
    import type { PageData } from './$types';

    let { data }: { data: PageData } = $props();

    let exampleTimeline: [Date, string][] = [
        [new Date(2025, 0, 15), "Event 1"],
        [new Date(2025, 1, 15), "Event 2"],
        [new Date(2025, 2, 15), "Event 3"],
    ]

    let minTime = exampleTimeline.reduce((a, b) => a[0] < b[0] ? a : b)[0]
    let maxTime = exampleTimeline.reduce((a, b) => a[0] > b[0] ? a : b)[0]
    let range = maxTime.valueOf() - minTime.valueOf()

    let exampleTodoList = [
        ["Lorem", "ipsum", "dolor", "sit", "amet", "consectetur", "adipisicing", "consequuntur", "deleniti"],
        ["elit", "Nihil", "quam", "omnis", "magni", "doloremque", "totam", "modi", "nisi", "impedit", "et"],
        ["nulla", "excepturi", "laborum", "esse", "harum", "ullam", "porro", "odit", "numquam", "velit"]
    ]


    let emails = []
    let resources = [
        "Link1",
        "Link2",
        "Link3"
    ]
</script>


<div class="timeline">
    <hr>
    {#each exampleTimeline as [date, event]}
        <div class="event">
            <div class="date">{date.toString().split(' ').slice(1, 3).join(' ')}</div>
            <div class="dot"></div>
            <div class="ev">{event}</div>
        </div>
    {/each}
</div>

<div class="todo">
    {#each exampleTodoList as todoMonth, i}
        <div>
            <h3>Month {i + 1}</h3>
            <div class="month">
                {#each todoMonth as todo}
                    <div class="item">{todo}</div>
                {/each}
            </div>
        </div>
    {/each}
</div>

<div class="res">
    <h2>You might want to check these out:</h2>
    <ul>
        {#each resources as link}
            <li>
                <a href={link}>{link}</a>
            </li>
        {/each}
    </ul>

</div>


<div>
    <h1>Take your first step</h1>
</div>

<style lang="scss">
    div.timeline {
        display: flex;
        justify-content: space-evenly;
        position: relative;

        hr {
            position: absolute;
            width: 80%;
            bottom: 45%;
            margin: 0px;
            border: solid white 3px;
        }


        div.event {
            display: flex;
            flex-direction: column;
            align-items: center;

            div.dot {
                background-color: white;
                aspect-ratio: 1;
                height: 2em;
                border-radius: 1em;
            }
        }
    }

    div.todo {
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        padding: 1em 0em;

        div.todo > * {
            gap: 1em;
            display: flex;
        }


        div.item {
            background-color: maroon;
            border-radius: 10px;
            padding: 0.2em;
            text-align: start;
        }
    }

</style>


