<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let finance = 'Bank loan'

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

    let image_dir = 'images/money_willing_to_spend.jpg'


    
</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        <div class='text-container'>
            It would be difficult to fund the journey yourself, so instead, you plan to finance your migration using
            <br>
            <br>
            <select 
                class="input-select" 
                style="color:#E15759;"
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
        margin-left: 0vh;
        margin-top: 0vh;
        margin-bottom: 0vh;
    }
    
</style>