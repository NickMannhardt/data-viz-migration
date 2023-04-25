<script>
    import { onMount } from 'svelte'

    import Slide from '../components/Slide.svelte'
    import Title from '../slides/Title.svelte'
    import Profile from '../slides/Profile.svelte'
    import Dashboard1 from '../slides/Dashboard1.svelte'
    import PersonaInfo1 from '../slides/PersonaInfo1.svelte'
    import PersonaInfo2 from '../slides/PersonaInfo2.svelte'
    import MigrateExternal from '../slides/MigrateExternal.svelte'
    import MigrateInternal from '../slides/MigrateInternal.svelte'

    // Current page being viewed
    var page_index = 0

    var scrollUp;
    var scrollDown;

    var animation_active = false;

    onMount( async () => {
        // pageHeight = window.innerHeight;
        window.scrollTo({
            top: window.innerHeight * page_index
        })

        function scrollPageDown() {
            if (transition_conditions[page_index + 1]) {
                page_index += 1

                let target = window.innerHeight * page_index
                window.scrollTo({
                    top: target,
                    behavior: 'smooth',
                });
            }
        }
        
        function scrollPageUp() {
            if (page_index > 0) {
                page_index -= 1
            }
            let target = window.innerHeight * page_index
            window.scrollTo({
                top: target,
                behavior: 'smooth',
            });
            animation_active = true;
            setTimeout(() => {
                animation_active = false;
            }, 1000);
        }

        document.addEventListener('keyup', e => {
            if (e.code === 'Space') {
                scrollPageDown();
            }
        });

        document.addEventListener('keydown', e => {
            if (e.target === document.body) {
                if (e.keyCode === 39) {
                    scrollPageDown();
                } else if (e.keyCode === 37) {
                    scrollPageUp();
                }
            }
            if (e.keyCode == 13) {
                scrollPageDown();
            }
        });

        window.addEventListener('resize', e => {
            window.scrollTo({
                top: window.innerHeight * page_index
            })
        })

        scrollUp = scrollPageUp;
        scrollDown = scrollPageDown;
    });

    // user choices
    $: name = "";
    let gender = "Woman";
    let age = 10;
    let country = "El Salvador";
    let rural = "rural"
    let migrationDecision = "yes"
    let income = 3

    $: transition_conditions = {
        0: true,
        1: true,
        2: name.length > 0,
        3: true,
        4: {internal: (migrationDecision == "no") , external: (migrationDecision == "yes")},
        5: true
    }

    console.log(transition_conditions)



</script>

<main>
    <Title/>
    {#if page_index >= 1 || animation_active}
        <Profile
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            bind:name={name}
            bind:gender={gender}
            bind:country={country}
        />
    {/if}
    {#if (page_index >= 2 || animation_active) && transition_conditions[2]}
        <PersonaInfo1
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
            name = {name}
            age = {age}
            gender = {gender}
            bind:rural={rural}
            bind:income = {income}
        />
    {/if}
    {#if (page_index >= 3 || animation_active) && transition_conditions[3]}
        <PersonaInfo2
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
            name = {name}
            age = {age}
            gender = {gender}
            bind:migrationDecision = {migrationDecision}
            
        />
    {/if}
    {#if (page_index >= 4 || animation_active) && transition_conditions[4].external}
        <MigrateExternal
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
            name = {name}
            age = {age}
            gender = {gender}
            
            
        />
    {/if}
    {#if (page_index >= 4 || animation_active) && transition_conditions[4].internal}
        <MigrateInternal
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
            name = {name}
            age = {age}
            gender = {gender}
            
            
        />
    {/if}


    {#if (page_index >= 5 || animation_active) && transition_conditions[5]}
        <Dashboard1
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
        />
    {/if}
    <Slide></Slide>  <!-- This buffer slide should remain hidden -->
</main>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Delicious+Handrawn&display=swap');

    main {
        font-family: 'Delicious Handrawn', 'Helvetica', 'Arial', sans-serif;
        color: #FFFFFF;
    }
</style>
