<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';
    import App from '../components/App.svelte';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let avg_income;
    export let country;
    export let debt_amount;
    export let amountSpent;

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

    let amounts = Array.from({ length: 50 }, (_, i) => (i+1) * 1)
    let image_dir = 'images/Envelope.jpg'
    
    
</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        
        <div class='text-container' >
            Your household earns <span class='data'>{avg_income} {currency[countryCode[country]]}</span>
            per month, and is in <span class='data'>{debt_amount} {currency[countryCode[country]]}</span> debt.
            You don't know how much you will have to spend migrating, but you do
             know that it might take multiple attempts, if you are successful 
             at all. If you make it, however, you will be able to support your 
             family and pay off you debt with remittances.
        </div>
        <br>
        <div class='text-container'>
            How much are you willing to spend on migrating? 
        </div>
        <br>
        <div class='text-container'>
            <select class="profile-select" style="color:#f66d0e;" bind:value={amountSpent}>
                {#each amounts  as amountSpent}
                    <option>{amountSpent}</option>
                {/each}
            </select>
            thousand <span class='data'>{currency[countryCode[country]]}</span>
        </div>
        <div class='image-div'>
            <img 
                src={image_dir}
                alt="oops"
                width="500"
            >
        </div> 
    </div>

    
</Slide>

<style>
    .profile-select {
        background-color: #1f1f1f;
        border: none;
        color: white;
        font-family: 'Delicious Handrawn';
        font-size: 24pt;
    }
    .profile-select:hover{
        cursor: pointer;
    }

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