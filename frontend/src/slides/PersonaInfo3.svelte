<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';
    import { PUBLIC_API_URL } from '$env/static/public';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let gender;
    export let age;
    

    let data = [];
    let remesa_amount = "0"

    let image_dir = 'images/DoYouMigrate.jpg'


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

    let currency_explain = {
        'SLV': 'A single person estimated monthly costs are 607.0$ without rent.',
        'HND': 'A single person estimated monthly costs are 519.5$ (12727.75 Lempiras) without rent.', 
        'GT': 'A single person estimated monthly costs are 636.0$ (4948.08 Quetzals) without rent.'
    }
    
    onMount( () => {
        fetch(`${PUBLIC_API_URL}/remesa_amount/${countryCode[country]}/${age}/${genderCode[gender]}`)
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
            other countries to make a better living. 
            <br>
            <br>
            Some families in your area receive remittances from their relatives abroad, up to 
            <span class='data'>{remesa_amount} {currency[countryCode[country]]}</span>*!
            With that kind of money, you could begin paying off your family’s debt for good.
            <br>
            <br>
            You know that your family has some concerns about migrating. It is a
             dangerous journey, and some people never come back. Yet it is a decision
              that could change your destiny, and the wellbeing of your family, forever.
            </div>
            <br>
            <br>
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
    .image-div {
        margin-right: 0vh;
    }
    
</style>