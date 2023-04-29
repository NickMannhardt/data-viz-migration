<script>
    import Bar from "../components/Bar.svelte";
    import Scatterplot from "../components/Scatterplot.svelte";
    import Slide from "../components/Slide.svelte";

    export let scrollUp;
    export let scrollDown;

</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
>   
    <div class='flex-center'>
        <div>
            hello
        </div>
        <div class='container'>
            <Scatterplot
                cssHeight=40
                cssWidth=60
                data={[
                    {x: 1, y: 1},
                    {x: 3, y: 2},
                    {x: 5, y: 6},
                    {x: 3, y: 8},
                    {x: 12, y: 3},
                ]}
            /> 
            <Bar
                cssHeight=60
                cssWidth=80
                data={[
                    {index: 0, size: 11},
                    {index: 1, size: 14},
                    {index: 2, size: 8},
                    {index: 3, size: 18},
                    {index: 4, size: 12},
                    {index: 5, size: 11},
                ]}
            />
        </div>
    </div>
</Slide>

<style>
    .BarDiv {
        width: 160vh;
        height: 20vh;
    }

    .flex-center {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .container {
        display: flex;
        flex-direction: column;
        padding: 1vh;

        /* width: 100vh; */
        /* height: 50vh; */
    }
</style>