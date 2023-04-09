<script>
    // TODO
    import { onMount } from 'svelte'

    // import Page1 from './Page1.svelte'
    // import Page2 from './Page2.svelte'
    import Slide from './Slide.svelte'
    import Title from './Title.svelte'

    // Current page being viewed
    var page_index = 0

    var scrollUp;
    var scrollDown;

    onMount( async () => {
        // pageHeight = window.innerHeight;

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
            console.log(window.innerHeight)
            window.scrollTo({
                top: window.innerHeight * page_index
            })
        })

        scrollUp = scrollPageUp;
        scrollDown = scrollPageDown;
    });

</script>

<main>
    <Title/>
    <Slide
        scrollUp={scrollUp}
        scrollDown={scrollDown}
    >
        <p>Page 1</p>
    </Slide>
    <Slide
        scrollUp={scrollUp}
        scrollDown={scrollDown}
    >
        <p>Page 2</p>
    </Slide>
    <Slide
        scrollUp={scrollUp}
    >
        <p>Page 3</p>
    </Slide>
</main>

<style>
    main {
        font-family: 'Helvetica', 'Arial', sans-serif;
        color: #FFFFFF;
    }
</style>
