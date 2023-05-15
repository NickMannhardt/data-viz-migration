<script>
    import Slide from '../components/Slide.svelte';
</script>

<Slide
    shifted={false}
>
    <div class='title-div'>
        <h1>Migrant Story</h1>
        <!-- <h1>Big <span class='red'>Data</span>. Big <span class='orange'>Choices</span>. Big <span class='teal'>Stories</span>.</h1> -->
        <!-- <h2><i>The choices of the individual told in aggregate, in a pick-your-own adventure format</i></h2> -->
        <h2>an <span class='orange'>interactive</span>, <span class='teal'>data-driven</span> experience</h2>
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
        <p>Press spacebar to begin.</p>
    </div>
</Slide>

<style>
    h1 {
        font-size: 34pt;
        font-family: 'Permanent Marker';
        color: #E15759;
    }

    h2 {
        font-size: 15pt;
        /* color: #31a693; */
        font-family: 'Inconsolata', Arial, sans-serif;
    }

    .title-div {
        font-family: 'Inconsolata', Arial, sans-serif;
        text-align: center;
    }

    .red {
        background-color: #E15759;
    }

    .orange {
        color: #F2832B;
    }

    .teal {
        color: #31a693;
    }
</style>