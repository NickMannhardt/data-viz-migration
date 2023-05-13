<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';

    import { onMount } from 'svelte';
    import BubbleChart from '../components/BubbleChart.svelte';
    export let scrollUp;
    export let scrollDown;
    export let amountSpent;
    export let country;
    export let acompany;
    export let gender;
    export let violence_group;
    export let age;
    export let coyote;
    let perc_attempt1 = 0.0
    let perc_attempt2 = 0.0
    let perc_attempt3 = 0.0
    let perc_attempt4plus = 0.0

    let perc_tot_violence = 10.0
    let remesa_freq = "Every week or less"

    let countryCode = {
        'El Salvador': 'SLV',
        'Honduras': 'HND',
        'Guatemala': 'GT'
    }

    let currency = {
        'SLV': 'Dollars',
        'HND': 'Lempiras', 
        'GT': 'Quetzals'
    }

    let genderCode = {
        'Woman': 1,
        'Man': 2
    }

    let violence_code ={
        1: 'a traveling companion',
        2: 'the coyote',
        3:'extermination groups',
        4:'organized crime',
        5:'police and / or armed forces',
        6:'groups dedicated to the extraction of natural resources',
        7:'unkown groups',
        8:'unkown groups',
        99: 'no violence',
    }


    let coyote_code = {
        "yes": "with",
        "no": "without"
    }

    let data_remesa = [];
    let data_violence = [];

    let currency_explain = {
        'SLV': 'A single person estimated monthly costs are 607.0$ without rent.',
        'HND': 'A single person estimated monthly costs are 519.5$ (12727.75 Lempiras) without rent.', 
        'GT': 'A single person estimated monthly costs are 636.0$ (4948.08 Quetzals) without rent.'
    }


    onMount( () => {
        fetch(`http://localhost:8080/mig_ext_violence/${genderCode[gender]}`)
            .then(res => res.json())
            .then(res => {
                data_violence = res.map(d => {
                    console.log(violence_code[d['mig_ext_violence_who']])
                    return {
                        label: violence_code[d['mig_ext_violence_who']],
                        value: d['count']
                    }
                })
                console.log(data_violence)
                violence_group = data_violence[0].label
                perc_tot_violence = Math.round(data_violence[0].value)

            })
    })

    onMount( () => {
        fetch(`http://localhost:8080/mig_ext_attempts/${age}/${genderCode[gender]}`)
            .then(res => res.json())
            .then(res => {
                perc_attempt1 = res.perc1
                perc_attempt2 = res.perc2
                perc_attempt3 = res.perc3
                perc_attempt4plus = res.perc4plus

            })
    })

    onMount( () => {
        fetch(`http://localhost:8080/final_remesa_amount/${countryCode[country]}/${age}/${genderCode[gender]}`)
            .then(res => res.json())
            .then(res => {
                data_remesa = res.map(d => {
                    return {
                        index: d['remesa_bracket'],
                        size: d['remesa_pct']
                    }
                })
            })
    })

    let xTitle= "Remesa Bracket";
    let yTitle = "Percentage %";


    

    
</script>

<Slide
    scrollUp={scrollUp}
    allowNext = True
>
    <div class='flex-center'>
        <div class='text-container'>
            Now you’ve decided to travel <span class='data'>{acompany}</span> and <span class='data'>{coyote_code[coyote]}</span> a coyote.
            You have chosen to spend <span class='data'>{amountSpent} thousand {currency[countryCode[country]]}</span>*.
        </div>
        <div class='text-container'>
            The likelihood that you will experience violence on your journey is quite high. 
            <span class='data'>{perc_tot_violence}%</span> of  <span class='data'>{gender}</span> 
            experience violence on their journey. If you do experience violence, 
            it is most likely from <span class='data'>{violence_group}</span>.
        </div>
        <br>
        <div class='text-container'>
            You will proabably not make it on your first attempt. Based on your age and gender
            you are <span class='data'>{perc_attempt1}%</span> likely of attempting the trip once, 
            <span class='data'>{perc_attempt2}%</span> likely of attempting the trip twice,
            <span class='data'>{perc_attempt3}%</span> likely of attempting the trip thrice,
            <span class='data'>{perc_attempt4plus}%</span> likely of attempting the trip 4 times or more.
        </div>
        <br>
        
        {#if data_remesa.length > 0}
            <!-- <Bar
                cssHeight=40
                cssWidth=50
                data={data_remesa}
                xTitle={xTitle}
                yTitle={yTitle}
            /> -->
            <BubbleChart
                Title={"Violence experienced"}
                cssHeight=40
                cssWidth=50
                data={data_violence.slice(0,6)}
            />
        {/if}

        <div class='flex-row'>
            <div class='barchart'>
            </div>
            <div class='barchart'>
                <!-- <BubbleChart
            cssHeight=40
            cssWidth=40
            data={[
                {label: 'A', size: 23},
                {label: 'B', size: 51},
            ]}
            /> -->
            </div>
            
    
        </div>

        
        <div class='text-container-2'>
            *{currency_explain[countryCode[country]]}
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
    .container {
        display: flex;
        flex-direction: column;
        padding: 1vh;

        /* width: 100vh; */
        /* height: 50vh; */
    }

    .flex-row {
        display: flex;
        flex-direction: row;
        margin-left: 20vh;
        margin-top: 5vh;
    }
    
</style>