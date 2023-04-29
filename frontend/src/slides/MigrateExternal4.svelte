<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let amountSpent;
    export let country;
    export let acompany;
    export let mig_ext_violence;
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
        8:'unkown groups'

    }

    let remesa_code = {

    }




    onMount( () => {
        fetch(`http://localhost:8080/mig_ext_violence/${genderCode[gender]}`)
            .then(res => res.json())
            .then(res => {
                violence_group = res.highest_violence_group
                perc_tot_violence = res.perc_violence

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

    

    
</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        
        <div class='text-container'>
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
            <span class='data'>{violence_code[violence_group]}</span>.
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
        <div class='text-container'>
            You chances of remittances based on your migration choices. 
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
    .input-select {
        background-color: #1f1f1f;
        border: none;
        color: white;
        font-family: 'Delicious Handrawn';
        font-size: 24pt;
    }
    .input-select{
        cursor: pointer;
    }
    .input-container {
        font-size: 24pt;
    }
    .profile-select {
        background-color: #1f1f1f;
        border: none;
        color: white;
        font-family: 'Delicious Handrawn';
        font-size: 24pt;
    }

    .data{
        color: #31a693;
        font-family: 'Delicious Handrawn';
        font-size: 24pt;
    }
    
</style>