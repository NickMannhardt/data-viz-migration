<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let name;
    export let gender;
    export let age;
    export let migrationDecision;
    

    let data = [];
    let remesa_amount = "0"


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

    let currency = {
        'SLV': 'Dollars',
        'HND': 'Lempiras', 
        'GT': 'Quetzals'
    }


    let genderCode = {
        'Woman': 1,
        'Man': 2
    }


    
    onMount( () => {
        fetch(`http://localhost:8080/remesa_amount/${countryCode[country]}/${age}/${genderCode[gender]}`)
            .then(res => res.json())
            .then(res => {
                remesa_amount = res.result
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
        
            <div class='input-container'>
            Over the last years, you have heard stories of people migrating to 
            other countries to make a better living. Some families in your area 
            even receive remittances from their relatives abroad, up to 
            <span class='data'>{remesa_amount} {currency[countryCode[country]]} </span>!
            You know that your family has some concerns about migrating.
            </div>
            <br>
            <div class='input-container'>
            Migration is a consequential decision that could change your life, 
            and that of your family, forever.
            </div>
            <br>
            <div class='input-container'> 
            Do you migrate?
            </div>
            <div class='input-container'> 
            <select 
                class="input-select" 
                style="color:#a8181c;"
                bind:value={migrationDecision}
            >
                <option>yes</option>
                <option>no</option>
            </select>
            </div>

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