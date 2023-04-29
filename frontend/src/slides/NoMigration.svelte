<script>
    import Slide from '../components/Slide.svelte';
    

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let name;
    export let gender;
    export let age;
    export let income;

 
    
</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        
        <div class='text-container'>
            You've chosen NOT to migrate.
            
        </div>
        <div class='text-container'>
            Some information about your options and outcomes.
        </div>
        <div class='text-container'>
            Your average income is #avg_income_amount #currency.
            You have #saving_months #currency months worth of savings to support your family.
            You have #debt_months #currency months worth of debt to pay off.

            Your top concern is #preocupaciones_first, follwed by #preocupaciones_second
            and #preocupaciones_third.

        </div>


        <div class='text-container'>
            You recieve #x #currency remittances from #remesa_parentesco. They were
            able to migrate aboroad and are now working as #remesa_remit_ocupacion.
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