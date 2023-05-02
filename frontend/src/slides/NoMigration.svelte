<script>
    import BubbleChart from '../components/BubbleChart.svelte';
import Slide from '../components/Slide.svelte';
    

    import { onMount } from 'svelte';
    export let scrollUp;
    export let scrollDown;
    export let country;
    export let name;
    export let gender;
    export let age;
    export let avg_income;

    let saving_months = 0;
    let debt_months = 0;
    let preocupaciones_first = 10;
    let preocupaciones_second = 10;

    let image_dir = '/images/Hug.jpg'

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

    let preocupaciones_code = {
        1: 'Fear of contagion of COVID-19',
        2: 'Limitations or restrictions on mobility due to COVID-19',
        3: 'Can\'t afford to buy food',
        4: 'Lack of work / unemployment',
        5: 'Insecurity / violence',
        6: 'Difficulty paying the rent or loan',
        7:'Interruption or irregularity in educational services',
        8:'Interruption of medical services',
        9:'Medicines shortage',
        10:'Public transport shortage',
        11:'Lack of water',
        12:'Persecution / discrimination',
        13:'Fear of facing a natural threat (hurricanes, volcanic eruptions, plagues, etc.)',
        14:'Other',
        15: 'Without worries'
    }
    
    let genderCode = {
        'Woman': 1,
        'Man': 2
    }

    let econ_condition = 1

    let econ_condition_code = {
        1: "Worse",
        2:"It remains the same",
        3: "Getting better",
        99: "Can't tell"
    }

    let remesa_parentesco = 1

    let remesa_parentesco_code = {
        1:'Spouse / Partner',
        2:'Father mother',
        3:'Child',
        4:'Brother',
        5:'Uncle',
        6:'Grandfather',
        7:'Grandson',
        8:'Father-in-law',
        9:'Cousin',
        10:'Nephew',
        11:'Stepchild',
        12:'Son in law daughter in law',
        13:'Former spouse / former partner',
        14:'Other relative',
        15:'Other non-relative',
        99:'NS / NR'

    }

    let remesa_remit_ocupacion = 1;

    let remesa_remit_ocupacion_code = {
        1:'are permanently employed',
        2:'have a temporary or seasonal employment',
        3:'have their own business',
        4:'do informal work',
        5:'work in agricultural production',
        6:'work an agricultural day',
        7:'are unemployed',
        8:'are retired',
        9:'do domestic work',
        10:'are a student',
        11:'do other work',
        99:'do other work'

    }

    onMount( () => {
        fetch(`http://localhost:8080/mean_income_amount/${countryCode[country]}`)
            .then(res => res.json())
            .then(res => {
                avg_income = res.result
            })
    })

    onMount( () => {
        fetch(`http://localhost:8080/saving_months/${countryCode[country]}`)
            .then(res => res.json())
            .then(res => {
                saving_months = res.result
            })
    })

    onMount( () => {
        fetch(`http://localhost:8080/debt_months/${countryCode[country]}`)
            .then(res => res.json())
            .then(res => {
                debt_months = res.result
            })
    })

    onMount( () => {
        fetch(`http://localhost:8080/preocupaciones_first/${countryCode[country]}/${genderCode[gender]}`)
            .then(res => res.json())
            .then(res => {
                preocupaciones_first = res.result
            })
    })

    onMount( () => {
        fetch(`http://localhost:8080/econ_condition/${countryCode[country]}/${genderCode[gender]}`)
            .then(res => res.json())
            .then(res => {
                econ_condition = res.result
            })
    })

    onMount( () => {
        fetch(`http://localhost:8080/remesa_parentesco/${countryCode[country]}/${genderCode[gender]}`)
            .then(res => res.json())
            .then(res => {
                remesa_parentesco = res.result
            })
    })

    onMount( () => {
        fetch(`http://localhost:8080/remesa_remit_ocupacion/${countryCode[country]}/${genderCode[gender]}`)
            .then(res => res.json())
            .then(res => {
                remesa_remit_ocupacion = res.result
            })
    })

 
    
</script>

<Slide 
    scrollUp={scrollUp}
    scrollDown={scrollDown}
    allowNext = True
>
    <div class='flex-center'>
<!--         
        <div class='text-container'>
            You've chosen not to migrate.
            
        </div>
        <div class='text-container'>
            <BubbleChart
                cssHeight=60
                cssWidth=80
                data={[
                    {label: 'A', size: 23},
                    {label: 'B', size: 51},
                ]}
            />
        </div> -->
        <div class='text-container'>
            Your average income is <span class='data'>{avg_income}{currency[countryCode[country]]}</span>.
            You have <span class='data'>{saving_months}</span> months worth of savings to support your family.
            You have <span class='data'>{debt_months}</span> months worth of debt to pay off.

            Your top concern is <span class='data'>{preocupaciones_code[preocupaciones_first]}</span>.

            You believe that the economic condition in your area is getting 
            <span class='data'>{econ_condition_code[econ_condition]}</span>.

        </div>
        <div class='text-container'>
            Your <span class='data'>{remesa_parentesco_code[remesa_parentesco]}</span> was
            able to migrate aboroad and 
            <span class='data'>{remesa_remit_ocupacion_code[remesa_remit_ocupacion]}</span>.
        </div>
        <div class='image-div'>
            <img 
                src={image_dir}
                alt="oops"
                width="500"
            >
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

    .data{
        color: #31a693;
        font-family: 'Delicious Handrawn';
        font-size: 24pt;
    }
    
</style>