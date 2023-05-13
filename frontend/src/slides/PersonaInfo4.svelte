<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let gender;
    export let age;
    export let migrationDecision;
    

    let data = [];
    let remesa_amount = "0"

    let image_dir = '/images/long_and_arduous_journey.jpg'


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
            Do you migrate?
            <br>
            <br>
            <br>
            <select 
                class="input-select" 
                style="color:#E15759;"
                bind:value={migrationDecision}
            >
                <option>yes</option>
                <option>no</option>
            </select>

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
    .image-div {
        margin-right: 0vh;
    }
    
</style>