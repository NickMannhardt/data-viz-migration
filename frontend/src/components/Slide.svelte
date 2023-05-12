<script>
    export let scrollUp = null;
    export let scrollDown = null;
    export let allowNext = null;
    export let shifted = true;
</script>

<div class="slide">
    {#if scrollUp}
        <div>
            <button class="prev" on:click={scrollUp}>&#60 Back</button>
        </div>
    {/if}
    <div class= {shifted ? "slide-content shifted" : "slide-content"}>
        <slot/>
    </div>
    {#if scrollDown}
        <div class="next-container">
            <button disabled={!allowNext} class="next" on:click={scrollDown}>Next</button>
        </div>
    {/if}
</div>

<style>
    .slide {
        height: 100vh;
        width: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .slide-content {
        height: 85vh;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: stretch;
        justify-content: center;
    }

    .shifted {
        margin-left: 20vh;
    }

    .prev {
        border: none;
        background: none;
        color: #E15759;
        margin-left: 7vh;
        font-size: 18pt;
        font-family: "Delicious Handrawn";
    }

    .next {
        background: none;
        color: #E15759;
        margin-right: 7vh;
        border: none;
        border-radius: 1vh;
        font-family: "Delicious Handrawn";
        font-size: 36pt;
        text-decoration: underline;
    }

    .next:hover {
        cursor:pointer
    }

    .prev:hover {
        cursor:pointer
    }

    .next:disabled{
        opacity: 0.5;
        cursor: default;
    }

    .next-container {
        display: flex;
        justify-content: end;
    }
</style>