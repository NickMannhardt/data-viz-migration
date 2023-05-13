<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';
    import { PUBLIC_API_URL } from '$env/static/public';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let migrationDecision;

    
</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        
        <div class='text-container'>
            Due to an overburdened bureaucracy and legal system, you are unable 
            to obtain a visa or the necessary papers for legal migration.
            You are left at an impasse. Stay at home, or migrate using irregular means.
        </div>
        <br>
        <br>
        <div class='text-container'>
            Do you migrate?
            <select 
                class="input-select" 
                style="color:#E15759;"
                bind:value={migrationDecision}
            >
                <option>yes</option>
                <option>no</option>
            </select>
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
        font-family: 'Inconsolata';
        font-size: 18pt;
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
        font-family: 'Inconsolata';
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
    .flex-row {
        display: flex;
        flex-direction: row;
    }
    
    
</style>