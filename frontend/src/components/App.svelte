<script>
    import { onMount } from 'svelte'

    import Slide from '../components/Slide.svelte'
    import Title from '../slides/Title.svelte'
    import Profile from '../slides/Profile.svelte'
    import Dashboard1 from '../slides/Dashboard1.svelte'
    import PersonaInfo1 from '../slides/PersonaInfo1.svelte'
    import PersonaInfo2 from '../slides/PersonaInfo2.svelte'
    import PersonaInfo3 from '../slides/PersonaInfo3.svelte'
    import PersonaInfo4 from '../slides/PersonaInfo4.svelte'
    import NoMigration from '../slides/NoMigration.svelte'
    import MigrateExternal1 from '../slides/MigrateExternal1.svelte'
    import MigrateExternal2 from '../slides/MigrateExternal2.svelte'
    import MigrateExternal3 from '../slides/MigrateExternal3.svelte'
    import MigrateExternal4 from '../slides/MigrateExternal4.svelte'
    import MigrateExternal5 from '../slides/MigrateExternal5.svelte'
    import MigrateExternal6 from '../slides/MigrateExternal6.svelte'
    import MigrateExternal7 from '../slides/MigrateExternal7.svelte'
    import ScatterTest from '../slides/ScatterTest.svelte';
    import Filters from '../components/Filters.svelte';
    import Bar from '../components/Bar.svelte';

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
            console.log(`index: ${page_index}`)
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
            console.log(`index: ${page_index}`)
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
    let rural = "rural";
    let migrationDecision = "yes";
    let avg_income = 500;
    let debt_amount = 10;
    let amountSpent = 10;
    let acompany = 'with your family';
    let mig_ext_violence = 0;
    $: amountwilling = "";
    let finance = 'Bank loan';
    let coyote = "yes" 

    let currency = {
        'SLV': 'Dollars',
        'HND': 'Lempiras', 
        'GT': 'Quetzals'
    }

    let countryCode = {
        'El Salvador': 'SLV',
        'Honduras': 'HND',
        'Guatemala': 'GT'
    }

    $: transition_conditions = {
        0: true,
        1: true,
        2: name.length > 0,
        3: true,
        4: true,
        5: true,
        6: {internal: (migrationDecision == "no") , external: (migrationDecision == "yes")},
        7: {internal: (migrationDecision == "no") , external: (migrationDecision == "yes")},
        8: {internal: (migrationDecision == "no") , external: (migrationDecision == "yes")},
        9: {internal: (migrationDecision == "no") , external: (migrationDecision == "yes")},
        10: {internal: (migrationDecision == "no") , external: (migrationDecision == "yes")},
        11: {internal: (migrationDecision == "no") , external: (migrationDecision == "yes")},
        12: {internal: (migrationDecision == "no") , external: (migrationDecision == "yes")},
    }

    console.log(`decision: ${migrationDecision}`)



</script>

