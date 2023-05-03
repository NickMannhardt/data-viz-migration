<script>
    
    import { onMount } from 'svelte';
    import Slide from '../components/Slide.svelte'

    export let scrollUp;
    export let scrollDown;
    export let name;
    export let gender;
    export let country;
    export let age;

    let ages = [...Array(70).keys()];

    let female_avatars = [
        'images/avatar_2.png',
        'images/avatar_3.png'
    ]
    let male_avatars = [
        'images/avatar_1.png',
        'images/avatar_4.png'
    ]
    
    let image_dir = null;

    function chooseAvatar(gender) {
        if (gender === "Woman") {
            let i = Math.floor(Math.random() * female_avatars.length);
            image_dir = female_avatars[i];
        } else {
            let i = Math.floor(Math.random() * male_avatars.length);
            image_dir = male_avatars[i];
        }
    }

    chooseAvatar(gender);



</script>

<Slide
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext={name.length > 0}
    shifted={true}
>
    <div class='flex-center'>
        <div class='flex-row'>
            <div class='image-div'>
                <img 
                    src={image_dir}
                    alt="oops"
                    width="300"
                >
            </div>
            <div class="flex-center">
                <div class='input-container'>
                    Your name is 
                    <input 
                        bind:value={name}
                        class="name-input" 
                        style="color:#a8181c;" 
                        type="text"
                        placeholder="Name"
                    >
                    .
                    <br>
                    You are a 
                    <select 
                        class="profile-select" 
                        style="color:#f66d0e;" 
                        bind:value={age}
                    >
                        {#each ages as ageOption}
                            <option value={ageOption}>{ageOption}</option>
                        {/each}
                    </select>
                    year old
                    <select 
                        class="profile-select" 
                        style="color:#31a693;" 
                        bind:value={gender}
                        onchange={chooseAvatar(gender)}
                    >
                        <option>Woman</option>
                        <option>Man</option>
                    </select>
                    <br>
                    in
                    <select 
                        class="profile-select" 
                        style="color:#a8181c;"
                        bind:value={country}
                    >
                        <option>El Salvador</option>
                        <option>Guatemala</option>
                        <option>Honduras</option>
                    </select>
                </div>
            </div>
        </div>
    </div>
</Slide>

<style>
    .profile-select {
        background-color: #1f1f1f;
        border: none;
        color: white;
        font-family: 'Delicious Handrawn';
        font-size: 24pt;
    }
    .profile-select:hover{
        cursor: pointer;
    }
    *:focus {
        outline: none;
    }
    .name-input {
        background-color: #1f1f1f;
        border: none;
        border-bottom: solid white;
        color: white;
        font-family: 'Delicious Handrawn';
        font-size: 24pt;
        width: 15vh;
        text-align: center;
    }
    .flex-center {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .flex-row {
        display: flex;
        flex-direction: row;
    }
    .input-container {
        font-size: 24pt;
    }
    .image-div {
        margin-right: 10vh;
    }
</style>