<script>
    // TODO
    import { onMount } from 'svelte'

    import Slide from './Slide.svelte'
    import Title from '../slides/Title.svelte'
    import Profile from '../slides/Profile.svelte'
    import Dashboard1 from '../slides/Dashboard1.svelte'

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
            // only scroll to windowHeight stopping points
            // let target = Math.floor((window.pageYOffset + window.innerHeight) / window.innerHeight) * window.innerHeight
            page_index += 1
            let target = window.innerHeight * page_index
            window.scrollTo({
                top: target,
                behavior: 'smooth',
            });
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
            if (e.keyCode === 39) {
                scrollPageDown();
            } else if (e.keyCode === 37) {
                scrollPageUp();
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
    let name = "";
    let gender = "Woman";
    let age = 10;

</script>

<main>
    <Title/>
    {#if page_index >= 1 || animation_active}
    <Profile
        scrollUp={scrollUp}
        scrollDown={scrollDown}
        bind:name={name}
        bind:gender={gender}
    />
    {/if}
    {#if ((page_index >= 2 || animation_active) && name.length > 0)}
    <Dashboard1
        scrollUp={scrollUp}
        scrollDown={scrollDown}
    />
    {/if}
    {#if page_index >= 3 || animation_active}
    <Slide
        scrollUp={scrollUp}
        scrollDown={scrollDown}
    >
        <p>Page 1</p>
    </Slide>
    {/if}
    <Slide></Slide>  <!-- This should remain hidden -->
</main>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Delicious+Handrawn&display=swap');

    main {
        font-family: 'Delicious Handrawn', 'Helvetica', 'Arial', sans-serif;
        color: #FFFFFF;
    }
</style>
