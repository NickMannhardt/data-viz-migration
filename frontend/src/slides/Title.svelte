<script>
    import Slide from '../components/Slide.svelte';
</script>

<Slide
    shifted={false}
>
    <div class='title-div'>
        <h1>Big <span class='red'>Data</span>. Big <span class='orange'>Choices</span>. Big <span class='teal'>Stories</span>.</h1>
        <h2><i>The choices of the individual told in aggregate, in a pick-your-own adventure format</i></h2>
        <i>Zoe De Simone, Tasha Hirt, Niklas Mannhardt</i>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <br/>
        <h3>Press spacebar to begin.</h3>
    </div>
</Slide>

<style>
    h1 {
        font-size: 34pt;
    }

    h2 {
        font-size: 15pt;
        color: #31a693;
    }

    .title-div {
        font-family: Helvetica, Arial, sans-serif;
        text-align: center;
    }

    .red {
        background-color: #a8181c;
    }

    .orange {
        background-color: #f66d0e;
    }

    .teal {
        background-color: #31a693;
    }
</style>