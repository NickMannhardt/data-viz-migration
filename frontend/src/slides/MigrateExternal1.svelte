<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';

    import { onMount } from 'svelte';
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

    let image_dir = '/images/money_willing_to_spend.jpg'


    
</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        
        <div class='text-container'>
            You've chosen to migrate! Now you'll need to make some preparations.
            It is a long road from <span class='data'>{country}</span> to the USA.

            You are planning to finance your migration using. Even as you prepare, one of 
            the most consequential questions of your journey is weighing on you:
            how you will travel, and with whom.
        </div>
        <br>
        <div class='text-container'>
            You are planning to finance your migration using 
            means of financing
            <select 
                class="input-select" 
                style="color:#a8181c;"
                bind:value={finance}
            >
                <option>Bank loan</option>
                <option>Mortgaged the house to the bank</option>
                <option>Loans with lender</option>
                <option>Cooperative loan</option>
                <option>Loan from a relative or friend abroad</option>
                <option>Gift from a relative or friend abroad</option>
                <option>Savings</option>
                <option>Family loan in the country</option>
                <option>With his work when arriving at the destination</option>
                <option>Sold property or property</option>
                <option>Other</option>
                <option>I don't wish to respond</option>
            </select>
        </div>
        <br>
        <div class='text-container'>
            Even as you prepare, one of the most consequential questions of your
             journey is weighing on you: how you will travel, and with whom.
        </div>
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

    .image-div {
        margin-right: 0vh;
    }
    
</style>