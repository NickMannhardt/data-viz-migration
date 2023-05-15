<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/BarOld.svelte';
    import BubbleChart from '../components/BubbleChart.svelte';
    import { PUBLIC_API_URL } from '$env/static/public';


    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let acompany;
    export let gender;
    export let violence_group;
    export let age;

    let slide_index = 0;

    let perc_attempt1 = 0.0
    let perc_attempt2 = 0.0
    let perc_attempt3 = 0.0
    let perc_attempt4plus = 0.0

    let perc_tot_violence = 10.0

    // let data = new Map();
    // let data_violence = [
    //     {label: 1, value: 50},
    //     {label: 2, value: 50},
    //     {label: 3, value: 50},
    //     {label: 4, value: 50},
    //     {label: 5, value: 50},
    //     {label: 6, value: 50},
    // ];
    // let data = [];
    // data = data.map(d => {
    //     return {
    //         index: d['label'],
    //         size: d['count'],
    //     }
    // })

    let chartWidth = 600;
    let chartHeight = 350;

    let selected_country = 'GLV';

    const paddings = {
        top: 50, 
        left: 100,
        right: 50,
        bottom: 50,
    }

    let countryCode = {
        'El Salvador': 'SLV',
        'Honduras': 'HND',
        'Guatemala': 'GT'
    }

    let genderCode = {
        'Woman': 1,
        'Man': 2
    }

    let violence_code = [
        'None',
        'Extortion',
        'Theft',
        'Armed Robbery',
        'Threat',
        'Physical Aggression',
        'Sexual Harassment',
        'Kidnapping',
        'Attempted Murder',
        'Missing',
        'Other'
    ]
    // $: data_gender = [];
    let data_gender = [];


    // let data_violence = [];
    // use this notation so that we can automatically fetch new data when the gender changes
    // onMount(() => {
    $: data_violence = fetch(`${PUBLIC_API_URL}/mig_ext_violence/${countryCode[country]}/${genderCode[gender]}`)
        .then(res => res.json())
        .then(res => {
            let d_v = res.map(d => {
                return {
                    label: violence_code[d['label']-1],
                    value: d['value'],
                    includes_protagonist: false,
                    highlighted: d['highlight']
                }
            })
            data_gender = [d_v.pop()]
            data_gender[0]['includes_protagonist'] = true
            violence_group = d_v[0].label
            perc_tot_violence = d_v[0].value
            return d_v
        })
    
    $: data_attempt = fetch(`${PUBLIC_API_URL}/mig_ext_attempts_counts/${countryCode[country]}/${age}/${genderCode[gender]}`)
        .then(res => res.json())
        .then(res => {
            let d_v = res.map(d => {
                return {
                    label: d['label'] == 1 ? '1 Attempt' : `${d['label']} Attempts`,
                    value: d['value'],
                    includes_protagonist: false,
                    highlighted: d['highlight']
                }
            })
            return d_v
        })

    let xTitle= "Family Type";
    let yTitle = "Count";

    function step() {
        slide_index++;
    }

    function back() {
        slide_index--;
    }


</script>

<Slide
    scrollUp={slide_index == 0 ? scrollUp : back}
    scrollDown={slide_index == 5 ? scrollDown : step}
    allowNext={true}
>
    {#if slide_index == 0}
        <div>Let's take a step back and see how you fit into the the bigger picture of migration to the US</div>
    {/if }

    {#if slide_index == 1}
        <div>This is you</div>
        <div class='container'>
            <BubbleChart
                cssHeight=70
                cssWidth=70
                data={[{label: '1', value: 1, includes_protagonist: true, highlighted: 1}]}
                legend={false}
            />
        </div>
    {/if}

    {#if slide_index >= 2 && slide_index < 4}
        <div>Suppose you are one of 100 south american migrants from {country}</div>
        {#if slide_index >= 3}
            <div>About x of these are {gender == 'Man' ? 'men' : 'women'}</div>
        {/if}
        {#if slide_index == 2}
            <div class='container'>
                <BubbleChart
                    cssHeight=70
                    cssWidth=70
                    data={[{label: '1', value: 100, includes_protagonist: true, highlighted: 100}]}
                    flink=0.0
                    legend={false}
                />
            </div>
        {:else if slide_index == 3}
            <div class='container'>
                <BubbleChart
                    cssHeight=70
                    cssWidth=70
                    data={data_gender}
                    flink=0.0
                    legend={false}
                />
            </div>
        {/if}
    {/if}

    {#if slide_index == 4}
        <div>Many migrants experience violence during their journey.</div>
        {#await data_violence}
            <div
                style='width: 70vh; height: 70vh;'
            >
                Waiting...
            </div>
        {:then data}
            <div class='container'>
                <BubbleChart
                    Title={"Violence experienced"}
                    cssHeight=70
                    cssWidth=70
                    data={data}
                    fcharge=0.7
                    fcollide=0.5
                    flink=0.3
                />
            </div>
        {:catch error}
            <div style="color: red">{error.message}</div> 
        {/await}
        <div>Change the filters on the sidebar to explore this data.</div>
    {/if}

    {#if slide_index == 5}
        <div>And many migrants do not succeed on their first attempt</div>
        {#await data_attempt}
            <div
                style='width: 70vh; height: 70vh;'
            >
                Waiting...
            </div>
        {:then data}
            <div class='container'>
                <BubbleChart
                    cssHeight=70
                    cssWidth=70
                    data={data}
                    fcenter=0.5
                    fcollide=0.6
                    flink=0.3
                />
            </div>
        {:catch error}
            <div style="color: red">{error.message}</div> 
        {/await}
    {/if}
</Slide>

<style>
    .barchart {
        width: 90vh;
    }

    .flex-center {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .text-container {
        font-size: 24pt;
        width: 80vh;
        animation:
            typing 3.5s steps(40, end),
    }

    .container {
        display: flex;
        align-items: center;
        flex-direction: column;
    }
    
</style>