<script>
    import Slide from "../components/Slide.svelte";

    export let scrollUp;

</script>

<Slide
    scrollUp={scrollUp}
    shifted={false}
>
    <div style='container'>
        <span>Would you like to start again?</span>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <button 
            onClick="window.location.reload();"
            class="retry-button"
        >
            Refresh Page
        </button>
        <br/>
        <br/>
        <br/>
        <br/>
        <i>This data visualization was made with data contributed by the United Nations World Food Programme (WFP).</i>
    </div>
</Slide>

<style>
    .container {
        display: flex;
        flex-direction: column;
    }

    .retry-button {
        font-family: 'Permanent Marker';
        font-size: 18pt;
        color: white;
        background-color: #E15759;
        border: none;
        padding: 2vh;
        cursor: pointer;
    }
</style>