<main>
    {#if page_index >= 2}
        <Filters
            disabled={!(page_index >= 4 && transition_conditions[4].internal) && !(page_index >= 7 && transition_conditions[7].external)}
            bind:gender={gender}
            bind:country={country}
            bind:age={age}
            bind:rural={rural}
            show_rural={page_index >= 3}
            bind:migrationDecision={migrationDecision}
            show_migration={page_index >= 4}
            bind:acompany={acompany}
            show_acompany={page_index >=6}
        />
    {/if}
    <!-- <ScatterTest/> -->
    <Title/>
    {#if page_index >= 1 || animation_active}
        <Profile
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            bind:name={name}
            bind:gender={gender}
            bind:country={country}
            bind:age = {age}
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
            bind:rural={rural}
            bind:avg_income = {avg_income}
            bind:debt_amount = {debt_amount}
            bind:currency = {currency}
            bind:countryCode = {countryCode}
        />
    {/if}
    {#if (page_index >= 4 || animation_active) && transition_conditions[4]}
        <PersonaInfo3
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
            name = {name}
            age = {age}
            gender = {gender}
            bind:migrationDecision = {migrationDecision}
            
        />
    {/if}
    {#if (page_index >= 5 || animation_active) && transition_conditions[5]}
        <PersonaInfo4
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
            name = {name}
            age = {age}
            gender = {gender}
            bind:migrationDecision = {migrationDecision}
            
        />
    {/if}
    {#if (page_index >= 6 || animation_active) && transition_conditions[6].external}
        <MigrateExternal1
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
            name = {name}
            age = {age}
            gender = {gender}
        />
    {/if}
    {#if (page_index >= 6 || animation_active) && transition_conditions[6].internal}
        <NoMigration
            scrollUp={scrollUp}
            country={country}
            name = {name}
            age = {age}
            gender = {gender}
            avg_income = {avg_income}
            currency = {currency}
            countryCode = {countryCode}
        /> 
    {/if}

    {#if (page_index >= 7 || animation_active) && transition_conditions[7].external}
        <MigrateExternal2
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
            avg_income = {avg_income}
            debt_amount={debt_amount}
            currency = {currency}
            countryCode = {countryCode}
            bind:amountSpent={amountSpent}
        />
    {/if}
    {#if (page_index >= 7 || animation_active) && transition_conditions[7].internal}
        <NoMigration
            scrollUp={scrollUp}
            country={country}
            name = {name}
            age = {age}
            gender = {gender}
            avg_income = {avg_income}
            currency = {currency}
            countryCode = {countryCode}
        /> 
    {/if}
    {#if (page_index >= 8 || animation_active) && transition_conditions[8].external}
        <MigrateExternal3
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
            name = {name}
            age = {age}
            gender = {gender}
            bind:finance = {finance}
        />
    {/if}
    {#if (page_index >= 8 || animation_active) && transition_conditions[8].internal}
        <NoMigration
            scrollUp={scrollUp}
            country={country}
            name = {name}
            age = {age}
            gender = {gender}
            avg_income = {avg_income}
            currency = {currency}
            countryCode = {countryCode}
            
        /> 
    {/if}


    {#if (page_index >= 9 || animation_active) && transition_conditions[9].external}
        <MigrateExternal4
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
            bind:migrationDecision={migrationDecision}
        />
    {/if}

    {#if (page_index >= 9 || animation_active) && transition_conditions[9].internal}
        <Dashboard1
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
        />
    {/if}

    {#if (page_index >= 10 || animation_active) && transition_conditions[10].external}
        <MigrateExternal5
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
            bind:acompany ={acompany}
        />
    {/if}

    {#if (page_index >= 10 || animation_active) && transition_conditions[10].internal}
        <Dashboard1
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
        />
    {/if}

    {#if (page_index >= 11 || animation_active) && transition_conditions[11].external}
        <MigrateExternal6
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
            bind:coyote ={coyote}
        />
    {/if}

    {#if (page_index >= 11 || animation_active) && transition_conditions[11].internal}
        <Dashboard1
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
        />
    {/if}

    {#if (page_index >= 12 || animation_active) && transition_conditions[12].external}
        <MigrateExternal7
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country} 
            name = {name}
            age = {age}
            gender = {gender}
            currency = {currency}
            countryCode = {countryCode}
            amountSpent = {amountSpent}
            acompany = {acompany}
            coyote = {coyote}
        />
    {/if}
    {#if (page_index >= 12 || animation_active) && transition_conditions[12].internal}
        <Dashboard1
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
        />
    {/if}

    <!-- {#if (page_index >= 7 || animation_active) && transition_conditions[7].internal}
        <Dashboard1
            scrollUp={scrollUp}
            scrollDown={scrollDown}
            country={country}
        />
    {/if}-->
    <Slide></Slide>  <!-- This buffer slide should remain hidden -->
</main>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Delicious+Handrawn&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Inconsolata&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap');

    @import url('https://fonts.googleapis.com/css2?family=Hind+Vadodara&display=swap');
    main {
        font-family: 'Delicious Handrawn', 'Helvetica', 'Arial', sans-serif;
        color: #FFFFFF;
    }


</style>
