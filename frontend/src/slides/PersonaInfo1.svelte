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


    let n_household = [1,2,3,4,5,6,7,8,9,10]

    const paddings = {
        top: 50, 
        left: 100,
        right: 50,
        bottom: 50,
    }

    let rural = "rural";

    let image_dir = '/images/long_and_arduous_journey.jpg'

</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        <div class='text-container'>
            Hello, <span class='data'>{name}</span>.
            <br>
            <br>
            Over the course of the following slides, you will be faced with the 
            same series of decisions made by Central Americans who are seeking 
            to improve their quality of life by migrating to the United States of America. 
            <br>
            <br>
            As you make your choices, we hope that you reflect on what it might 
            mean to have to leave your roots, your family, and your country in
             search of a better future. Let’s begin.
             <br>
             <br>

            <div class='input-container'>
            You are a <span class='data'>{age}</span> year old 
            <span class='data'>{gender}</span> from <span class='data'>{country}</span>.
            <br>
            <br>
            You live in a
            <select 
                class="input-select" 
                style="color:#E15759;"
                bind:value={rural}
            >
                <option>rural</option>
                <option>urban</option>
            </select>
            area.
            You live in a 
            <select class="profile-select" style="color:#F2832B;">
                {#each n_household  as number}
                    <option>{number}</option>
                {/each}
            </select>
            person household.
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
    
</style>