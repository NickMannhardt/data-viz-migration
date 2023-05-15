<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';

    import { onMount } from 'svelte';
  import App from '../components/App.svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;


    let finance = 'Bank loan'

    let destCountry = 'United States of America'

    let migExtFinance = {
        'Bank loan': 1,
        'Mortgaged the house to the bank': 2,
        'Loans with lender': 3,
        'Cooperative loan': 4,
        'Loan from a relative or friend abroad': 5,
        'Gift from a relative or friend abroad': 6,
        'Savings': 7,
        'Family loan in the country': 8,
        'With his work when arriving at the destination':9,
        'Sold property or property':10,
        'Other':11,
        'I don\'t wish to respond':99
    }

    let image_dir = 'images/DoYouMigrate.jpg'


    
</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        
        <div class='text-container'>
            Now that you’ve decided to migrate, it is time to plan your journey…
            <br>
            <br>
            Due to an overburdened bureaucracy and legal system, you are unable 
            to obtain a visa or the necessary papers for legal migration.
            <br>
            <br>
            You are left at an impasse. Stay at home, or migrate using irregular means.
        <div class='image-div'>
            <img 
                src={image_dir}
                alt="oops"
                width="600"
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