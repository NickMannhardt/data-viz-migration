<script>
    import { onMount } from "svelte";

    import Bar from "../components/Bar.svelte";
    import BubbleChart from "../components/BubbleChart.svelte";
    import Scatterplot from "../components/Scatterplot.svelte";
    import Slide from "../components/Slide.svelte";

    export let scrollUp;
    export let scrollDown;

    let country = 'El Salvador';
    let age = 21;
    let gender = 'Woman';
    
    let countryCode = {
        'El Salvador': 'SLV',
        'Honduras': 'HND',
        'Guatemala': 'GT'
    }

    let genderCode = {
        'Woman': 1,
        'Man': 2
    }

    let data = []
    
    onMount( () => {
        fetch(`${PUBLIC_API_URL}/final_remesa_amount/${countryCode[country]}/${age}/${genderCode[gender]}`)
            .then(res => res.json())
            .then(res => {
                data = res.map(d => {
                    return {
                        index: d['remesa_bracket'],
                        size: d['remesa_pct']
                    }
                })
            })
    })

</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
>   
    <div class='flex-center'>
        <!-- <div>
            hello
        </div> -->
        <div class='container'>
            <!-- <Scatterplot
                cssHeight=40
                cssWidth=60
                data={[
                    {x: 1, y: 1},
                    {x: 3, y: 2},
                    {x: 5, y: 6},
                    {x: 3, y: 8},
                    {x: 12, y: 3},
                ]}
            />  -->
            {#if data.length > 0}
                <BubbleChart
                    Title="Demo Graphic"
                    cssHeight=40
                    cssWidth=60
                    data={[
                        // 0, 1, 2, 3
                        // {a: 0},{a: 1},{a: 2},{a: 3}
                        {label: 'A', value: 23},
                        {label: 'B', value: 51},
                        {label: 'C', value: 26},
                        // {label: 'C', size: 32},
                    ]}
                />
                <!-- <BubbleChart
                    cssHeight=40
                    cssWidth=60
                    data={data.slice(0,6)}
                /> -->
                <Bar
                    cssHeight=50
                    cssWidth=90
                    data={data.slice(0,7)}
                />
            {/if}
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