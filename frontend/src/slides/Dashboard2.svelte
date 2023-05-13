<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';
    import { PUBLIC_API_URL } from '$env/static/public';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let acompany;
    export let gender;
    export let violence_group;
    export let age;
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

    let data_remesa = [];
    // let data_violence = [];

    console.log(`gender: ${gender}`)

    // use this notation so that we can automatically fetch new data when the gender changes
    $: data_violence = fetch(`${PUBLIC_API_URL}/mig_ext_violence/${genderCode[gender]}`)
        .then(res => res.json())
        .then(res => {
            let d_v = res.map(d => {
                return {
                    label: violence_code[d['mig_ext_violence_who']],
                    value: d['count']
                }
            })
            violence_group = d_v[0].label
            perc_tot_violence = d_v[0].value
            return d_v
        })

    onMount( () => {
        fetch(`${PUBLIC_API_URL}/mig_ext_attempts/${age}/${genderCode[gender]}`)
            .then(res => res.json())
            .then(res => {
                perc_attempt1 = res.perc1
                perc_attempt2 = res.perc2
                perc_attempt3 = res.perc3
                perc_attempt4plus = res.perc4plus

            })
    })

    onMount( () => {
        fetch(`${PUBLIC_API_URL}/final_remesa_amount/${countryCode[country]}/${age}/${genderCode[gender]}`)
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
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        
        <!-- <div class='text-container'>
            You have chosen to spend <span class='data'>{amountSpent} thousand {currency[countryCode[country]]}</span> 
            to migrate by <span class='data'>{acompany}</span>.
        </div>
        <div class='text-container'>
            It is a long and hard journey. In particular, you are the victim of violence.
        </div>
        <div class='text-container'>
            From your choices, you are <span class='data'>{perc_tot_violence}%</span> likely that you experience 
            some form of violence during your migration. 
            If you do experience violence, you are most likely to experience violence from 
            <span class='data'>{violence_group}</span>.
        </div>
        <br>
        <br>
        <div class='text-container'>
            You chances of remittances based on your migration choices.
        </div> -->
        {#await data_violence}
            <div
                style='width: 50vh; height: 40vh;'
            >
                Waiting...
            </div>
        {:then data}
            <BubbleChart
                Title={"Violence experienced"}
                cssHeight=70
                cssWidth=70
                data={data.slice(0,6)}
            />
        {:catch error}
            <div style="color: red">{error.message}</div> 
        {/await}
    </div>

    
</Slide>

<style>

    .flex-center {
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .text-container {
        font-family: 'Inconsolata';
        font-size: 18pt;
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
        font-family: 'Inconsolata';
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
    .image-div {
        margin-right: 0vh;
    }
    .flex-row {
        display: flex;
        flex-direction: row;
    }
    
    
</style>