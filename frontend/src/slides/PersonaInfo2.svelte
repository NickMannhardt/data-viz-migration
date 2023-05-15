<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';
    import { PUBLIC_API_URL } from '$env/static/public';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let name;
    export let gender;
    export let age;
    export let avg_income;
    export let currency;
    export let countryCode;
    export let debt_amount;



    let data = [];
    let n_household = [1,2,3,4,5,6,7,8,9,10]
    let incomes = Array.from({ length: 21 }, (_, i) => i * 0.5);
    
    
    let preocupaciones = 10


    let selected_country = 'GLV';

    const paddings = {
        top: 50, 
        left: 100,
        right: 50,
        bottom: 50,
    }

    let preocupaciones_first = {
        1: 'Fear of contagion of COVID-19',
        2: 'Limitations or restrictions on mobility due to COVID-19',
        3: 'Can\'t afford to buy food',
        4: 'Lack of work / unemployment',
        5: 'Insecurity / violence',
        6: 'Difficulty paying the rent or loan',
        7:'Interruption or irregularity in educational services',
        8:'Interruption of medical services',
        9:'Medicines shortage',
        10:'Public transport shortage',
        11:'Lack of water',
        12:'Persecution / discrimination',
        13:'Fear of facing a natural threat (hurricanes, volcanic eruptions, plagues, etc.)',
        14:'Other',
        15: 'Without worries'
    }

    let genderCode = {
        'Woman': 1,
        'Man': 2
    }

    let currency_explain = {
        'SLV': 'A single person estimated monthly costs are 607.0$ without rent.',
        'HND': 'A single person estimated monthly costs are 519.5$ (12727.75 Lempiras) without rent.', 
        'GT': 'A single person estimated monthly costs are 636.0$ (4948.08 Quetzals) without rent.'
    }

    let rural = "rural";

    let image_dir = 'images/long_and_arduous_journey.jpg'

    onMount( () => {
        fetch(`${PUBLIC_API_URL}/avg_income_amount/${countryCode[country]}`)
            .then(res => res.json())
            .then(res => {
                data = res.map(d => {
                    return {
                        index: d['avg_income_amount'],
                        size: d['count']
                    }
                })
            })
    })

    let xTitle= "Income";
    let yTitle = "Count";

    
    onMount( () => {
        fetch(`${PUBLIC_API_URL}/mean_income_amount/${countryCode[country]}`)
            .then(res => res.json())
            .then(res => {
                avg_income = res.result
            })
    })

    onMount( () => {
        fetch(`${PUBLIC_API_URL}/debt_amount/${countryCode[country]}`)
            .then(res => res.json())
            .then(res => {
                debt_amount = res.result
            })
    })

    onMount( () => {
        fetch(`${PUBLIC_API_URL}/preocupaciones_first/${countryCode[country]}/${genderCode[gender]}`)
            .then(res => res.json())
            .then(res => {
                preocupaciones = res.result
            })
    })
    
</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        <div class='text-container'>
            
        Your family earns about <span class='data'>{avg_income} {currency[countryCode[country]]}</span>*,
        and you are <span class='data'>{debt_amount} {currency[countryCode[country]]}</span>* in debt.
        <br>
        <br>
        At home, you are predominantly concerned with <span class='data'>{preocupaciones_first[preocupaciones]}</span>.
            
        <!-- <div class='barchart'>
            {#if data.length > 0}
                <Bar 
                    cssHeight=50
                    cssWidth=40
                    data={data.slice(0,7)}
                    xTitle={xTitle}
                    yTitle={yTitle}
                />
            {/if}
        </div> -->

        

        <div class='text-container-2'>
            *{currency_explain[countryCode[country]]}
        </div>
        
        <!-- <div class='image-div'>
            <img 
                src={image_dir}
                alt="oops"
                height="200"
            >
        </div> -->
    </div>

    
</Slide>

<style>
    .barchart {
        
    }

    .flex-center {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .text-container {
        font-size: 18pt;
        font-family: 'Inconsolata';
        width: 80vh;
        animation:
            typing 3.5s steps(40, end),
    }
    .text-container-2 {
        font-size: 12pt;
        font-family: 'Inconsolata';
        width: 80vh;
        animation:
            typing 3.5s steps(40, end),
    }
    .input-select {
        background-color: #1f1f1f;
        border: none;
        color: white;
        font-family: 'Permanent Marker';
        font-size: 18pt;
    }
    .input-select{
        cursor: pointer;
    }
    .input-container {
        font-size: 18pt;
    }
    .profile-select {
        background-color: #1f1f1f;
        border: none;
        color: white;
        font-family: 'Permanent Marker';
        font-size: 18pt;
    }

    .data{
        color: #31a693;
        font-family: 'Permanent Marker';
        font-size: 18pt;
    }
    
</style>