<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';


    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;

    // let data = new Map();
    // let data = [{label: 1, count: 123},{label: 2, count: 144},{label: 3, count: 74}];
    let data = [];
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
    
    onMount( () => {
        fetch(`http://localhost:8080/tipo_familia/${countryCode[country]}`)
            .then(res => res.json())
            .then(res => {
                data = res.map(d => {
                    return {
                        index: d['tipo_familia'],
                        size: d['count']
                    }
                })
            })
    })

    let xTitle= "Family Type";
    let yTitle = "Count";


</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
>
    <div class='flex-center'>
        <div class='text-container'>
            You probably live in a (type of home). Your family is (type of family e.g. biparental) and you live with (number of people in household) other people in your household.
        </div>
        <br>
        <br>
        <div class='barchart'>
            {#if data.length > 0}
                <Bar bind:data={data} bind:xTitle={xTitle} bind:yTitle={yTitle}/>
            {/if}
        </div>
    </div>
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
    
</style>