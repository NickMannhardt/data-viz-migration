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
    export let income;


    let data = [];
    let n_household = [1,2,3,4,5,6,7,8,9,10]
    let incomes = Array.from({ length: 21 }, (_, i) => i * 0.5);
    let avg_income = 500;
    let debt_amount = 0;


    let chartWidth = 600;
    let chartHeight = 350;

    let selected_country = 'GLV';

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

    let rural = "rural";

    onMount( () => {
        fetch(`http://localhost:8080/avg_income_amount/${countryCode[country]}`)
            .then(res => res.json())
            .then(res => {
                data = res.map(d => {
                    return {
                        index: d['avg_income_amount'],
                        size: d['count']
                    }
                })
            })
    })

    let xTitle= "Income";
    let yTitle = "Count";

    
    onMount( () => {
        fetch(`http://localhost:8080/mean_income_amount/${countryCode[country]}`)
            .then(res => res.json())
            .then(res => {
                avg_income = res.result
            })
    })

    onMount( () => {
        fetch(`http://localhost:8080/debt_amount/${countryCode[country]}`)
            .then(res => res.json())
            .then(res => {
                debt_amount = res.result
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
            Filters Text.
        
        <div class='input-container'>
        Hello, {name}.
        You are a {age} year old {gender} from {country}.

        You live in a
        <select 
            class="input-select" 
            style="color:#a8181c;"
            bind:value={rural}
        >
            <option>rural</option>
            <option>urban</option>
        </select>
        area.
        You live in a 
        <select class="profile-select" style="color:#f66d0e;">
            {#each n_household  as number}
                <option>{number}</option>
            {/each}
        </select>
        person household. Your family earns about {avg_income} {currency[countryCode[country]]}.
        You have and average debt of {debt_amount} {currency[countryCode[country]]}.
        You are predominantly concerned with

        <select class="profile-select" style="color:#f66d0e;">
            {#each incomes  as income}
                <option>{income}</option>
            {/each}
        </select>
        
        </div>
        <div class='barchart'>
            {#if data.length > 0}
                <Bar bind:data={data} bind:xTitle={xTitle} bind:yTitle={yTitle}/>
            {/if}
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
    
</style>