<script>
    import Slide from '../components/Slide.svelte';
    import Bar from '../components/Bar.svelte';

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let acompany;

    let acompany_dir = null;


    function chooseAccompany(acompany) {
        if (acompany === 'with your family'){
            acompany_dir  = '/images/family.jpg'
        }
        else 
        {
            acompany_dir  ='/images/Alone.jpg'
        }

    }

    chooseAccompany(acompany)

    
</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
        
        <div class='text-container'>
            You know that the easiest route from <span class='data'>{country}</span> to the USA is through
            the southern border from Mexico.
        </div>
        <br>
        <div class='text-container'>
            This is a long, arduous journey, and you debate who you want to 
            travel with. You decide you want to travel
            <select 
                class="input-select" 
                style="color:#E15759;"
                bind:value={acompany}
                onchange={chooseAccompany(acompany)}
            >
            <option>with your family</option>
            <option> alone</option>
            </select>   
            .     
        </div>
        <div class='flex-row'>
        <div class='image-div'>
            <img 
                src={acompany_dir}
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