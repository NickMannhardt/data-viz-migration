<script>
    export let gender;
    export let age;
    export let country;

    export let rural;
    export let show_rural

    export let migrationDecision;
    export let show_migration;

    export let acompany;
    export let show_acompany;

    export let avg_income;
    export let debt_amount;
    export let amountSpent;
    export let disabled = true;

    let ages = [...Array(70).keys()];
</script>

<div class="filterContainer">
    <div>Profile and Choices</div>
    <hr/>
    <div class="optionsContainer">
        <select
            bind:value={gender}
            disabled={disabled}
        >
            <option>Man</option>
            <option>Woman</option>
        </select>
        <select
            bind:value={age}
            disabled={disabled}
        >
            {#each ages as ageOption}
                <option value={ageOption}>{ageOption}</option>
            {/each}
        </select>
        <select
            bind:value={country}
            disabled={disabled}
        >
            <option>El Salvador</option>
            <option>Guatemala</option>
            <option>Honduras</option>
        </select>
        {#if show_rural}
            <select
                bind:value={rural}
                disabled={disabled}
            >
                <option>rural</option>
                <option>urban</option>
            </select>
        {/if}
        {#if show_migration}
            <select
                bind:value={migrationDecision}
                disabled={true}
            >
                <option>yes</option>
                <option>no</option>
            </select>
        {/if}
        {#if show_acompany}
            <select
                bind:value={acompany}
                disabled={disabled}
            >
                <option>with your Dad</option>
                <option>with your Mother</option>
                <option>with your Brother</option>
                <option>with a known person</option>
                <option>with your child</option>
                <option> alone</option>
                <option>with a coyote</option>
                <option>with another relative</option>
                <option>with an unfamiliar person</option>
            </select>
        {/if}
    </div>
</div>

<style>
    .filterContainer {
        position: fixed;
        margin-left: 5vh;
        margin-top: 30vh;
        outline: 1px solid white;
        padding: 2vh;
        border-radius: 2vh;
        /* visibility: hidden; */
        opacity: 0.8;

        animation: appear 1s linear;
    }

    @keyframes appear {
        from {
            opacity: 0;
        } 
        to {
            opacity: 1;
        }
    }


    .optionsContainer{
        display: flex;
        flex-direction: column;
    }
</style>