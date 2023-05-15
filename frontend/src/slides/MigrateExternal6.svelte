<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let coyote;

    let coyote_dir = null;

    let coyoteID = {
        'yes':  7,
        'no': [1,2,3,5,8]
    }

    function chooseCoyote(coyote) {
        if (coyote === 'yes'){
            coyote_dir = 'images/Coyote.jpg'
        }
        else 
        {
            coyote_dir ='images/NoCoyote-02-01.jpg'
        }

    }
    chooseCoyote(coyote)


    
</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        
        <div class='text-container'> 
            Some of your friends suggest you might need a guide. They point you 
            in the direction of a coyote.
        </div>
        <br>
        <div class='text-container'>
            You’re a little bit unsure. A coyote, or coyotero, is slang for 
            people smuggler. Smugglers illegally accept money to help migrants 
            cross into the United States from Mexico, often by guiding the migrants
            over the hills and through the desert or by forging papers and contracts
            to bypass the slow bureaucratic process.
        </div>
        <br>
        <div class='text-container'>
            Traveling with a coyote could be the solution to your problems, but 
            it also comes with a great deal of risk.
        </div>
           <br>
        <div class='input-container'> 
            Do you want to travel with a coyote?
            <br>
            <select 
                class="input-select" 
                style="color:#E15759;"
                bind:value={coyote}
                onchange = {chooseCoyote(coyote)}
            >
                <option>yes</option>
                <option>no</option>
            </select>
        </div>
        <div class='flex-row'>
        <div class='image-div'>
            <img 
                src={coyote_dir}
                alt="oops"
                height = "250"
            >

        </div>
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