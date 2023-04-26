<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let acompany;

    let finance = 'Bank loan'

    let destCountry = 'United States of America'

    let accompanyId = {
        'with your Dad': 1,
        'with your Mother': 2,
        'with your Brother': 3,
        'with a known person': 4,
        'with your child': 5,
        'alone': 6,
        'with a coyote': 7,
        'with another relative': 8,
        'with an unfamiliar person':9,
    }


    
</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        
        <div class='text-container'>
            Due to an overburdened bureaucracy and legal system, you are unable 
            to obtain a visa or the necessary papers for a legal migration. 
            You have to migrate using irregular means. You know that the easiest 
            route from <span class='data'>{country}</span> to the USA is through
            the southern border from Mexico.
        </div>
        <br>
        <div class='text-container'>
            This is a long, arduous journey, and you debate who you want to 
            travel with. You decide you want to travel with
            <select 
                class="input-select" 
                style="color:#a8181c;"
                bind:value={acompany}
            >
            <option>with your Dad</option>
            <option>with your Mother</option>
            <option>with your Brother</option>
            <option>with a known person</option>
            <option>with your child</option>
            <option> alone</option>
            <option>with a coyote</option>
            <option>with another relative</option>
            <option>with an unfamiliar person</option>
            </select>        
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