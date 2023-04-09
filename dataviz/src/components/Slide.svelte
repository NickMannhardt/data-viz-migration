<script>
    export let scrollUp;
    export let scrollDown;
</script>

<div class="slide">
    {#if scrollUp}
        <div>
            <button class="prev" on:click={scrollUp}>Back</button>
        </div>
    {/if}
    <div class="slide-content">
        <slot />
    </div>
    {#if scrollDown}
        <div class="next-container">
            <button class="next" on:click={scrollDown}>Next</button>
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
        align-items: center;
        justify-content: center;
    }

    .prev {
        border: none;
        background: none;
        color: #a8181c;
        text-decoration: underline;
        margin-left: 7vh;
    }

    .next {
        background-color: #a8181c;
        color: white;
        margin-right: 7vh;
        padding: 2vh 3vh;
        border: none;
        border-radius: 1vh;
    }

    .next:hover {
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