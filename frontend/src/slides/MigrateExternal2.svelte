<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let acompany;
    export let coyote;

    let finance = 'Bank loan'

    let destCountry = 'United States of America'


    let acompany_dir = null;
    let coyote_dir = null;


    function chooseAccompany(acompany) {
        if (acompany === 'with your family'){
            acompany_dir  = 'src/images/family.jpg'
        }
        else 
        {
            acompany_dir  ='src/images/Alone.jpg'
        }

    }

    chooseAccompany(acompany)

    let accompanyId = {
        'with your family': [1,2,3,5,8],
        'alone': 6
    }

    let coyoteID = {
        'yes':  7,
        'no': [1,2,3,5,8]
    }

    function chooseCoyote(coyote) {
        if (coyote === 'yes'){
            coyote_dir = 'src/images/Coyote.jpg'
        }
        else 
        {
            coyote_dir ='src/images/NoCoyote-02-01.jpg'
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
            Due to an overburdened bureaucracy and legal system, you are unable 
            to obtain a visa or the necessary papers for a legal migration. 
            You have to migrate using irregular means. You know that the easiest 
            route from <span class='data'>{country}</span> to the USA is through
            the southern border from Mexico.
        </div>
        <br>
        <div class='text-container'>
            This is a long, arduous journey, and you debate who you want to 
            travel with. You decide you want to travel
            <select 
                class="input-select" 
                style="color:#a8181c;"
                bind:value={acompany}
                onchange={chooseAccompany(acompany)}
            >
            <option>with your family</option>
            <option> alone</option>
            </select>   
            .     
        </div>
        <br>
        <div class='text-container'>
        A coyote, or coyotero, is slang for people smuggler. Smugglers illegally
        accept money to help migrants cross into the United States from Mexico,
        often by guiding the migrants over the hills and through the desert or
        by forging papers and contracts to bypass the slow bureaucratic process.
        Other smugglers, called polleros, transport migrants over the border
        in secret compartments of cars and vans.
            </div>
            <br>
        <div class='input-container'> 
            Do you want to travel with a coyote?
            <br>
            <select 
                class="input-select" 
                style="color:#a8181c;"
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
                src={acompany_dir}
                alt="oops"
                height = "300"
            >
        </div>
        <div class='image-div'>
            <img 
                src={coyote_dir}
                alt="oops"
                height = "300"
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
    .flex-row {
        display: flex;
        flex-direction: row;
    }
    
    
</style>